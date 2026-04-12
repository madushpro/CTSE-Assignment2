"""
Location Data Tool for Travel Planning Agent

This tool provides predefined travel destination data including:
- Popular attractions
- Accommodation types
- Local cuisines
- Best time to visit
- Historical/cultural information

Author: AI Travel Planner Team
"""

from typing import Dict, List, Any


def get_location_data(destination: str) -> Dict[str, Any]:
    """
    Retrieve comprehensive travel data for a given destination.
    
    Args:
        destination (str): The destination name (e.g., 'Ella', 'Kandy', 'Colombo', 'Galle')
    
    Returns:
        Dict[str, Any]: Detailed information about the location including attractions,
                        accommodations, cuisines, season info, and cultural details
    
    Raises:
        ValueError: If destination is not found in database
    
    Example:
        >>> data = get_location_data('Ella')
        >>> print(data['attractions'])
        ['Nine Arch Bridge', 'Little Adam's Peak', 'Ravana Falls', ...]
    """
    
    # Mock Travel Database for Sri Lanka
    locations_database = {
        "Ella": {
            "description": "Hill station town located at ~1,000 meters altitude in Badulla District",
            "best_season": "December to February (cool and dry)",
            "attractions": [
                "Nine Arch Bridge (historic railway bridge with scenic views)",
                "Little Adam's Peak (hiking trail with panoramic views)",
                "Ravana Falls (waterfall with cultural legend)",
                "Ella Gap (mountain pass offering landscape views)",
                "Demodara Loop (unique railway tunnel location)",
                "Rawana Ella Resort Area (nature and gardens)"
            ],
            "accommodations": [
                "Budget Hostels (Rs. 1,500-3,000/night)",
                "Mid-range Guesthouses (Rs. 4,000-8,000/night)",
                "Luxury Resorts (Rs. 10,000-25,000/night)"
            ],
            "cuisines": ["Tea leaf curry", "Hoppers", "Kottu Roti", "Jaggery sweets"],
            "transport": "Scenic train ride available from Kandy or Haputale",
            "altitude": "1,041 meters",
            "climate": "Cool and temperate with occasional rainfall"
        },
        "Kandy": {
            "description": "Cultural capital of Sri Lanka, home to Temple of the Tooth Relic",
            "best_season": "November to February (cooler temperatures)",
            "attractions": [
                "Temple of the Tooth Relic (sacred Buddhist temple complex)",
                "Royal Botanic Garden (largest botanical garden in Asia)",
                "Kandy Lake (scenic water body in city center)",
                "Kandy National Museum (cultural and historical artifacts)",
                "Sir Arthur C. Clarke residence (historical site of famous author)",
                "Royal Palace Ruins (historical architectural remnants)",
                "Embekka Devale (historic temple with intricate woodcarvings)"
            ],
            "accommodations": [
                "Budget Hotels (Rs. 2,000-4,000/night)",
                "Mid-range Hotels (Rs. 5,000-10,000/night)",
                "Luxury Hotels (Rs. 15,000-35,000/night)"
            ],
            "cuisines": [
                "Chicken Curry",
                "Fish Curry",
                "Lamprais",
                "Weli Thalapa (traditional bread)",
                "Thambuli (vegetable salad)"
            ],
            "transport": "Well-connected by bus, train from Colombo (3-4 hours)",
            "altitude": "500 meters",
            "climate": "Tropical, warm and humid with central highlands nearby"
        },
        "Colombo": {
            "description": "Capital city and commercial hub of Sri Lanka",
            "best_season": "December to March (dry season)",
            "attractions": [
                "Galle Face Promenade (beachfront Victorian-era walkway)",
                "Old Parliament Building (historic architecture)",
                "Colombo National Museum (ancient artifacts and art)",
                "Gangaramaya Temple (Buddhist temple with museum)",
                "Mount Lavinia Beach (popular beach resort area)",
                "Colombo Port City (modern development zone)",
                "Sri Lanka Cricket Stadium (world-class sports venue)"
            ],
            "accommodations": [
                "Budget Hotels (Rs. 3,000-6,000/night)",
                "Mid-range Hotels (Rs. 8,000-15,000/night)",
                "Luxury Hotels (Rs. 20,000-50,000/night)"
            ],
            "cuisines": [
                "Lamprais (rice and meat wrapped in leaf)",
                "Devilled preparations (spicy meat dishes)",
                "Dhal curry",
                "Seafood specialties",
                "Chinese and Indian fusion"
            ],
            "transport": "International airport hub, central station for trains and buses",
            "altitude": "Sea level",
            "climate": "Tropical with monsoon rains in May-July and October-November"
        },
        "Galle": {
            "description": "Historic coastal town known for Galle Fort (UNESCO World Heritage Site)",
            "best_season": "November to April (dry and pleasant)",
            "attractions": [
                "Galle Fort (impressive 17th-century Dutch fortification)",
                "Fort Promenade (scenic pathway around fort walls)",
                "Japanese Peace Pagoda (meditation site with ocean views)",
                "Unawatuna Beach (nearby pristine beach)",
                "Hikkaduwa Beach (water sports and snorkeling location)",
                "Turtle Hatchery (marine conservation project)",
                "Local fish market (authentic cultural experience)"
            ],
            "accommodations": [
                "Budget Beachside Guesthouses (Rs. 2,500-5,000/night)",
                "Mid-range Beach Hotels (Rs. 6,000-12,000/night)",
                "Luxury Beach Resorts (Rs. 15,000-40,000/night)"
            ],
            "cuisines": [
                "Fresh-caught fish curry",
                "Crab dishes",
                "Prawn paste sambol",
                "Coconut-based curries",
                "Fresh tropical fruits"
            ],
            "transport": "Southern coastal railway, scenic train ride available",
            "altitude": "Sea level",
            "climate": "Tropical coastal climate, warm year-round"
        }
    }
    
    # Error handling for unknown destination
    if destination not in locations_database:
        available_destinations = list(locations_database.keys())
        raise ValueError(
            f"Destination '{destination}' not found. Available destinations: {available_destinations}"
        )
    
    return locations_database[destination]


def get_all_destinations() -> List[str]:
    """
    Get list of all available destinations in the database.
    
    Returns:
        List[str]: List of available destination names
    
    Example:
        >>> destinations = get_all_destinations()
        >>> print(destinations)
        ['Ella', 'Kandy', 'Colombo', 'Galle']
    """
    return ["Ella", "Kandy", "Colombo", "Galle"]


def get_attraction_suggestions(destination: str, num_suggestions: int = 3) -> List[str]:
    """
    Get top attraction suggestions for a destination.
    
    Args:
        destination (str): The destination name
        num_suggestions (int): Number of attractions to return (default: 3)
    
    Returns:
        List[str]: List of top attractions
    
    Example:
        >>> attractions = get_attraction_suggestions('Ella', 2)
        >>> print(attractions)
        ['Nine Arch Bridge', 'Little Adam\\'s Peak']
    """
    data = get_location_data(destination)
    attractions = data.get("attractions", [])
    return attractions[:min(num_suggestions, len(attractions))]


if __name__ == "__main__":
    # Test the location data tool
    test_destination = "Ella"
    try:
        location_info = get_location_data(test_destination)
        print(f"\n✓ Location Data for {test_destination}:")
        print(f"  Description: {location_info['description']}")
        print(f"  Attractions: {location_info['attractions'][:2]}")
        print(f"  Best Season: {location_info['best_season']}")
    except ValueError as e:
        print(f"✗ Error: {e}")
