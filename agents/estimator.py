"""
Budget Estimator Agent - STUDENT 3 CONTRIBUTION

Role: Calculates and provides detailed cost breakdowns
Goal: Ensure transparent, accurate budget planning
Backstory: Finance professional specializing in travel budgeting

STUDENT 3: Responsible for this agent
- Implements cost estimation using LLM-assisted reasoning
- Creates personalized budget recommendations
- Handles fallback to calculated mock data if LLM unavailable
"""

from typing import Dict, Any, Optional, List
import sys
import os
import logging

# Add tools directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'tools'))

from cost_calculator_tool import calculate_travel_cost, breakdown_daily_cost, validate_within_budget

# Try to import Ollama client, fall back gracefully if not available
try:
    from ollama_client import create_ollama_client, OllamaClient
    OLLAMA_AVAILABLE = True
except ImportError:
    OLLAMA_AVAILABLE = False

logger = logging.getLogger(__name__)


class BudgetEstimatorAgent:
    """Agent responsible for budget calculations and cost estimation using Ollama LLM."""
    
    def __init__(self, use_ollama: bool = True):
        """Initialize Budget Estimator Agent.
        
        Args:
            use_ollama (bool): Whether to use Ollama LLM (default: True)
        """
        self.role = "Travel Budget Specialist"
        self.goal = "Provide accurate, transparent cost estimates and budget recommendations"
        self.backstory = (
            "You are a finance expert specializing in travel budgeting with 8+ years of experience. "
            "You understand the true costs of traveling in Sri Lanka, including hidden expenses. "
            "You help travelers make informed decisions and optimize their spending."
        )
        self.tools_used = ["calculate_travel_cost", "breakdown_daily_cost", "validate_within_budget"]
        
        # Initialize Ollama client if available
        self.ollama_client: Optional[OllamaClient] = None
        self.use_ollama = use_ollama and OLLAMA_AVAILABLE
        
        if self.use_ollama:
            try:
                self.ollama_client = create_ollama_client()
                logger.info("✓ Ollama LLM initialized for Budget Estimator Agent")
            except Exception as e:
                logger.warning(f"Could not initialize Ollama: {str(e)}. Using mock data.")
                self.use_ollama = False
    
    def estimate_costs(
        self,
        destination: str,
        num_days: int,
        accommodation_type: str = "mid-range"
    ) -> Dict[str, Any]:
        """
        Estimate travel costs for a trip.
        
        Args:
            destination (str): Travel destination
            num_days (int): Duration of trip
            accommodation_type (str): 'budget', 'mid-range', or 'luxury'
        
        Returns:
            Dict[str, Any]: Detailed cost breakdown
        
        Raises:
            ValueError: If inputs are invalid
        """
        
        costs = calculate_travel_cost(destination, num_days, accommodation_type)
        
        # Add analysis
        analysis = {
            "destination": destination,
            "num_days": num_days,
            "accommodation_type": accommodation_type,
            "breakdown": costs,
            "daily_breakdown": breakdown_daily_cost(destination, accommodation_type),
            "summary": self._create_cost_summary(costs),
            "recommendations": self._create_recommendations(costs, accommodation_type)
        }
        
        return analysis
    
    def validate_budget(
        self,
        destination: str,
        num_days: int,
        user_budget: float,
        accommodation_type: str = "mid-range"
    ) -> Dict[str, Any]:
        """
        Check if user's budget is sufficient for the trip.
        
        Args:
            destination (str): Travel destination
            num_days (int): Duration
            user_budget (float): User's budget in LKR
            accommodation_type (str): Accommodation level
        
        Returns:
            Dict[str, Any]: Budget validation result with recommendations
        """
        
        costs = calculate_travel_cost(destination, num_days, accommodation_type)
        validation = validate_within_budget(destination, num_days, user_budget, accommodation_type)
        
        # Create detailed analysis
        result = {
            "destination": destination,
            "num_days": num_days,
            "user_budget": user_budget,
            "estimated_cost": costs['total'],
            "within_budget": validation['within_budget'],
            "remaining_budget": validation['remaining_budget'],
            "status": validation['recommendation'],
            "cost_breakdown": costs,
            "suggestion": self._create_budget_suggestion(
                user_budget,
                costs['total'],
                destination,
                num_days,
                costs
            )
        }
        
        return result
    
    def create_budget_report(
        self,
        destination: str,
        num_days: int,
        user_budget: float,
        accommodation_type: str = "mid-range"
    ) -> str:
        """
        Create a detailed budget report.
        
        Args:
            destination (str): Travel destination
            num_days (int): Duration
            user_budget (float): User's budget
            accommodation_type (str): Accommodation level
        
        Returns:
            str: Formatted budget report
        """
        
        validation = self.validate_budget(destination, num_days, user_budget, accommodation_type)
        costs = validation['cost_breakdown']
        
        report = f"""
{'='*70}
TRAVEL BUDGET REPORT
{'='*70}

TRIP DETAILS
-----------
Destination: {destination}
Duration: {num_days} days
Budget: Rs. {user_budget:,.2f}

COST BREAKDOWN
--------------
• Accommodation:  Rs. {costs['accommodation']:>10,.2f}
• Food & Dining:  Rs. {costs['food']:>10,.2f}
• Transport:      Rs. {costs['transport']:>10,.2f}
• Activities:     Rs. {costs['activities']:>10,.2f}
                  {'─'*30}
  Subtotal:       Rs. {costs['subtotal']:>10,.2f}
  Buffer (10%):   Rs. {costs['buffer']:>10,.2f}
                  {'═'*30}
  TOTAL COST:     Rs. {costs['total']:>10,.2f}

BUDGET ANALYSIS
---------------
Estimated Cost:   Rs. {validation['estimated_cost']:,.2f}
Your Budget:      Rs. {user_budget:,.2f}
Difference:       Rs. {validation['remaining_budget']:,.2f}

Status: {'✓ WITHIN BUDGET' if validation['within_budget'] else '✗ EXCEEDS BUDGET'}

RECOMMENDATION
--------------
{validation['status']}

DAILY COST BREAKDOWN
--------------------
Daily Accommodation:  Rs. {costs['accommodation']/num_days:,.2f}
Daily Food:           Rs. {costs['food']/num_days:,.2f}
Daily Transport:      Rs. {costs['transport']/num_days:,.2f}
Daily Activities:     Rs. {costs['activities']/num_days:,.2f}
                      {'─'*30}
DAILY TOTAL:          Rs. {(costs['accommodation']+costs['food']+costs['transport']+costs['activities'])/num_days:,.2f}

MONEY-SAVING TIPS
-----------------
{chr(10).join([f'• {tip}' for tip in self._get_money_saving_tips(accommodation_type)])}

{'='*70}
"""
        
        return report
    
    def _create_cost_summary(self, costs: Dict) -> str:
        """Create a brief cost summary."""
        return (
            f"Total estimated cost: Rs. {costs['total']:,.2f} "
            f"({costs['num_days']} days)"
        )
    
    def _create_recommendations(self, costs: Dict, accommodation: str) -> List[str]:
        """Create budget recommendations."""
        recommendations = []
        
        if accommodation == "luxury":
            recommendations.append("Consider upgrading to luxury for premium experience")
        elif accommodation == "mid-range":
            recommendations.append("Mid-range offers best value for money")
        else:
            recommendations.append("Budget option - good for backpackers")
        
        recommendations.append(f"Daily cost: Rs. {(costs['accommodation']+costs['food']+costs['transport']+costs['activities'])/costs['num_days']:,.0f}")
        recommendations.append("Include 10% buffer for emergencies")
        
        return recommendations
    
    
    def _generate_llm_suggestions(
        self,
        user_budget: float,
        estimated_cost: float,
        destination: str,
        num_days: int,
        costs: Dict
    ) -> str:
        """Generate budget suggestions using Ollama LLM.
        
        Args:
            user_budget: User's budget
            estimated_cost: Estimated trip cost
            destination: Travel destination
            num_days: Trip duration
            costs: Cost breakdown
            
        Returns:
            str: LLM-generated budget suggestions
        """
        if not self.ollama_client:
            raise RuntimeError("Ollama client not initialized")
        
        prompt = f"""Generate personalized budget recommendations for a {num_days}-day trip to {destination}, Sri Lanka.

User's Budget: Rs. {user_budget:,.0f}
Estimated Cost: Rs. {estimated_cost:,.0f}
Daily Cost: Rs. {estimated_cost/num_days:,.0f}

Cost Breakdown:
- Accommodation: Rs. {costs['accommodation']:,.0f}
- Food: Rs. {costs['food']:,.0f}
- Transport: Rs. {costs['transport']:,.0f}
- Activities: Rs. {costs['activities']:,.0f}
- Buffer: Rs. {costs['buffer']:,.0f}

Provide:
1. Budget status assessment
2. Specific cost-saving recommendations
3. Alternative options if over budget
4. Ways to enhance experience if under budget"""
        
        system_prompt = (
            "You are a travel budget advisor specializing in Sri Lankan trips. "
            "Provide practical, specific recommendations for travelers to optimize their budgets. "
            "Be concise and actionable."
        )
        
        logger.info(f"Generating LLM budget suggestions for {destination}")
        suggestions = self.ollama_client.generate(
            prompt=prompt,
            system=system_prompt,
            temperature=0.6,
            max_tokens=500
        )
        
        if not suggestions or len(suggestions.strip()) < 50:
            raise ValueError("LLM returned empty or too-short response")
        
        return suggestions
    
    def _create_budget_suggestion(
        self,
        user_budget: float,
        estimated_cost: float,
        destination: str,
        num_days: int,
        costs: Dict = None
    ) -> str:
        """Create actionable budget suggestions.
        
        Uses Ollama LLM for intelligent suggestions with fallback to rules-based.
        """
        
        # Try LLM first
        if self.use_ollama and self.ollama_client and costs:
            try:
                return self._generate_llm_suggestions(
                    user_budget,
                    estimated_cost,
                    destination,
                    num_days,
                    costs
                )
            except Exception as e:
                logger.warning(f"LLM suggestion failed: {str(e)}. Using fallback.")
        
        # Fallback to rules-based suggestions
        if estimated_cost <= user_budget:
            difference = user_budget - estimated_cost
            if difference > (user_budget * 0.2):
                return (
                    f"Great! You have Rs. {difference:,.0f} left over. "
                    f"Consider luxury upgrades or extending your trip."
                )
            else:
                return (
                    f"Budget is tight with Rs. {difference:,.0f} remaining. "
                    f"Avoid unnecessary expenses."
                )
        else:
            shortfall = estimated_cost - user_budget
            reduction_needed = (shortfall / user_budget) * 100
            
            if reduction_needed < 20:
                return (
                    f"Short by Rs. {shortfall:,.0f}. "
                    f"Try budget accommodations or reduce trip to {num_days-1} days."
                )
            else:
                return (
                    f"Short by Rs. {shortfall:,.0f} ({reduction_needed:.0f}%). "
                    f"Consider reducing trip duration or changing destination."
                )
    
    def _get_money_saving_tips(self, accommodation: str) -> List[str]:
        """Get money-saving tips based on accommodation type."""
        
        tips = [
            "Eat at local restaurants instead of tourist spots",
            "Use public transport (buses, trains) instead of taxis",
            "Buy water bottles and refill from local sources",
            "Visit free attractions and hike on your own",
            "Shop at local markets instead of souvenir shops"
        ]
        
        if accommodation in ["budget", "mid-range"]:
            tips.insert(0, "Book guesthouses directly to avoid markups")
        
        return tips
    
    
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
    # Test the Budget Estimator Agent
    print("\n=== Budget Estimator Agent Tests ===\n")
    
    agent = BudgetEstimatorAgent(use_ollama=False)  # Use mock for testing
    
    # Test 1: Estimate costs
    print("Test 1: Estimate costs for 3-day Ella trip (mid-range)")
    estimate = agent.estimate_costs("Ella", 3, "mid-range")
    print(f"Total Estimated Cost: Rs. {estimate['breakdown']['total']:,.2f}")
    print(f"Daily Cost: Rs. {estimate['breakdown']['total']/3:,.2f}/day\n")
    
    # Test 2: Validate against budget
    print("Test 2: Validate against budget Rs. 20,000")
    validation = agent.validate_budget("Ella", 3, 20000, "mid-range")
    print(f"Status: {validation['status']}\n")
    
    # Test 3: Create report
    print("Test 3: Create full budget report")
    report = agent.create_budget_report("Kandy", 2, 18000, "budget")
    print(report)
