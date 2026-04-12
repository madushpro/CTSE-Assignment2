"""
Cost Calculator Tool for Budget Estimation

This tool calculates estimated costs for travel including:
- Accommodation costs
- Food and dining
- Local transportation
- Activities and attractions
- Emergency buffer

Author: AI Travel Planner Team
"""

from typing import Dict, Tuple
from dataclasses import dataclass


@dataclass
class CostBreakdown:
    """Data class for cost breakdown structure"""
    accommodation: float
    food: float
    transport: float
    activities: float
    buffer: float
    total: float


def calculate_travel_cost(
    destination: str,
    num_days: int,
    accommodation_type: str = "mid-range"
) -> Dict[str, float]:
    """
    Calculate estimated travel cost for a destination.
    
    Args:
        destination (str): Travel destination name (Ella, Kandy, Colombo, Galle)
        num_days (int): Number of days for the trip (must be >= 1)
        accommodation_type (str): Budget level - 'budget', 'mid-range', or 'luxury'
    
    Returns:
        Dict[str, float]: Breakdown of costs including:
                         - accommodation: Daily room cost
                         - food: Daily meal costs
                         - transport: Local transportation
                         - activities: Attractions and tours
                         - buffer: Emergency contingency (10%)
                         - total: Total estimated cost
    
    Raises:
        ValueError: If destination invalid, days < 1, or accommodation type invalid
        TypeError: If num_days is not an integer
    
    Example:
        >>> costs = calculate_travel_cost('Ella', 3, 'budget')
        >>> print(f"Total: Rs. {costs['total']}")
        Total: Rs. 13650.0
    """
    
    # Input validation
    if not isinstance(num_days, int):
        raise TypeError(f"num_days must be an integer, got {type(num_days)}")
    
    if num_days < 1:
        raise ValueError(f"num_days must be >= 1, got {num_days}")
    
    valid_accommodations = ["budget", "mid-range", "luxury"]
    if accommodation_type.lower() not in valid_accommodations:
        raise ValueError(
            f"accommodation_type must be one of {valid_accommodations}, got '{accommodation_type}'"
        )
    
    # Cost database based on destination and accommodation type (in LKR - Sri Lankan Rupees)
    cost_matrix = {
        "Ella": {
            "budget": {"accommodation": 2000, "food": 1200, "transport": 800, "activities": 500},
            "mid-range": {"accommodation": 5000, "food": 2000, "transport": 1200, "activities": 1000},
            "luxury": {"accommodation": 15000, "food": 5000, "transport": 2000, "activities": 3000}
        },
        "Kandy": {
            "budget": {"accommodation": 2500, "food": 1000, "transport": 700, "activities": 600},
            "mid-range": {"accommodation": 6000, "food": 2000, "transport": 1000, "activities": 1200},
            "luxury": {"accommodation": 20000, "food": 4000, "transport": 1500, "activities": 2500}
        },
        "Colombo": {
            "budget": {"accommodation": 3000, "food": 1500, "transport": 1000, "activities": 800},
            "mid-range": {"accommodation": 8000, "food": 2500, "transport": 1500, "activities": 1500},
            "luxury": {"accommodation": 25000, "food": 6000, "transport": 2500, "activities": 4000}
        },
        "Galle": {
            "budget": {"accommodation": 2500, "food": 1300, "transport": 900, "activities": 700},
            "mid-range": {"accommodation": 7000, "food": 2200, "transport": 1200, "activities": 1300},
            "luxury": {"accommodation": 18000, "food": 4500, "transport": 2000, "activities": 3500}
        }
    }
    
    # Validate destination
    if destination not in cost_matrix:
        raise ValueError(
            f"Unknown destination '{destination}'. Valid options: {list(cost_matrix.keys())}"
        )
    
    # Get daily costs for destination and accommodation type
    daily_costs = cost_matrix[destination][accommodation_type.lower()]
    
    # Calculate totals
    accommodation_total = daily_costs["accommodation"] * num_days
    food_total = daily_costs["food"] * num_days
    transport_total = daily_costs["transport"] * num_days  # One-time local transport pass
    activities_total = daily_costs["activities"] * num_days
    
    subtotal = accommodation_total + food_total + transport_total + activities_total
    buffer = subtotal * 0.10  # 10% emergency buffer
    total = subtotal + buffer
    
    return {
        "accommodation": accommodation_total,
        "food": food_total,
        "transport": transport_total,
        "activities": activities_total,
        "subtotal": subtotal,
        "buffer": buffer,
        "total": total,
        "currency": "LKR",
        "num_days": num_days
    }


