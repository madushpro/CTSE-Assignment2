"""
Comprehensive Test Suite for AI Travel Planner Tools and Agents

Tests include:
- Tool functionality (cost calculator, location data, validation, file operations)
- Agent workflows
- Integration tests
- Error handling

Author: AI Travel Planner Team
"""

import pytest
import os
import sys
import tempfile
from pathlib import Path

# Add project paths
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'tools'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'agents'))

# Import tools
from cost_calculator_tool import calculate_travel_cost, validate_within_budget
from location_data_tool import get_location_data, get_all_destinations
from validation_tool import validate_plan_structure, comprehensive_plan_validation
from file_saver_tool import save_travel_plan, append_to_log, load_travel_plan

# Import agents
from planner import TravelPlannerAgent
from researcher import LocationResearchAgent
from estimator import BudgetEstimatorAgent
from validator import PlanValidatorAgent


# ============================================================================
# COST CALCULATOR TOOL TESTS
# ============================================================================

class TestCostCalculator:
    """Test suite for cost calculator tool."""
    
    def test_calculate_cost_basic(self):
        """Test basic cost calculation."""
        costs = calculate_travel_cost("Ella", 3, "mid-range")
        assert costs["total"] > 0
        assert costs["num_days"] == 3
        assert "accommodation" in costs
        assert "food" in costs
        assert "transport" in costs
        assert "activities" in costs
    
    def test_calculate_cost_invalid_destination(self):
        """Test with invalid destination."""
        with pytest.raises(ValueError):
            calculate_travel_cost("InvalidCity", 3, "mid-range")
    
    def test_calculate_cost_invalid_days(self):
        """Test with invalid number of days."""
        with pytest.raises(ValueError):
            calculate_travel_cost("Ella", 0, "mid-range")
    
    def test_calculate_cost_invalid_type_days(self):
        """Test with invalid day type."""
        with pytest.raises(TypeError):
            calculate_travel_cost("Ella", "3", "mid-range")
    
    def test_calculate_cost_invalid_accommodation(self):
        """Test with invalid accommodation type."""
        with pytest.raises(ValueError):
            calculate_travel_cost("Ella", 3, "invalid")
    
    def test_calculate_cost_all_destinations(self):
        """Test cost calculation for all destinations."""
        destinations = ["Ella", "Kandy", "Colombo", "Galle"]
        for dest in destinations:
            costs = calculate_travel_cost(dest, 2, "mid-range")
            assert costs["total"] > 0
    
    def test_calculate_cost_all_accommodation_types(self):
        """Test cost calculation for all accommodation types."""
        for acc_type in ["budget", "mid-range", "luxury"]:
            costs = calculate_travel_cost("Ella", 2, acc_type)
            assert costs["total"] > 0
    
    def test_budget_validation_within_budget(self):
        """Test budget validation when within budget."""
        result = validate_within_budget("Ella", 3, 25000, "mid-range")
        assert result["within_budget"] == True
        assert result["remaining_budget"] > 0
    
    def test_budget_validation_exceed_budget(self):
        """Test budget validation when exceeding budget."""
        result = validate_within_budget("Colombo", 5, 10000, "mid-range")
        assert result["within_budget"] == False
        assert result["remaining_budget"] < 0
    
    def test_cost_increases_with_duration(self):
        """Test that total cost increases with trip duration."""
        cost_1_day = calculate_travel_cost("Ella", 1, "mid-range")["total"]
        cost_3_days = calculate_travel_cost("Ella", 3, "mid-range")["total"]
        assert cost_3_days > cost_1_day


# ============================================================================
# LOCATION DATA TOOL TESTS
# ============================================================================

class TestLocationDataTool:
    """Test suite for location data tool."""
    
    def test_get_location_data_valid(self):
        """Test retrieving valid location data."""
        data = get_location_data("Ella")
        assert data is not None
        assert "description" in data
        assert "attractions" in data
        assert "best_season" in data
    
    def test_get_location_data_all_destinations(self):
        """Test all destinations return valid data."""
        destinations = get_all_destinations()
        for dest in destinations:
            data = get_location_data(dest)
            assert data is not None
            assert len(data["attractions"]) > 0
    
    def test_get_location_data_invalid(self):
        """Test with invalid destination."""
        with pytest.raises(ValueError):
            get_location_data("InvalidCity")
    
    def test_get_all_destinations(self):
        """Test retrieving all destinations."""
        destinations = get_all_destinations()
        assert len(destinations) == 4
        assert "Ella" in destinations
        assert "Kandy" in destinations
    
    def test_location_data_structure(self):
        """Test complete structure of location data."""
        data = get_location_data("Kandy")
        required_keys = [
            "description", "best_season", "attractions", 
            "accommodations", "cuisines", "transport", "climate"
        ]
        for key in required_keys:
            assert key in data
    
    def test_attraction_suggestions(self):
        """Test attraction suggestions."""
        from location_data_tool import get_attraction_suggestions
        attractions = get_attraction_suggestions("Ella", 3)
        assert len(attractions) <= 3
        assert all(isinstance(a, str) for a in attractions)


# ============================================================================
# VALIDATION TOOL TESTS
# ============================================================================

