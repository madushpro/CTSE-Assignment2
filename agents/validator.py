from typing import Dict, Any, List, Optional
import sys
import os
import logging

# Add tools directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'tools'))

from validation_tool import (
    validate_plan_structure,
    validate_budget_compliance,
    validate_trip_duration,
    comprehensive_plan_validation
)

# Try to import Ollama client, fall back gracefully if not available
try:
    from ollama_client import create_ollama_client, OllamaClient
    OLLAMA_AVAILABLE = True
except ImportError:
    OLLAMA_AVAILABLE = False

logger = logging.getLogger(__name__)


class PlanValidatorAgent:
    """Agent responsible for validating and quality-checking travel plans using Ollama LLM."""
    
    def __init__(self, use_ollama: bool = True):
        """Initialize Plan Validator Agent.
        
        Args:
            use_ollama (bool): Whether to use Ollama LLM (default: True)
        """
        self.role = "Quality Assurance Specialist"
        self.goal = "Ensure the final travel plan meets all quality standards and user requirements"
        self.backstory = (
            "You are a meticulous QA specialist with 12+ years of experience in travel planning. "
            "You have an eye for detail and understand what makes a great travel plan: clarity, "
            "feasibility, value for money, and adherence to user constraints. You ensure every plan "
            "is polished, practical, and ready for delivery."
        )
        self.tools_used = [
            "validate_plan_structure",
            "validate_budget_compliance",
            "validate_trip_duration",
            "comprehensive_plan_validation"
        ]
        
        # Initialize Ollama client if available
        self.ollama_client: Optional[OllamaClient] = None
        self.use_ollama = use_ollama and OLLAMA_AVAILABLE
        
        if self.use_ollama:
            try:
                self.ollama_client = create_ollama_client()
                logger.info("✓ Ollama LLM initialized for Plan Validator Agent")
            except Exception as e:
                logger.warning(f"Could not initialize Ollama: {str(e)}. Using mock data.")
                self.use_ollama = False
    
    def validate_complete_plan(
        self,
        plan: str,
        num_days: int,
        estimated_cost: float,
        user_budget: float
    ) -> Dict[str, Any]:
        """
        Perform comprehensive validation of entire travel plan.
        
        Args:
            plan (str): The complete travel plan text
            num_days (int): Expected trip duration
            estimated_cost (float): Calculated trip cost
            user_budget (float): User's budget limit
        
        Returns:
            Dict[str, Any]: Comprehensive validation results
        
        Raises:
            ValueError: If inputs invalid
        """
        
        if not plan or len(plan) < 50:
            raise ValueError("Plan text too short for validation")
        
        validation_result = comprehensive_plan_validation(
            plan,
            num_days,
            estimated_cost,
            user_budget
        )
        
        # Add plan text for LLM analysis
        validation_result['plan_text'] = plan
        
        # Enhance with validator-specific insights
        validation_result['validator_notes'] = self._generate_validator_notes(
            validation_result
        )
        validation_result['quality_score'] = validation_result['final_score']
        
        return validation_result
    
    def check_plan_quality(self, plan: str) -> Dict[str, Any]:
        """
        Check the structural quality of a plan.
        
        Args:
            plan (str): Travel plan text
        
        Returns:
            Dict[str, Any]: Quality assessment with score and feedback
        """
        
        result = validate_plan_structure(plan)
        
        # Add quality assessment
        quality_assessment = {
            "is_valid": result['is_valid'],
            "quality_score": result['score'],
            "quality_level": self._score_to_quality_level(result['score']),
            "issues": result['issues'],
            "improvement_suggestions": self._generate_improvements(result)
        }
        
        return quality_assessment
    
    def verify_budget_compliance(
        self,
        estimated_cost: float,
        user_budget: float,
        is_strict: bool = False
    ) -> Dict[str, Any]:
        """
        Verify that plan stays within budget constraints.
        
        Args:
            estimated_cost (float): Total estimated cost
            user_budget (float): User's budget limit
            is_strict (bool): If True, require minimum 10% buffer
        
        Returns:
            Dict[str, Any]: Budget compliance check
        """
        
        budget_result = validate_budget_compliance(
            "Validation check",
            estimated_cost,
            user_budget
        )
        
        compliance = {
            "compliant": budget_result['within_budget'],
            "cost": estimated_cost,
            "budget": user_budget,
            "remaining": budget_result['remaining'],
            "status": budget_result['status']
        }
        
        if is_strict and budget_result['remaining'] < (user_budget * 0.1):
            compliance['warning'] = "Budget buffer is less than 10% - recommend review"
            compliance['compliant'] = False
        
        return compliance
    
    def verify_itinerary_coverage(self, plan: str, num_days: int) -> Dict[str, Any]:
        """
        Verify that itinerary covers all trip days.
        
        Args:
            plan (str): Travel plan text
            num_days (int): Expected trip duration
        
        Returns:
            Dict[str, Any]: Coverage verification result
        """
        
        coverage = validate_trip_duration(plan, num_days)
        
        return {
            "all_days_covered": coverage['is_valid'],
            "days_found": coverage['days_in_plan'],
            "days_expected": coverage['expected_days'],
            "missing_days": coverage['missing_days']
        }
    
    def generate_validation_report(
        self,
        plan: str,
        num_days: int,
        estimated_cost: float,
        user_budget: float
    ) -> str:
        """
        Generate a detailed validation report.
        
        Args:
            plan (str): Travel plan
            num_days (int): Trip duration
            estimated_cost (float): Estimated cost
            user_budget (float): User budget
        
        Returns:
            str: Formatted validation report
        """
        
        validation = self.validate_complete_plan(plan, num_days, estimated_cost, user_budget)
        budget_check = self.verify_budget_compliance(estimated_cost, user_budget)
        coverage_check = self.verify_itinerary_coverage(plan, num_days)
        
        report = f"""
{'='*70}
TRAVEL PLAN VALIDATION REPORT
{'='*70}

OVERALL STATUS
--------------
{'✓ APPROVED FOR DELIVERY' if validation['ready_for_delivery'] else '✗ REQUIRES REVISION'}
Quality Score: {validation['quality_score']:.1f}/100
Quality Level: {self._score_to_quality_level(validation['quality_score'])}

VALIDATION RESULTS
------------------
1. Plan Structure: {self._check_mark(validation['structure_validation']['is_valid'])}
   Score: {validation['structure_validation']['score']:.1f}/100
   
2. Budget Compliance: {self._check_mark(budget_check['compliant'])}
   Cost: Rs. {estimated_cost:,.2f}
   Budget: Rs. {user_budget:,.2f}
   Remaining: Rs. {budget_check['remaining']:,.2f}
   
3. Itinerary Coverage: {self._check_mark(coverage_check['all_days_covered'])}
   Days: {coverage_check['days_found']}/{coverage_check['days_expected']}
   {f"Missing Days: {coverage_check['missing_days']}" if coverage_check['missing_days'] else "All days covered"}

ISSUES IDENTIFIED
-----------------
"""
        
        all_issues = validation['structure_validation']['issues']
        if not all_issues:
            report += "✓ No issues found\n"
        else:
            for issue in all_issues:
                report += f"• {issue}\n"
        
        report += f"""
RECOMMENDATIONS
---------------
"""
        
        for rec in validation['recommendations']:
            report += f"• {rec}\n"
        
        report += f"""
VALIDATOR NOTES
---------------
{validation.get('validator_notes', 'Plan meets quality standards.')}

{'='*70}
FINAL VERDICT: {'APPROVED' if validation['ready_for_delivery'] else 'REVISION NEEDED'}
{'='*70}
"""
        
        return report
    
    
    def _generate_llm_feedback(self, plan: str, validation_result: Dict) -> str:
        """Generate LLM-based validation feedback.
        
        Args:
            plan: Travel plan text
            validation_result: Validation results
            
        Returns:
            str: LLM-generated feedback
        """
        if not self.ollama_client:
            raise RuntimeError("Ollama client not initialized")
        
        prompt = f"""Review this travel plan and provide detailed quality feedback:

{plan[:1000]}...

Qua lity Score: {validation_result['final_score']:.1f}/100
Issues Found: {len(validation_result['structure_validation']['issues'])}

Provide:
1. Overall assessment of plan quality
2. Strengths of the plan
3. Areas for improvement
4. Specific recommendations for enhancement
5. Readiness for delivery verdict"""
        
        system_prompt = (
            "You are an expert travel plan reviewer. "
            "Provide constructive, specific feedback on travel itineraries. "
            "Format: clear sections with actionable recommendations."
        )
        
        logger.info("Generating LLM validation feedback")
        feedback = self.ollama_client.generate(
            prompt=prompt,
            system=system_prompt,
            temperature=0.6,
            max_tokens=500
        )
        
        if not feedback or len(feedback.strip()) < 50:
            raise ValueError("LLM returned empty or too-short response")
        
        return feedback
    
    def _generate_validator_notes(self, validation: Dict) -> str:
        """Generate detailed validator notes.
        
        Uses Ollama LLM for intelligent feedback with fallback to rules-based.
        """
        
        # Try LLM first
        if self.use_ollama and self.ollama_client:
            try:
                llm_feedback = self._generate_llm_feedback(
                    validation.get('plan_text', ''),
                    validation
                )
                return f"[LLM Analysis]\n{llm_feedback}"
            except Exception as e:
                logger.warning(f"LLM feedback failed: {str(e)}. Using fallback.")
        
        # Fallback to rules-based notes
        notes = []
        
        if validation['ready_for_delivery']:
            notes.append("✓ Plan is ready for customer delivery")
        else:
            notes.append("Plan requires revision before delivery")
        
        if validation['final_score'] >= 90:
            notes.append("Excellent quality - premium travel experience")
        elif validation['final_score'] >= 75:
            notes.append("Good quality - solid travel plan")
        else:
            notes.append("Fair quality - consider improvements")
        
        if validation['budget_validation']['status'] == 'PASS':
            notes.append("Budget well-managed with comfortable margin")
        elif validation['budget_validation']['status'] == 'WARNING':
            notes.append("Budget is tight but manageable")
        else:
            notes.append("Budget exceeded - plan requires adjustment")
        
        return "\n".join(notes)
    
    def _score_to_quality_level(self, score: float) -> str:
        """Convert score to quality level description."""
        if score >= 90:
            return "Excellent"
        elif score >= 80:
            return "Very Good"
        elif score >= 70:
            return "Good"
        elif score >= 60:
            return "Fair"
        else:
            return "Needs Improvement"
    
    def _check_mark(self, is_valid: bool) -> str:
        """Return check mark or x mark."""
        return "✓ Pass" if is_valid else "✗ Fail"
    
    def _generate_improvements(self, quality_result: Dict) -> List[str]:
        """Generate improvement suggestions from quality check."""
        
        suggestions = []
        
        if quality_result['score'] < 70:
            suggestions.append("Add more specific day-by-day details")
        
        if not any("accommodation" in issue.lower() for issue in quality_result['issues']):
            suggestions.append("Specify accommodation preferences")
        
        if not any("activity" in issue.lower() or "attraction" in issue.lower() 
                   for issue in quality_result['issues']):
            suggestions.append("Add more activity descriptions")
        
        if not suggestions:
            suggestions.append("Plan already has good structure and coverage")
        
        return suggestions
    
    
    def get_agent_info(self) -> Dict[str, str]:
        """Get agent role information.
        
        Returns:
            Dict[str, str]: Agent metadata
        """
        return {
            "role": self.role,
            "goal": self.goal,
            "backstory": self.backstory,
            "uses_ollama": self.use_ollama,
            "model": "llama3:8b" if self.use_ollama else "mock_data"
        }


