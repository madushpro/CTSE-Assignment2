"""
Location Research Agent - STUDENT 2 CONTRIBUTION

Role: Provides detailed destination information and attraction suggestions
Goal: Enrich travel plans with accurate cultural, historical and practical info
Backstory: Geography expert and cultural specialist

STUDENT 2: Responsible for this agent
- Implements location research using LLM reasoning
- Creates cultural insights and destination guides
- Handles fallback to mock data if LLM unavailable
"""

from typing import Dict, Any, List, Optional
import sys
import os
import logging

# Add tools directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'tools'))

from location_data_tool import get_location_data, get_attraction_suggestions

# Try to import Ollama client, fall back gracefully if not available
try:
    from ollama_client import create_ollama_client, OllamaClient
    OLLAMA_AVAILABLE = True
except ImportError:
    OLLAMA_AVAILABLE = False

logger = logging.getLogger(__name__)


class LocationResearchAgent:
    """Agent responsible for researching and providing destination information using Ollama LLM."""
    
    def __init__(self, use_ollama: bool = True):
        """Initialize Location Research Agent.
        
        Args:
            use_ollama (bool): Whether to use Ollama LLM (default: True)
        """
        self.role = "Destination Research Specialist"
        self.goal = "Provide rich, culturally accurate destination information to enhance travel plans"
        self.backstory = (
            "You are a travel researcher and cultural expert who has studied destinations "
            "across Sri Lanka extensively. You excel at providing practical travel tips, "
            "cultural insights, and attraction recommendations. You ensure travelers have "
            "authentic, memorable experiences."
        )
        self.tools_used = ["get_location_data", "get_attraction_suggestions"]
        
        # Initialize Ollama client if available
        self.ollama_client: Optional[OllamaClient] = None
        self.use_ollama = use_ollama and OLLAMA_AVAILABLE
        
        if self.use_ollama:
            try:
                self.ollama_client = create_ollama_client()
                logger.info("✓ Ollama LLM initialized for Location Research Agent")
            except Exception as e:
                logger.warning(f"Could not initialize Ollama: {str(e)}. Using mock data.")
                self.use_ollama = False
    
    def research_destination(self, destination: str) -> Dict[str, Any]:
        """
        Research and gather comprehensive information about a destination.
        
        Args:
            destination (str): The destination to research
        
        Returns:
            Dict[str, Any]: Comprehensive destination research including:
                           - 'destination': Destination name
                           - 'full_data': Complete location data
                           - 'summary': Brief summary
                           - 'highlights': Top 3 attractions
                           - 'practical_info': Travel tips
        
        Raises:
            ValueError: If destination is invalid
        """
        
        try:
            location_data = get_location_data(destination)
            attractions = get_attraction_suggestions(destination, 3)
            
            # Create enriched research data
            research = {
                "destination": destination,
                "full_data": location_data,
                "summary": location_data.get("description", ""),
                "highlights": attractions,
                "practical_info": self._build_practical_info(destination, location_data),
                "best_season": location_data.get("best_season", ""),
                "climate": location_data.get("climate", ""),
                "accommodation_options": location_data.get("accommodations", [])
            }
            
            return research
        
        except ValueError as e:
            raise ValueError(f"Research failed for {destination}: {str(e)}")
    
    def create_detailed_guide(self, destination: str) -> str:
        """
        Create a detailed travel guide for a destination.
        
        Args:
            destination (str): The destination
        
        Returns:
            str: Formatted travel guide
        """
        
        research = self.research_destination(destination)
        
        guide = f"""
{'='*70}
DESTINATION RESEARCH GUIDE: {destination.upper()}
{'='*70}

OVERVIEW
--------
{research['summary']}

BEST TIME TO VISIT
------------------
{research['best_season']}

CLIMATE
-------
{research['climate']}

TOP ATTRACTIONS
---------------
"""
        
        for i, attraction in enumerate(research['highlights'], 1):
            guide += f"{i}. {attraction}\n"
        
        guide += f"""
ACCOMMODATION OPTIONS
---------------------
"""
        for option in research['accommodation_options'][:3]:
            guide += f"• {option}\n"
        
        guide += f"""
LOCAL CUISINES
--------------
"""
        cuisines = research['full_data'].get('cuisines', [])
        for cuisine in cuisines[:3]:
            guide += f"• {cuisine}\n"
        
        guide += f"""
TRAVEL TIPS
-----------
{research.get('practical_info', '')}

{'='*70}
"""
        
        return guide
    
    def _build_practical_info(self, destination: str, location_data: Dict) -> str:
        """Build practical travel information for destination."""
        
        transport_info = location_data.get('transport', '')
        altitude_info = f"Altitude: {location_data.get('altitude', 'N/A')}"
        
        tips = f"""
• Transportation: {transport_info}
• {altitude_info}
• Pack light, breathable clothing
• Bring sunscreen and insect repellent
• Respect local customs and cultural sites
• Try local cuisine at street food stalls
• Bargain respectfully at markets
• Keep local currency for small purchases
"""
        
        return tips
    
    def get_cultural_insights(self, destination: str) -> List[str]:
        """
        Get cultural insights for a destination.
        
        Args:
            destination (str): The destination
        
        Returns:
            List[str]: List of cultural insights and tips
        """
        
        cultural_insights = {
            "Ella": [
                "Ella is a peaceful hill station beloved by hikers and nature enthusiasts",
                "The area is home to tea plantations - try fresh Ceylon tea",
                "Nine Arch Bridge is best photographed at sunset",
                "Locals recommend the train ride for stunning mountain views",
                "The town has a quirky, bohemian atmosphere popular with backpackers"
            ],
            "Kandy": [
                "The Temple of the Tooth is one of Buddhism's holiest sites",
                "Kandy Esala Perahera (August) is a spectacular festival procession",
                "The lake provides a peaceful escape in the city center",
                "Accept invitations to local homes - Sri Lankan hospitality is renowned",
                "Traditional drum performances showcase local culture"
            ],
            "Colombo": [
                "Colombo is the vibrant heart of modern Sri Lanka",
                "Mix of colonial architecture and contemporary development",
                "Galle Face Promenade is the city's soul - best visited at sunset",
                "Street food culture is incredible - try kottu roti and lamprais",
                "The city is culturally diverse with Hindu, Buddhist, and Muslim communities"
            ]

        }
        
        return cultural_insights.get(destination, ["No specific insights available"])
    
    
    def _generate_llm_insights(self, destination: str, itinerary: str) -> str:
        """Generate enhanced insights using Ollama LLM.
        
        Args:
            destination: Travel destination
            itinerary: Current itinerary
            
        Returns:
            str: LLM-generated enhanced insights
        """
        if not self.ollama_client:
            raise RuntimeError("Ollama client not initialized")
        
        prompt = f"""Based on this {destination} travel itinerary, provide cultural insights and travel tips:

{itinerary}

Provide:
1. Key cultural considerations for {destination}
2. Best times to visit attractions
3. Local dining recommendations
4. Safety and practical tips
5. Hidden gems not in standard guides"""
        
        system_prompt = (
            "You are an expert travel guide specializing in Sri Lankan destinations. "
            "Provide authentic, practical cultural insights that enhance travel experiences. "
            "Format responses with clear sections and bullet points."
        )
        
        logger.info(f"Generating LLM insights for {destination}")
        insights = self.ollama_client.generate(
            prompt=prompt,
            system=system_prompt,
            temperature=0.6,
            max_tokens=600
        )
        
        if not insights or len(insights.strip()) < 50:
            raise ValueError("LLM returned empty or too-short response")
        
        return insights
    
    def enhance_itinerary(self, itinerary: str, destination: str) -> str:
        """
        Enhance an itinerary with location research information.
        Uses Ollama LLM for intelligent insights with fallback to mock data.
        
        Args:
            itinerary (str): The original itinerary
            destination (str): The destination
        
        Returns:
            str: Enhanced itinerary with research insights
        """
        
        research = self.research_destination(destination)
        
        # Try LLM generation first
        if self.use_ollama and self.ollama_client:
            try:
                llm_insights = self._generate_llm_insights(destination, itinerary)
                source_note = "\n[Enhanced with Ollama LLM reasoning]\n"
                return itinerary + "\n" + "="*70 + "\n" + source_note + llm_insights
            except Exception as e:
                logger.warning(f"LLM enhancement failed: {str(e)}. Using mock data.")
        
        # Fallback to mock data
        cultural_tips = self.get_cultural_insights(destination)
        
        enhanced = itinerary + "\n" + "="*70 + "\n"
        enhanced += "LOCATION RESEARCH & CULTURAL INSIGHTS (Mock Data)\n"
        enhanced += "="*70 + "\n\n"
        
        enhanced += f"DESTINATION OVERVIEW:\n{research['summary']}\n\n"
        
        enhanced += "CULTURAL TIPS:\n"
        for tip in cultural_tips[:3]:
            enhanced += f"• {tip}\n"
        
        enhanced += f"\nBEST TIME TO VISIT:\n{research['best_season']}\n"
        enhanced += f"\nCLIMATE:\n{research['climate']}\n"
        
        return enhanced
    
    
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
    # Test the Location Research Agent
    print("\n=== Location Research Agent Tests ===\n")
    
    agent = LocationResearchAgent()
    
    # Test 1: Research destination
    print("Test 1: Research Ella")
    research = agent.research_destination("Ella")
    print(f"Destination: {research['destination']}")
    print(f"Best Season: {research['best_season']}")
    print(f"Top Attractions: {research['highlights'][:2]}\n")
    
    # Test 2: Create detailed guide
    print("Test 2: Create travel guide for Kandy")
    guide = agent.create_detailed_guide("Kandy")
    print(guide)
