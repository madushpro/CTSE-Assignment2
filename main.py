"""
Main Integration for AI Travel Planner Multi-Agent System

This module orchestrates all agents and manages the complete workflow:
1. User Input Collection
2. Travel Planning by Planner Agent
3. Location Research by Researcher Agent
4. Cost Estimation by Estimator Agent
5. Plan Validation by Validator Agent
6. Output Generation and Saving
7. Logging and Observability

Author: AI Travel Planner Team
"""

import sys
import os
from datetime import datetime
from typing import Dict, Any

# Add paths for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'agents'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'tools'))

# Import agents
from planner import TravelPlannerAgent
from researcher import LocationResearchAgent
from estimator import BudgetEstimatorAgent
from validator import PlanValidatorAgent

# Import tools
from location_data_tool import get_location_data
from cost_calculator_tool import calculate_travel_cost
from file_saver_tool import save_travel_plan, append_to_log, get_log_contents, clear_log


class TravelPlannerMAS:
    """Main Multi-Agent System orchestrator for travel planning with Ollama LLM support."""
    
    def __init__(self, log_file: str = "logs/log.txt", use_ollama: bool = True):
        """
        Initialize the Travel Planner MAS.
        
        Args:
            log_file (str): Path to log file for observability
            use_ollama (bool): Whether to use Ollama LLM (default: True)
        """
        self.log_file = log_file
        self.use_ollama = use_ollama
        
        # Initialize agents with Ollama support
        self.planner = TravelPlannerAgent(use_ollama=use_ollama)
        self.researcher = LocationResearchAgent(use_ollama=use_ollama)
        self.estimator = BudgetEstimatorAgent(use_ollama=use_ollama)
        self.validator = PlanValidatorAgent(use_ollama=use_ollama)
        
        # Initialize logging
        clear_log(log_file)
        self._log("AI Travel Planner MAS initialized")
        if use_ollama:
            self._log("✓ Ollama LLM support ENABLED")
    
    def generate_travel_plan(
        self,
        destination: str,
        num_days: int,
        budget: float
    ) -> Dict[str, Any]:
        """
        Main orchestration method - generates complete travel plan.
        
        Args:
            destination (str): Travel destination (Ella, Kandy, Colombo, Galle)
            num_days (int): Number of days for trip
            budget (float): User's budget in LKR
        
        Returns:
            Dict[str, Any]: Complete travel plan with all components
        
        Raises:
            ValueError: If inputs are invalid
        """
        
        # Input validation
        self._log(f"User Input: Destination={destination}, Days={num_days}, Budget=Rs.{budget}")
        
        if destination not in ["Ella", "Kandy", "Colombo", "Galle"]:
            raise ValueError(f"Invalid destination: {destination}")
        if num_days < 1:
            raise ValueError("Number of days must be at least 1")
        if budget < 1000:
            raise ValueError("Budget too low for travel planning")
        
        self._log("Input validation: PASSED")
        
        try:
            # STEP 1: Travel Planner Agent - Create itinerary
            self._log(f"[AGENT 1] Travel Planner: Creating {num_days}-day itinerary for {destination}")
            planner_result = self.planner.create_itinerary(
                destination=destination,
                num_days=num_days,
                preferences="mixed"
            )
            itinerary = planner_result['itinerary']
            self._log(f"[AGENT 1] Travel Planner: Itinerary created successfully ({len(itinerary)} chars)")
            
            # STEP 2: Location Research Agent - Enhance with research
            self._log(f"[AGENT 2] Location Research: Researching {destination}")
            enhanced_itinerary = self.researcher.enhance_itinerary(itinerary, destination)
            self._log(f"[AGENT 2] Location Research: Plan enhanced with cultural insights")
            
            # STEP 3: Budget Estimator Agent - Calculate costs
            self._log(f"[AGENT 3] Budget Estimator: Calculating costs for {num_days} days")
            cost_analysis = self.estimator.estimate_costs(
                destination=destination,
                num_days=num_days,
                accommodation_type="mid-range"
            )
            estimated_cost = cost_analysis['breakdown']['total']
            self._log(f"[AGENT 3] Budget Estimator: Estimated cost Rs. {estimated_cost:,.2f}")
            
            # Add cost information to plan
            plan_with_costs = enhanced_itinerary + f"\n\n{'='*70}\nBUDGET SUMMARY\n{'='*70}\n"
            plan_with_costs += self.estimator.create_budget_report(
                destination, num_days, budget, "mid-range"
            )
            
            # STEP 4: Plan Validator Agent - Validate entire plan
            self._log(f"[AGENT 4] Plan Validator: Validating complete plan")
            validation_result = self.validator.validate_complete_plan(
                plan_with_costs,
                num_days,
                estimated_cost,
                budget
            )
            self._log(f"[AGENT 4] Plan Validator: Validation complete. Score: {validation_result['quality_score']:.1f}/100")
            
            # STEP 5: Final assembly and output
            final_plan = self._assemble_final_plan(
                destination,
                num_days,
                budget,
                itinerary,
                enhanced_itinerary,
                cost_analysis,
                validation_result
            )
            
            self._log("✓ Travel plan generation COMPLETE")
            
            return {
                "success": True,
                "destination": destination,
                "num_days": num_days,
                "budget": budget,
                "estimated_cost": estimated_cost,
                "itinerary": itinerary,
                "enhanced_plan": enhanced_itinerary,
                "cost_analysis": cost_analysis,
                "validation": validation_result,
                "final_plan": final_plan,
                "overall_status": "✓ APPROVED" if validation_result['ready_for_delivery'] else "⚠ REVIEW NEEDED"
            }
        
        except Exception as e:
            error_msg = f"Error in plan generation: {str(e)}"
            self._log(f"✗ {error_msg}")
            raise ValueError(error_msg)
    
    def _assemble_final_plan(
        self,
        destination: str,
        num_days: int,
        budget: float,
        itinerary: str,
        enhanced_itinerary: str,
        cost_analysis: Dict,
        validation: Dict
    ) -> str:
        """Assemble the final comprehensive travel plan."""
        
        final = f"""
{'='*70}
FINAL TRAVEL PLAN REPORT
{'='*70}

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

TRIP SUMMARY
-----------
Destination: {destination}
Duration: {num_days} days
Budget: Rs. {budget:,.2f}
Estimated Cost: Rs. {cost_analysis['breakdown']['total']:,.2f}
Status: {validation['overall_valid'] and '✓ APPROVED' or '⚠ NEEDS REVIEW'}
Quality Score: {validation['quality_score']:.1f}/100

{'='*70}
DETAILED ITINERARY
{'='*70}

{enhanced_itinerary}

{'='*70}
COST BREAKDOWN
{'='*70}

{self.estimator.create_budget_report(destination, num_days, budget, 'mid-range')}

{'='*70}
QUALITY ASSURANCE REPORT
{'='*70}

{self.validator.generate_validation_report(enhanced_itinerary, num_days, cost_analysis['breakdown']['total'], budget)}

VALIDATION NOTES
{validation.get('validator_notes', '')}

{'='*70}
Ready for Delivery: {validation['ready_for_delivery'] and 'YES ✓' or 'NO - Review Required'}
{'='*70}
"""
        
        return final
    
    def save_plan(self, plan_content: str, filename: str = "output.txt") -> Dict[str, Any]:
        """
        Save the final plan to a file.
        
        Args:
            plan_content (str): The plan to save
            filename (str): Output filename
        
        Returns:
            Dict[str, Any]: Save result
        """
        result = save_travel_plan(plan_content, filename)
        self._log(f"Plan saved to {result['filepath']}")
        return result
    
    def _log(self, message: str) -> None:
        """Log a message with timestamp."""
        try:
            append_to_log(message, self.log_file)
        except Exception as e:
            print(f"Logging error: {e}")
    
    def get_logs(self) -> str:
        """Get all logged messages."""
        return get_log_contents(self.log_file)
    
    def get_agent_info(self) -> Dict[str, Dict]:
        """Get information about all agents."""
        return {
            "Planner": self.planner.get_agent_info(),
            "Researcher": self.researcher.get_agent_info(),
            "Estimator": self.estimator.get_agent_info(),
            "Validator": self.validator.get_agent_info()
        }


def main():
    """
    Example usage of the Travel Planner MAS.
    """
    
    print("\n" + "="*70)
    print("AI TRAVEL PLANNER - MULTI-AGENT SYSTEM")
    print("="*70 + "\n")
    
    # Initialize MAS
    mas = TravelPlannerMAS()
    
    # Example: Generate plan for Ella
    print("Generating travel plan for Ella (3 days, Budget: Rs. 20,000)...\n")
    
    try:
        result = mas.generate_travel_plan(
            destination="Ella",
            num_days=3,
            budget=20000
        )
        
        if result['success']:
            print(f"✓ Plan generated successfully!")
            print(f"Status: {result['overall_status']}")
            print(f"Estimated Cost: Rs. {result['estimated_cost']:,.2f}")
            print(f"Quality Score: {result['validation']['quality_score']:.1f}/100\n")
            
            # Save plan
            save_result = mas.save_plan(result['final_plan'])
            print(f"✓ Plan saved to {save_result['filepath']}\n")
            
            # Show logs
            print("="*70)
            print("EXECUTION LOGS")
            print("="*70)
            print(mas.get_logs())
        else:
            print("✗ Plan generation failed")
    
    except Exception as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    main()
