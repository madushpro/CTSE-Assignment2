"""
Validation Tool for Plan Quality Assurance

This tool validates the final travel plan to ensure:
- Plan structure integrity
- Budget compliance
- Reasonable day-by-day breakdown
- Logical flow and completeness
- Safety and feasibility checks

Author: AI Travel Planner Team
"""

from typing import Dict, List, Tuple, Any
import re


def validate_plan_structure(plan: str) -> Dict[str, Any]:
    """
    Validate the overall structure and completeness of a travel plan.
    
    Args:
        plan (str): The complete travel plan text to validate
    
    Returns:
        Dict[str, Any]: Validation result with:
                       - 'is_valid': Boolean indicating overall validity
                       - 'issues': List of identified problems
                       - 'score': 0-100 quality score
                       - 'details': Detailed breakdown of checks
    
    Raises:
        ValueError: If plan is empty or None
    
    Example:
        >>> result = validate_plan_structure(travel_plan)
        >>> print(f"Valid: {result['is_valid']}, Score: {result['score']}")
        Valid: True, Score: 85
    """
    
    if not plan or not isinstance(plan, str):
        raise ValueError("Plan must be a non-empty string")
    
    issues = []
    checks_passed = 0
    total_checks = 6
    
    # Check 1: Minimum length
    MIN_LENGTH = 100
    if len(plan) < MIN_LENGTH:
        issues.append(f"Plan is too short ({len(plan)} chars, minimum {MIN_LENGTH} required)")
    else:
        checks_passed += 1
    
    # Check 2: Contains day breakdown pattern
    day_pattern = r'(?:Day|DAY)\s+\d+'
    if re.search(day_pattern, plan):
        checks_passed += 1
    else:
        issues.append("Plan doesn't contain clear day-by-day breakdown (e.g., 'Day 1', 'Day 2')")
    
    # Check 3: Contains destination mention
    destinations = ["Ella", "Kandy", "Colombo", "Galle"]
    has_destination = any(dest in plan for dest in destinations)
    if has_destination:
        checks_passed += 1
    else:
        issues.append("Plan doesn't mention any recognized destination")
    
    # Check 4: Contains accommodation mention
    accommodation_keywords = ["hotel", "guesthouse", "resort", "accommodation", "stay", "lodge"]
    has_accommodation = any(keyword in plan.lower() for keyword in accommodation_keywords)
    if has_accommodation:
        checks_passed += 1
    else:
        issues.append("Plan doesn't mention accommodation arrangements")
    
    # Check 5: Contains activities/attractions
    activity_keywords = ["visit", "explore", "hike", "tour", "see", "attraction", "temple", "beach"]
    has_activities = any(keyword in plan.lower() for keyword in activity_keywords)
    if has_activities:
        checks_passed += 1
    else:
        issues.append("Plan doesn't include specific activities or attractions")
    
    # Check 6: Contains cost information
    cost_keywords = ["cost", "budget", "price", "rs.", "rupees", "expense"]
    has_cost_info = any(keyword in plan.lower() for keyword in cost_keywords)
    if has_cost_info:
        checks_passed += 1
    else:
        issues.append("Plan doesn't contain cost information")
    
    # Calculate score
    score = (checks_passed / total_checks) * 100
    is_valid = score >= 60 and len(issues) <= 2  # Lower threshold for MVP
    
    return {
        "is_valid": is_valid,
        "issues": issues,
        "score": round(score, 2),
        "details": {
            "checks_passed": checks_passed,
            "total_checks": total_checks,
            "length": len(plan),
            "minimum_length_met": len(plan) >= MIN_LENGTH
        }
    }


def validate_budget_compliance(
    plan_text: str,
    estimated_cost: float,
    user_budget: float
) -> Dict[str, Any]:
    """
    Validate that plan costs stay within user's budget.
    
    Args:
        plan_text (str): The travel plan text
        estimated_cost (float): Calculated estimated total cost
        user_budget (float): User's stated budget limit
    
    Returns:
        Dict[str, Any]: Budget validation result with:
                       - 'within_budget': Boolean
                       - 'cost': Estimated cost
                       - 'budget': User budget
                       - 'remaining': Surplus/shortage amount
                       - 'status': 'PASS', 'WARNING', or 'FAIL'
    
    Raises:
        ValueError: If costs are negative or invalid
    """
    
    if estimated_cost < 0 or user_budget < 0:
        raise ValueError("Costs and budget must be non-negative")
    
    if user_budget == 0:
        raise ValueError("Budget cannot be zero")
    
    remaining = user_budget - estimated_cost
    within_budget = remaining >= 0
    
    # Determine status
    if within_budget:
        if remaining > (user_budget * 0.2):  # Comfortable margin
            status = "PASS"
        else:
            status = "WARNING"  # Tight budget
    else:
        status = "FAIL"
    
    return {
        "within_budget": within_budget,
        "cost": estimated_cost,
        "budget": user_budget,
        "remaining": remaining,
        "status": status,
        "buffer_percentage": (remaining / user_budget * 100) if user_budget > 0 else 0
    }