class TestValidationTool:
    """Test suite for validation tool."""
    
    def test_validate_plan_structure_valid(self):
        """Test validation of valid plan structure."""
        valid_plan = """
        Day 1: Visit Ella
        - Check in at hotel
        - Hike Little Adam's Peak
        
        Day 2: Explore
        - Nine Arch Bridge
        - Ravana Falls
        
        Cost: Rs. 15,000
        """
        result = validate_plan_structure(valid_plan)
        assert result["score"] > 0
        assert isinstance(result["is_valid"], bool)
    
    def test_validate_plan_empty(self):
        """Test validation with empty plan."""
        with pytest.raises(ValueError):
            validate_plan_structure("")
    
    def test_validate_plan_too_short(self):
        """Test validation with very short plan."""
        result = validate_plan_structure("Short")
        assert result["is_valid"] == False
    
    def test_comprehensive_validation(self):
        """Test comprehensive plan validation."""
        plan = """
        Day 1: Arrive Ella - Visit Little Adam's Peak
        Day 2: Nine Arch Bridge and Ravana Falls
        Day 3: Tea plantation tour - Cost Rs. 15,000
        """
        result = comprehensive_plan_validation(plan, 3, 15000, 20000)
        assert "overall_valid" in result
        assert "final_score" in result
        assert "recommendations" in result


# ============================================================================
# FILE OPERATIONS TESTS
# ============================================================================

class TestFileOperations:
    """Test suite for file operations."""
    
    def test_save_travel_plan(self):
        """Test saving travel plan."""
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "test_plan.txt")
            test_content = "Test travel plan content"
            
            result = save_travel_plan(test_content, filepath)
            
            assert result["success"] == True
            assert os.path.exists(filepath)
    
    def test_save_plan_empty_content(self):
        """Test saving with empty content."""
        with pytest.raises(ValueError):
            save_travel_plan("", "test.txt")
    
    def test_append_to_log(self):
        """Test appending to log file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_file = os.path.join(tmpdir, "test_log.txt")
            
            result = append_to_log("Test log entry", log_file)
            assert result["success"] == True
            assert os.path.exists(log_file)
    
    def test_load_travel_plan(self):
        """Test loading travel plan."""
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "test_load.txt")
            content = "Test content to load"
            
            save_travel_plan(content, filepath)
            result = load_travel_plan(filepath)
            
            assert result["success"] == True
            assert content in result["content"]
    
    def test_load_nonexistent_file(self):
        """Test loading non-existent file."""
        result = load_travel_plan("nonexistent.txt")
        assert result["success"] == False


# ============================================================================
# AGENT TESTS
# ============================================================================

class TestAgents:
    """Test suite for agents."""
    
    def test_travel_planner_agent(self):
        """Test Travel Planner Agent."""
        agent = TravelPlannerAgent()
        result = agent.create_itinerary("Ella", 3, "mixed")
        
        assert result["days_planned"] == 3
        assert "itinerary" in result
        assert len(result["itinerary"]) > 0
    
    def test_location_research_agent(self):
        """Test Location Research Agent."""
        agent = LocationResearchAgent()
        research = agent.research_destination("Kandy")
        
        assert research["destination"] == "Kandy"
        assert "highlights" in research
        assert len(research["highlights"]) > 0
    
    def test_budget_estimator_agent(self):
        """Test Budget Estimator Agent."""
        agent = BudgetEstimatorAgent()
        estimate = agent.estimate_costs("Ella", 3, "mid-range")
        
        assert estimate["destination"] == "Ella"
        assert estimate["num_days"] == 3
        assert estimate["breakdown"]["total"] > 0
    
    def test_plan_validator_agent(self):
        """Test Plan Validator Agent."""
        agent = PlanValidatorAgent()
        plan = """
        Day 1: Arrival
        Day 2: Sightseeing
        Day 3: Adventure
        Cost: Rs. 15,000
        """
        
        result = agent.check_plan_quality(plan)
        assert "quality_score" in result
        assert "is_valid" in result


# ============================================================================
# INTEGRATION TESTS
# ============================================================================

class TestIntegration:
    """Integration tests for the complete system."""
    
    def test_end_to_end_planning(self):
        """Test end-to-end planning flow."""
        from main import TravelPlannerMAS
        
        mas = TravelPlannerMAS()
        result = mas.generate_travel_plan(
            destination="Ella",
            num_days=2,
            budget=15000
        )
        
        assert result["success"] == True
        assert result["destination"] == "Ella"
        assert result["num_days"] == 2
        assert "itinerary" in result
        assert "final_plan" in result


# ============================================================================
# PROPERTY-BASED TESTS
# ============================================================================

class TestPropertyBased:
    """Property-based tests for system stability."""
    
    @pytest.mark.parametrize("destination,days,accommodation", [
        ("Ella", 1, "budget"),
        ("Ella", 5, "luxury"),
        ("Kandy", 3, "mid-range"),
        ("Colombo", 4, "luxury"),
        ("Galle", 2, "budget"),
    ])
    def test_cost_calculation_consistency(self, destination, days, accommodation):
        """Test cost calculation is consistent across inputs."""
        costs1 = calculate_travel_cost(destination, days, accommodation)
        costs2 = calculate_travel_cost(destination, days, accommodation)
        
        assert costs1["total"] == costs2["total"]
    
    @pytest.mark.parametrize("destination", ["Ella", "Kandy", "Colombo", "Galle"])
    def test_all_destinations_have_data(self, destination):
        """Test all destinations have complete data."""
        data = get_location_data(destination)
        
        assert data is not None
        assert len(data["attractions"]) >= 3
        assert len(data["accommodations"]) >= 2
        assert len(data["cuisines"]) >= 2


# ============================================================================
# TEST EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("AI TRAVEL PLANNER - TEST SUITE")
    print("="*70 + "\n")
    
    print("Run tests with: pytest tests/test_tools.py -v")
    print("\nOr run specific test class:")
    print("  pytest tests/test_tools.py::TestCostCalculator -v")
    print("\nOr run with coverage:")
    print("  pytest tests/test_tools.py --cov=tools --cov=agents")
