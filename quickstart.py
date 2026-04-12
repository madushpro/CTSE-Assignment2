#!/usr/bin/env python3
"""
QUICK START GUIDE - AI Travel Planner Multi-Agent System

This script provides step-by-step setup and testing instructions.
"""

import os
import sys
from pathlib import Path

def print_section(title):
    """Print formatted section header."""
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")

def print_step(number, description):
    """Print numbered step."""
    print(f"  {number}. {description}")

def check_file_exists(filepath):
    """Check if file exists."""
    return "✓" if Path(filepath).exists() else "✗"

def main():
    print_section("AI TRAVEL PLANNER - QUICK START GUIDE")
    
    print("""
This is a complete Multi-Agent System (MAS) for generating personalized
travel itineraries. The system uses 4 intelligent agents working together
to create comprehensive travel plans.
    """)
    
    # System check
    print_section("STEP 1: System Check")
    
    project_files = {
        "Main Application": "main.py",
        "Streamlit UI": "app.py",
        "Requirements": "requirements.txt",
        "Tests": "tests/test_tools.py",
        "Agent 1 (Planner)": "agents/planner.py",
        "Agent 2 (Researcher)": "agents/researcher.py",
        "Agent 3 (Estimator)": "agents/estimator.py",
        "Agent 4 (Validator)": "agents/validator.py",
        "Tool 1 (Cost Calculator)": "tools/cost_calculator_tool.py",
        "Tool 2 (Location Data)": "tools/location_data_tool.py",
        "Tool 3 (Validation)": "tools/validation_tool.py",
        "Tool 4 (File Saver)": "tools/file_saver_tool.py",
    }
    
    print("  Checking required files...")
    all_exist = True
    for name, filepath in project_files.items():
        status = check_file_exists(filepath)
        print(f"    {status} {name:30s} {filepath}")
        if status == "✗":
            all_exist = False
    
    if not all_exist:
        print("\n  ✗ Some files are missing! Check project structure.")
        return False
    
    print("\n  ✓ All required files present!")
    
    # Installation
    print_section("STEP 2: Installation")
    
    print("  Run one of the following commands:")
    print()
    print("  Option A - Using pip:")
    print("    python -m pip install streamlit pandas pytest pytest-cov")
    print()
    print("  Option B - Using requirements.txt:")
    print("    python -m pip install -r requirements.txt")
    print()
    print("  (If you have multiple Python versions, use python3 or python3.8+)")
    
    # Usage options
    print_section("STEP 3: Run the Application")
    
    print("  Choose your preferred interface:")
    print()
    print("  Option A - Web Interface (Recommended):")
    print("    streamlit run app.py")
    print("    Then open: http://localhost:8501")
    print()
    print("  Option B - Command Line:")
    print("    python main.py")
    print()
    print("  Option C - Run Tests:")
    print("    python -m pytest tests/test_tools.py -v")
    
    # How it works
    print_section("STEP 4: Understanding the System")
    
    print("  The system works in stages:")
    print()
    print("  1. TRAVEL PLANNER AGENT")
    print("     Creates day-by-day itinerary structure")
    print()
    print("  2. LOCATION RESEARCH AGENT")
    print("     Adds destination details and cultural insights")
    print()
    print("  3. BUDGET ESTIMATOR AGENT")
    print("     Calculates all costs (accommodation, food, transport, activities)")
    print()
    print("  4. PLAN VALIDATOR AGENT")
    print("     Checks quality, validates against budget, ensures completeness")
    print()
    print("  All agents work together to create an optimal travel plan!")
    
    # Features
    print_section("STEP 5: Features")
    
    print("  ✓ 4 Intelligent Agents with distinct roles")
    print("  ✓ 4 Custom Python Tools (no external APIs)")
    print("  ✓ Supports 4 destinations: Ella, Kandy, Colombo, Galle")
    print("  ✓ Flexible trip duration (1-10 days)")
    print("  ✓ Budget analysis and recommendations")
    print("  ✓ Quality scoring (0-100)")
    print("  ✓ Execution logging for transparency")
    print("  ✓ Plan saved to output.txt")
    print("  ✓ Beautiful web interface")
    
    # Example usage
    print_section("STEP 6: Example Usage")
    
    print("  Input Example:")
    print("    Destination: Ella")
    print("    Days: 3")
    print("    Budget: Rs. 25,000")
    print()
    print("  Output Includes:")
    print("    - Day-by-day itinerary")
    print("    - Accommodation recommendations")
    print("    - Attraction suggestions")
    print("    - Complete cost breakdown")
    print("    - Budget validation")
    print("    - Quality score and recommendations")
    
    # File locations
    print_section("STEP 7: Important Files")
    
    print("  Generated Plans: output.txt")
    print("  Execution Logs: logs/log.txt")
    print("  Test Results: Run 'pytest tests/test_tools.py -v'")
    print()
    print("  You can download generated plans from the web interface")
    print("  or view them directly from output.txt")
    
    # Troubleshooting
    print_section("STEP 8: Troubleshooting")
    
    print("  If you get 'module not found' errors:")
    print("    1. Ensure you're in the project directory")
    print("    2. Install dependencies: pip install streamlit pandas pytest")
    print("    3. Use full path: python -m pip install ...")
    print()
    print("  If port 8501 is already in use:")
    print("    streamlit run app.py --server.port=8502")
    print()
    print("  To run tests without pytest installed:")
    print("    python tools/cost_calculator_tool.py")
    print("    python tools/location_data_tool.py")
    print("    python agents/planner.py")
    
    # Next steps
    print_section("STEP 9: Next Steps")
    
    print("  1. Run the web interface to explore the system")
    print("  2. Try generating plans for different destinations")
    print("  3. Test with different trip durations and budgets")
    print("  4. Check logs to see agent execution flow")
    print("  5. Review generated plans in output.txt")
    print("  6. Run tests to ensure everything works")
    
    # Success
    print_section("✓ You're Ready!")
    
    print("""
  Everything is set up and ready to use!
  
  The AI Travel Planner is a complete Multi-Agent System that
  generates intelligent travel plans by orchestrating 4 specialized agents.
  
  Start with:  streamlit run app.py
  
  Or:          python main.py
  
  Enjoy your travel planning experience!
    """)
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