def breakdown_daily_cost(destination: str, accommodation_type: str = "mid-range") -> Dict[str, float]:
    """
    Get the daily cost breakdown for a destination (per day).
    
    Args:
        destination (str): Travel destination name
        accommodation_type (str): Budget level - 'budget', 'mid-range', or 'luxury'
    
    Returns:
        Dict[str, float]: Daily costs for each category
    
    Example:
        >>> daily = breakdown_daily_cost('Ella', 'budget')
        >>> print(f"Daily food cost: Rs. {daily['food']}")
        Daily food cost: Rs. 1200
    """
    daily_cost = calculate_travel_cost(destination, 1, accommodation_type)
    return {
        key: value for key, value in daily_cost.items() 
        if key not in ["subtotal", "buffer", "total", "currency", "num_days"]
    }


def validate_within_budget(
    destination: str,
    num_days: int,
    budget: float,
    accommodation_type: str = "mid-range"
) -> Dict[str, any]:
    """
    Check if estimated cost fits within user's budget.
    
    Args:
        destination (str): Travel destination
        num_days (int): Duration of trip
        budget (float): User's budget in LKR
        accommodation_type (str): Budget level for accommodation
    
    Returns:
        Dict[str, any]: Dictionary with:
                       - 'within_budget': Boolean indicating if cost fits
                       - 'estimated_cost': Calculated total cost
                       - 'remaining_budget': Difference (positive = surplus, negative = shortage)
                       - 'recommendation': Text recommendation
    
    Example:
        >>> result = validate_within_budget('Ella', 3, 20000, 'budget')
        >>> print(result['within_budget'])
        True
    """
    costs = calculate_travel_cost(destination, num_days, accommodation_type)
    estimated = costs["total"]
    remaining = budget - estimated
    within_budget = remaining >= 0
    
    if within_budget:
        recommendation = f"Budget is sufficient. You have Rs. {remaining:.2f} remaining."
    else:
        recommendation = (
            f"Budget is insufficient by Rs. {abs(remaining):.2f}. "
            f"Consider reducing days or choosing budget accommodation."
        )
    
    return {
        "within_budget": within_budget,
        "estimated_cost": estimated,
        "user_budget": budget,
        "remaining_budget": remaining,
        "recommendation": recommendation
    }


if __name__ == "__main__":
    # Test the cost calculator tool
    print("\n=== Cost Calculator Tool Tests ===\n")
    
    try:
        # Test 1: Basic cost calculation
        print("Test 1: Calculate cost for Ella (3 days, mid-range)")
        costs = calculate_travel_cost("Ella", 3, "mid-range")
        print(f"  Accommodation: Rs. {costs['accommodation']:.2f}")
        print(f"  Food: Rs. {costs['food']:.2f}")
        print(f"  Transport: Rs. {costs['transport']:.2f}")
        print(f"  Activities: Rs. {costs['activities']:.2f}")
        print(f"  Buffer (10%): Rs. {costs['buffer']:.2f}")
        print(f"  TOTAL: Rs. {costs['total']:.2f}\n")
        
        # Test 2: Budget validation
        print("Test 2: Validate against budget Rs. 20,000")
        validation = validate_within_budget("Ella", 3, 20000, "mid-range")
        print(f"  Within Budget: {validation['within_budget']}")
        print(f"  Recommendation: {validation['recommendation']}\n")
        
        # Test 3: Different accommodation types
        print("Test 3: Compare accommodation types for Kandy")
        for acc_type in ["budget", "mid-range", "luxury"]:
            costs = calculate_travel_cost("Kandy", 2, acc_type)
            print(f"  {acc_type.upper()}: Rs. {costs['total']:.2f}")
            
    except (ValueError, TypeError) as e:
        print(f"✗ Error during testing: {e}")
