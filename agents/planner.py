"""
Travel Planner Agent - STUDENT 1 CONTRIBUTION

Role: Creates day-by-day travel itinerary structure
Goal: Break down trip into organized, logical daily activities
Backstory: Expert itinerary curator with deep knowledge of travel planning

STUDENT 1: Responsible for this agent
- Designs itinerary generation using LLM reasoning
- Implements prompt engineering for travel planning
- Handles fallback to mock data if LLM unavailable
"""

from typing import Dict, Any, Optional
import logging

# Try to import Ollama client, fall back gracefully if not available
try:
    from ollama_client import create_ollama_client, OllamaClient
    OLLAMA_AVAILABLE = True
except ImportError:
    OLLAMA_AVAILABLE = False

logger = logging.getLogger(__name__)


class TravelPlannerAgent:
    """
    Agent responsible for creating structured travel itineraries.
    
    Uses Ollama LLM (llama3:8b) for intelligent planning with fallback
    to mock data if LLM is unavailable.
    """
    
    def __init__(self, use_ollama: bool = True):
        """
        Initialize Travel Planner Agent.
        
        Args:
            use_ollama (bool): Whether to attempt LLM usage (default: True)
        """
        self.role = "Travel Itinerary Curator"
        self.goal = "Create a structured, engaging day-by-day travel itinerary"
        self.backstory = (
            "You are an experienced travel planner with 10+ years of expertise in "
            "designing memorable itineraries. You understand travel pacing, local culture, "
            "and how to balance adventure with relaxation. You create logical day-by-day "
            "breakdowns that maximize experiences while respecting rest day needs."
        )
        self.tools_used = ["destination_context", "trip_duration", "accommodation_planning"]
        
        # Initialize Ollama client if available
        self.ollama_client: Optional[OllamaClient] = None
        self.use_ollama = use_ollama and OLLAMA_AVAILABLE
        
        if self.use_ollama:
            try:
                self.ollama_client = create_ollama_client()
                logger.info("✓ Ollama LLM initialized for Travel Planner Agent")
            except Exception as e:
                logger.warning(f"Could not initialize Ollama: {str(e)}. Using mock data.")
                self.use_ollama = False
    
    def create_itinerary(
        self,
        destination: str,
        num_days: int,
        preferences: str = "mixed"
    ) -> Dict[str, Any]:
        """
        Create a day-by-day travel itinerary.
        
        Uses Ollama LLM (llama3:8b) for intelligent planning if available,
        falls back to structured mock data otherwise.
        
        Args:
            destination (str): Travel destination (Ella, Kandy, Colombo, Galle)
            num_days (int): Number of days for the trip (1-10)
            preferences (str): Activity preferences (adventure, cultural, relaxation, mixed)
        
        Returns:
            Dict[str, Any]: Dictionary containing:
                - 'itinerary': Day-by-day plan as formatted string
                - 'days_planned': Number of days in itinerary
                - 'structure': Structure type used (LLM or Mock)
                - 'destination': Destination name
                - 'preferences': User preferences
                - 'source': "Ollama LLM" or "Mock Data"
        
        Raises:
            ValueError: If inputs are invalid
            requests.RequestException: If Ollama call fails unexpectedly
        """
        
        # Validate inputs
        if not isinstance(num_days, int) or num_days < 1 or num_days > 10:
            raise ValueError("Number of days must be an integer between 1 and 10")
        
        valid_destinations = ["Ella", "Kandy", "Colombo", "Galle"]
        if destination not in valid_destinations:
            raise ValueError(f"Destination must be one of: {', '.join(valid_destinations)}")
        
        # Try LLM first, fall back to mock data
        if self.use_ollama and self.ollama_client:
            try:
                itinerary = self._create_llm_itinerary(destination, num_days, preferences)
                source = "Ollama LLM (llama3:8b)"
            except Exception as e:
                logger.warning(f"LLM generation failed: {str(e)}. Falling back to mock data.")
                itinerary = self._create_mock_itinerary(destination, num_days, preferences)
                source = "Mock Data (Fallback)"
        else:
            itinerary = self._create_mock_itinerary(destination, num_days, preferences)
            source = "Mock Data"
        
        return {
            "itinerary": itinerary,
            "days_planned": num_days,
            "structure": "Day-by-day breakdown",
            "destination": destination,
            "preferences": preferences,
            "source": source
        }
    
    def _create_llm_itinerary(
        self,
        destination: str,
        num_days: int,
        preferences: str
    ) -> str:
        """
        Generate itinerary using Ollama LLM.
        
        Args:
            destination: Travel destination
            num_days: Number of days
            preferences: Activity preference type
        
        Returns:
            str: LLM-generated itinerary
            
        Raises:
            requests.RequestException: If LLM call fails
        """
        if not self.ollama_client:
            raise RuntimeError("Ollama client not initialized")
        
        prompt = f"""Create a detailed {num_days}-day travel itinerary for {destination}, Sri Lanka.

Preferences: {preferences}

Requirements:
- Break into specific daily activities
- Include morning, afternoon, and evening activities
- Mention specific attractions, restaurants, and experiences
- Consider realistic travel times between locations
- Balance activity intensity appropriately

Format as a clear, structured itinerary with day numbers and times."""

        system_prompt = (
            "You are an expert travel planner specializing in Sri Lankan destinations. "
            "Create detailed, practical, and engaging travel itineraries. "
            "Always format responses as clear daily plans with specific times and activities."
        )
        
        logger.info(f"Generating {num_days}-day itinerary for {destination} via Ollama LLM")
        
        itinerary = self.ollama_client.generate(
            prompt=prompt,
            system=system_prompt,
            temperature=0.7,
            max_tokens=800
        )
        
        # Ensure output is well-formatted
        if not itinerary or len(itinerary.strip()) < 50:
            raise ValueError("LLM returned empty or too-short response")
        
        return itinerary
    
    def _create_mock_itinerary(
        self,
        destination: str,
        num_days: int,
        preferences: str
    ) -> str:
        """
        Create itinerary using structured mock data (fallback).
        
        Args:
            destination: Travel destination
            num_days: Number of days
            preferences: Activity preferences
        
        Returns:
            str: Formatted itinerary string
        """
        
        itineraries = {
            "Ella": self._create_ella_itinerary(num_days, preferences),
            "Kandy": self._create_kandy_itinerary(num_days, preferences),
            "Colombo": self._create_colombo_itinerary(num_days, preferences),
            "Galle": self._create_galle_itinerary(num_days, preferences)
        }
        
        return itineraries.get(destination, "")
    
    def _create_ella_itinerary(self, num_days: int, preferences: str) -> str:
        """Create Ella itinerary."""
        
        base = "ELLA TRAVEL ITINERARY\n" + "="*50 + "\n\n"
        
        if num_days == 1:
            base += (
                "Day 1: Quick Ella Experience\n"
                "- 08:00 AM: Arrive in Ella by train (scenic mountain railway)\n"
                "- 11:00 AM: Check into accommodation\n"
                "- 02:00 PM: Quick hike to Little Adam's Peak (30 minutes)\n"
                "- 04:30 PM: Sunset views and rest\n"
                "- 06:30 PM: Local dinner at café\n"
                "- 08:00 PM: Rest in cozy guesthouse\n\n"
            )
        elif num_days == 2:
            base += (
                "Day 1: Arrival and Little Peak\n"
                "- 08:00 AM: Arrive in Ella via scenic train\n"
                "- 02:00 PM: Settle into accommodation and relax\n"
                "- 04:00 PM: Hike to Little Adam's Peak\n"
                "- 06:00 PM: Explore local market and traditional cuisine\n\n"
                "Day 2: Nine Arch Bridge and Waterfalls\n"
                "- 06:00 AM: Early hike to Nine Arch Bridge (photography)\n"
                "- 09:00 AM: Breakfast at local café with mountain views\n"
                "- 01:00 PM: Trek to Ravana Falls (20 min)\n"
                "- 04:00 PM: Rest and shopping\n"
                "- 07:00 PM: Dinner and evening walk\n\n"
            )
        elif num_days >= 3:
            base += (
                "Day 1: Arrival and Orientation\n"
                "- 08:00 AM: Arrive in Ella via train\n"
                "- 02:00 PM: Check in and explore town\n"
                "- 05:00 PM: Tea plantation walk\n"
                "- 07:00 PM: Local dinner and rest\n\n"
                "Day 2: Mountain Hiking Adventure\n"
                "- 06:00 AM: Sunrise hike to Little Adam's Peak\n"
                "- 09:00 AM: Visit Nine Arch Bridge\n"
                "- 12:00 PM: Local lunch\n"
                "- 02:00 PM: Rest and activities\n"
                "- 05:00 PM: Traditional curry dinner\n\n"
                "Day 3: Waterfalls and Relaxation\n"
                "- 08:00 AM: Trek to Ravana Falls\n"
                "- 11:00 AM: Visit Demodara Loop (unique railway tunnel)\n"
                "- 02:00 PM: Lunch and free time\n"
                "- 04:00 PM: Final activities or shopping\n"
                "- 07:00 PM: Relaxation and packing\n\n"
            )
        
        return base
    
    def _create_kandy_itinerary(self, num_days: int, preferences: str) -> str:
        """Create Kandy itinerary."""
        
        base = "KANDY TRAVEL ITINERARY\n" + "="*50 + "\n\n"
        
        if num_days == 1:
            base += (
                "Day 1: Cultural Kandy\n"
                "- 09:00 AM: Visit Temple of the Tooth Relic\n"
                "- 02:00 PM: Kandy Lake walk and lunch\n"
                "- 05:00 PM: Local market exploration\n"
                "- 07:30 PM: Cultural show and traditional dinner\n\n"
            )
        elif num_days == 2:
            base += (
                "Day 1: Sacred Kandy\n"
                "- 09:00 AM: Temple of the Tooth Relic (UNESCO World Heritage)\n"
                "- 12:00 PM: Kandy National Museum\n"
                "- 02:00 PM: Lake walk and local lunch\n"
                "- 05:00 PM: Explore local shops\n"
                "- 07:00 PM: Cultural performance\n\n"
                "Day 2: Nature and Gardens\n"
                "- 08:00 AM: Royal Botanic Garden (largest in Asia)\n"
                "- 12:00 PM: Garden lunch and exploration\n"
                "- 02:00 PM: Rest at hotel\n"
                "- 04:00 PM: Last-minute shopping\n"
                "- 07:00 PM: Farewell dinner\n\n"
            )
        elif num_days >= 3:
            base += (
                "Day 1: Arrival and Temple Visit\n"
                "- 09:00 AM: Reach Kandy\n"
                "- 10:00 AM: Temple of the Tooth Relic tour\n"
                "- 01:00 PM: Local lunch\n"
                "- 03:00 PM: Kandy Lake evening walk\n"
                "- 07:00 PM: Dinner and rest\n\n"
                "Day 2: Cultural Immersion\n"
                "- 08:00 AM: Royal Botanic Garden\n"
                "- 12:00 PM: Garden cafeteria lunch\n"
                "- 02:00 PM: Kandy National Museum\n"
                "- 05:00 PM: Local market\n"
                "- 07:30 PM: Cultural dance performance and dinner\n\n"
                "Day 3: Adventure Options\n"
                "- 08:00 AM: Elephant sanctuary or hiking options\n"
                "- 01:00 PM: Lunch at local restaurant\n"
                "- 02:30 PM: Local market exploration\n"
                "- 05:00 PM: Relaxation time\n"
                "- 07:00 PM: Traditional Sri Lankan dinner\n\n"
            )
        
        return base
    
    def _create_colombo_itinerary(self, num_days: int, preferences: str) -> str:
        """Create Colombo itinerary."""
        
        base = "COLOMBO TRAVEL ITINERARY\n" + "="*50 + "\n\n"
        
        if num_days == 1:
            base += (
                "Day 1: Metropolitan Colombo\n"
                "- 09:00 AM: Galle Face Promenade walk\n"
                "- 11:30 AM: Colombo National Museum\n"
                "- 02:00 PM: Local lunch\n"
                "- 04:00 PM: Shopping at local markets\n"
                "- 06:30 PM: Beach dinner at Mount Lavinia\n\n"
            )
        elif num_days == 2:
            base += (
                "Day 1: Colonial and Modern Colombo\n"
                "- 09:00 AM: Galle Face Promenade (historic waterfront)\n"
                "- 11:00 AM: Old Parliament Building tour\n"
                "- 01:00 PM: Local lunch\n"
                "- 03:00 PM: Museum visit\n"
                "- 06:00 PM: Mount Lavinia sunset\n"
                "- 07:30 PM: Beachfront dinner\n\n"
                "Day 2: Cultural Colombo\n"
                "- 09:00 AM: Gangaramaya Temple visit\n"
                "- 11:00 AM: Shopping and local exploration\n"
                "- 02:00 PM: Lunch\n"
                "- 03:00 PM: Mount Lavinia beach experience\n"
                "- 06:00 PM: Sunset walk\n"
                "- 07:30 PM: Modern Colombo nightlife\n\n"
            )
        elif num_days >= 3:
            base += (
                "Day 1: Arrival and Waterfront\n"
                "- 09:00 AM: Arrival and settlement\n"
                "- 11:00 AM: Galle Face Promenade\n"
                "- 01:00 PM: Lunch\n"
                "- 02:00 PM: Beach exploration\n"
                "- 06:30 PM: Dinner and rest\n\n"
                "Day 2: Museums and Culture\n"
                "- 09:00 AM: Colombo National Museum\n"
                "- 12:00 PM: Gangaramaya Temple\n"
                "- 02:00 PM: Lunch\n"
                "- 03:00 PM: Local market exploration\n"
                "- 06:00 PM: Sunset at Marina\n"
                "- 07:30 PM: Dinner\n\n"
                "Day 3: Beach and Relaxation\n"
                "- 09:00 AM: Mount Lavinia beach time\n"
                "- 12:00 PM: Beachside lunch\n"
                "- 02:00 PM: Water sports or spa options\n"
                "- 04:00 PM: Shopping\n"
                "- 06:30 PM: Final dinner\n\n"
            )
        
        return base
    
    def _create_galle_itinerary(self, num_days: int, preferences: str) -> str:
        """Create Galle itinerary."""
        
        base = "GALLE TRAVEL ITINERARY\n" + "="*50 + "\n\n"
        
        if num_days == 1:
            base += (
                "Day 1: Historic Galle Fort\n"
                "- 09:00 AM: Galle Fort exploration (UNESCO site)\n"
                "- 12:00 PM: Local lunch\n"
                "- 02:00 PM: Fort Promenade walk\n"
                "- 05:00 PM: Shopping and cafés\n"
                "- 06:30 PM: Sunset beach experience\n\n"
            )
        elif num_days == 2:
            base += (
                "Day 1: Fort and Beach\n"
                "- 09:00 AM: Galle Fort tour (intricate architecture)\n"
                "- 12:00 PM: Local lunch\n"
                "- 02:00 PM: Fort shopping and exploration\n"
                "- 05:00 PM: Sunset walk\n"
                "- 07:00 PM: Beachfront dinner\n\n"
                "Day 2: Water Activities\n"
                "- 09:00 AM: Snorkeling or boat tour\n"
                "- 12:00 PM: Lunch\n"
                "- 02:00 PM: Unawatuna Beach relaxation\n"
                "- 05:00 PM: Beach walk\n"
                "- 07:00 PM: Final dinner\n\n"
            )
        elif num_days >= 3:
            base += (
                "Day 1: Galle Fort Discovery\n"
                "- 09:00 AM: Detailed Galle Fort tour (UNESCO World Heritage)\n"
                "- 12:00 PM: Local lunch\n"
                "- 02:00 PM: Fort promenade and shops\n"
                "- 05:00 PM: Sunset walk\n"
                "- 07:00 PM: Beachfront dinner\n\n"
                "Day 2: Beaches and Relaxation\n"
                "- 09:00 AM: Unawatuna Beach swim\n"
                "- 12:00 PM: Beachside lunch\n"
                "- 02:00 PM: Water sports or spa\n"
                "- 05:00 PM: Local village exploration\n"
                "- 07:00 PM: Dinner\n\n"
                "Day 3: Marine Adventures\n"
                "- 09:00 AM: Snorkeling or whale watching tour\n"
                "- 01:00 PM: Lunch\n"
                "- 02:00 PM: Turtle hatchery visit\n"
                "- 04:00 PM: Beach relaxation\n"
                "- 06:30 PM: Final evening on the beach\n\n"
            )
        
        return base
    
    def get_agent_info(self) -> Dict[str, str]:
        """
        Get agent role information.
        
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
    # Test the Travel Planner Agent
    print("\n=== Travel Planner Agent Tests ===\n")
    
    agent = TravelPlannerAgent(use_ollama=False)  # Use mock for testing
    
    # Test 1: Ella 3-day
    print("Test 1: Create 3-day Ella itinerary")
    result = agent.create_itinerary("Ella", 3, "adventure")
    print(f"Source: {result['source']}")
    print(result['itinerary'])
    
    # Test 2: Kandy 2-day
    print("\nTest 2: Create 2-day Kandy itinerary")
    result = agent.create_itinerary("Kandy", 2, "cultural")
    print(f"Source: {result['source']}")
    print(result['itinerary'])