def validate_trip_duration(plan: str, expected_days: int) -> Dict[str, Any]:
    """
    Validate that plan covers the expected trip duration with all days accounted for.
    
    Args:
        plan (str): Travel plan text
        expected_days (int): Expected number of days for the trip
    
    Returns:
        Dict[str, Any]: Duration validation result with:
                       - 'is_valid': Boolean
                       - 'days_in_plan': Number of day entries found
                       - 'expected_days': Expected number
                       - 'missing_days': List of missing day numbers
    """
    
    if expected_days < 1:
        raise ValueError("Expected days must be >= 1")
    
    # Find all day patterns (Day 1, Day 2, etc.)
    day_pattern = r'Day\s+(\d+)'
    found_days = set()
    
    for match in re.finditer(day_pattern, plan, re.IGNORECASE):
        day_num = int(match.group(1))
        found_days.add(day_num)
    
    expected_days_set = set(range(1, expected_days + 1))
    missing_days = sorted(expected_days_set - found_days)
    
    is_valid = len(missing_days) == 0
    
    return {
        "is_valid": is_valid,
        "days_in_plan": len(found_days),
        "expected_days": expected_days,
        "missing_days": missing_days,
        "all_days_covered": is_valid
    }


def comprehensive_plan_validation(
    plan: str,
    num_days: int,
    estimated_cost: float,
    user_budget: float
) -> Dict[str, Any]:
    """
    Perform comprehensive validation of the entire travel plan.
    
    Args:
        plan (str): Complete travel plan
        num_days (int): Expected trip duration
        estimated_cost (float): Calculated cost
        user_budget (float): User's budget limit
    
    Returns:
        Dict[str, Any]: Comprehensive validation results including:
                       - 'overall_valid': Final validation verdict
                       - 'ready_for_delivery': Boolean indicating if plan is ready
                       - 'structure_validation': Structure check results
                       - 'budget_validation': Budget check results
                       - 'duration_validation': Duration check results
                       - 'recommendations': List of improvement suggestions
                       - 'final_score': 0-100 quality score
    
    Example:
        >>> result = comprehensive_plan_validation(plan, 3, 15000, 20000)
        >>> if result['ready_for_delivery']:
        ...     print("Plan is ready!")
    """
    
    # Run all validations
    structure_result = validate_plan_structure(plan)
    budget_result = validate_budget_compliance(plan, estimated_cost, user_budget)
    duration_result = validate_trip_duration(plan, num_days)
    
    # Determine overall status
    structure_valid = structure_result["is_valid"]
    budget_valid = budget_result["status"] in ["PASS", "WARNING"]
    duration_valid = duration_result["is_valid"]
    
    overall_valid = structure_valid and budget_valid and duration_valid
    ready_for_delivery = overall_valid
    
    # Generate recommendations
    recommendations = []
    if structure_result["score"] < 80:
        recommendations.append("Consider adding more detail to the plan")
    if budget_result["status"] == "FAIL":
        recommendations.append("Plan exceeds budget - recommend cost reduction")
    elif budget_result["status"] == "WARNING":
        recommendations.append("Budget margin is tight - add contingency buffer")
    if not duration_result["is_valid"]:
        recommendations.append(f"Missing days: {duration_result['missing_days']}")
    
    if not recommendations:
        recommendations.append("Plan meets all validation criteria - Ready to share!")
    
    # Calculate final score
    final_score = (
        structure_result["score"] * 0.4 +
        (100 if budget_valid else 0) * 0.3 +
        (100 if duration_valid else 0) * 0.3
    )
    
    return {
        "overall_valid": overall_valid,
        "ready_for_delivery": ready_for_delivery,
        "final_score": round(final_score, 2),
        "structure_validation": structure_result,
        "budget_validation": budget_result,
        "duration_validation": duration_result,
        "recommendations": recommendations,
        "summary": f"{'✓' if overall_valid else '✗'} Plan validation: {final_score:.1f}/100"
    }


if __name__ == "__main__":
    # Test the validation tool
    print("\n=== Validation Tool Tests ===\n")
    
    # Mock travel plan
    test_plan = """
    Day 1: Arrive in Ella
    Stay at mid-range hotel
    Visit Little Adam's Peak for sunset views
    
    Day 2: Explore Ella
    Hike to Nine Arch Bridge
    Relax at local café
    
    Day 3: Day trip to nearby attractions
    Visit Ravana Falls
    Return to accommodation
    
    Estimated Cost: Rs. 15,000
    Budget: Rs. 20,000
    """
    
    try:
        print("Test 1: Structure Validation")
        result = validate_plan_structure(test_plan)
        print(f"  Valid: {result['is_valid']}, Score: {result['score']}/100")
        if result['issues']:
            print(f"  Issues: {result['issues']}\n")
        
        print("Test 2: Comprehensive Validation")
        full_result = comprehensive_plan_validation(test_plan, 3, 15000, 20000)
        print(f"  Overall Valid: {full_result['overall_valid']}")
        print(f"  Ready for Delivery: {full_result['ready_for_delivery']}")
        print(f"  Final Score: {full_result['final_score']}/100")
        print(f"  Recommendations:")
        for rec in full_result['recommendations']:
            print(f"    - {rec}")
            
    except ValueError as e:
        print(f"✗ Error: {e}")