if __name__ == "__main__":
    # Test the Plan Validator Agent
    print("\n=== Plan Validator Agent Tests ===\n")
    
    agent = PlanValidatorAgent(use_ollama=False)  # Use mock for testing
    
    # Mock plan
    test_plan = """
    ELLA TRAVEL PLAN - 3 DAYS
    
    Day 1: Arrival
    - Reach Ella by train
    - Check into accommodation (mid-range hotel)
    - Explore local town
    - Have traditional dinner
    
    Day 2: Adventure
    - Hike to Nine Arch Bridge (historic railway bridge)
    - Visit Little Adam's Peak
    - Relax at local café
    - Experience local culture
    
    Day 3: Relaxation
    - Visit Ravana Falls
    - Nature walk
    - Shopping at local market
    
    Cost: Rs. 15,000 for accommodation, food, transport, activities
    """
    
    try:
        # Test validation
        print("Test: Complete plan validation")
        validation = agent.validate_complete_plan(test_plan, 3, 15000, 20000)
        print(f"Ready for Delivery: {validation['ready_for_delivery']}")
        print(f"Quality Score: {validation['quality_score']}/100\n")
        
        # Test report
        print("Generating validation report...")
        report = agent.generate_validation_report(test_plan, 3, 15000, 20000)
        print(report)
        
    except ValueError as e:
        print(f"Error: {e}")
