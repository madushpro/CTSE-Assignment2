"""
Streamlit UI for AI Travel Planner Multi-Agent System

Provides an interactive web interface for generating travel plans.
"""

import streamlit as st
import sys
import os
from datetime import datetime

# Add paths for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from main import TravelPlannerMAS


# Page configuration
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
        .main { padding: 20px; }
        .stButton > button { width: 100%; }
        .success-box { background-color: #d4edda; padding: 15px; border-radius: 5px; }
        .error-box { background-color: #f8d7da; padding: 15px; border-radius: 5px; }
        .info-box { background-color: #d1ecf1; padding: 15px; border-radius: 5px; }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("✈️ AI Travel Planner")
st.markdown("### Generate personalized travel itineraries powered by Multi-Agent AI")

# Sidebar for inputs
st.sidebar.markdown("## 📋 Trip Planning")

destination = st.sidebar.selectbox(
    "Select Destination",
    options=["Ella", "Kandy", "Colombo", "Galle"],
    help="Choose from popular Sri Lankan destinations"
)

num_days = st.sidebar.slider(
    "Number of Days",
    min_value=1,
    max_value=10,
    value=3,
    help="Duration of your trip"
)

budget = st.sidebar.number_input(
    "Budget (LKR)",
    min_value=5000,
    max_value=500000,
    value=20000,
    step=1000,
    help="Your total budget in Sri Lankan Rupees"
)

generate_button = st.sidebar.button(
    "🚀 Generate Travel Plan",
    use_container_width=True
)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### Your Trip Details")
    st.write(f"""
    - **Destination:** {destination}
    - **Duration:** {num_days} days
    - **Budget:** Rs. {budget:,}
    """)

with col2:
    st.markdown("### Budget Breakdown")
    daily_budget = budget / num_days
    st.metric("Daily Budget", f"Rs. {daily_budget:,.0f}")

# Plan generation
if generate_button:
    with st.spinner("🔄 Generating your travel plan..."):
        try:
            # Initialize MAS
            mas = TravelPlannerMAS()
            
            # Generate plan
            result = mas.generate_travel_plan(
                destination=destination,
                num_days=num_days,
                budget=budget
            )
            
            if result['success']:
                # Store in session state
                st.session_state.plan_result = result
                st.session_state.mas = mas
                
                st.success("✓ Travel plan generated successfully!")
                
                # Display summary
                st.markdown("---")
                st.markdown("### 📊 Plan Summary")
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Estimated Cost", f"Rs. {result['estimated_cost']:,.0f}")
                with col2:
                    st.metric("Budget Limit", f"Rs. {budget:,.0f}")
                with col3:
                    remaining = budget - result['estimated_cost']
                    st.metric("Remaining", f"Rs. {remaining:,.0f}")
                with col4:
                    st.metric("Quality Score", f"{result['validation']['quality_score']:.1f}/100")
                
                # Plan status
                st.markdown("---")
                if result['validation']['ready_for_delivery']:
                    st.markdown('<div class="success-box"><h4>✓ Plan Approved for Delivery</h4></div>', 
                              unsafe_allow_html=True)
                else:
                    st.markdown('<div class="error-box"><h4>⚠ Plan Requires Review</h4></div>', 
                              unsafe_allow_html=True)
                
                # Full plan content
                st.markdown("---")
                st.markdown("### 📅 Your Detailed Itinerary")
                
                with st.expander("📖 View Full Plan", expanded=True):
                    st.text_area(
                        "Complete Travel Plan",
                        value=result['final_plan'],
                        height=600,
                        disabled=True
                    )
                
                # Download plan
                plan_text = result['final_plan']
                st.download_button(
                    label="📥 Download Plan as TXT",
                    data=plan_text,
                    file_name=f"travel_plan_{destination}_{num_days}days.txt",
                    mime="text/plain"
                )
            
            else:
                st.error("❌ Failed to generate plan")
        
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# Show existing plan if available
if 'plan_result' in st.session_state:
    st.markdown("---")
    
    # Tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs(["Itinerary", "Budget", "Validation", "Logs"])
    
    with tab1:
        st.markdown("### Day-by-Day Itinerary")
        st.text(st.session_state.plan_result['itinerary'])
    
    with tab2:
        st.markdown("### Budget Breakdown")
        cost = st.session_state.plan_result['cost_analysis']['breakdown']
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Cost Details:**")
            st.write(f"""
            - Accommodation: Rs. {cost['accommodation']:,.2f}
            - Food: Rs. {cost['food']:,.2f}
            - Transport: Rs. {cost['transport']:,.2f}
            - Activities: Rs. {cost['activities']:,.2f}
            """)
        
        with col2:
            st.write("**Cost Summary:**")
            st.write(f"""
            - Subtotal: Rs. {cost['subtotal']:,.2f}
            - Buffer (10%): Rs. {cost['buffer']:,.2f}
            - **TOTAL: Rs. {cost['total']:,.2f}**
            """)
        
        # Cost chart
        chart_data = {
            "Category": ["Accommodation", "Food", "Transport", "Activities"],
            "Cost": [
                cost['accommodation'],
                cost['food'],
                cost['transport'],
                cost['activities']
            ]
        }
        
        import pandas as pd
        df = pd.DataFrame(chart_data)
        st.bar_chart(df.set_index("Category"))
    
    with tab3:
        st.markdown("### Plan Validation Report")
        validation = st.session_state.plan_result['validation']
        st.write(f"""
        **Validation Results:**
        - Overall Valid: {'✓ Yes' if validation['overall_valid'] else '✗ No'}
        - Ready for Delivery: {'✓ Yes' if validation['ready_for_delivery'] else '✗ No'}
        - Quality Score: {validation['quality_score']:.1f}/100
        """)
        
        if validation['structure_validation']['issues']:
            st.warning("**Issues Found:**")
            for issue in validation['structure_validation']['issues']:
                st.write(f"- {issue}")
        
        st.info("**Recommendations:**")
        for rec in validation['recommendations']:
            st.write(f"- {rec}")
    
    with tab4:
        st.markdown("### Execution Logs")
        logs = st.session_state.mas.get_logs()
        st.text_area(
            "System Logs",
            value=logs,
            height=400,
            disabled=True
        )

# Information section
with st.sidebar:
    st.markdown("---")
    st.markdown("## ℹ️ About")
    st.markdown("""
    This AI Travel Planner uses a multi-agent system to:
    
    1. **Plan** your itinerary
    2. **Research** destinations
    3. **Estimate** costs
    4. **Validate** your plan
    
    All processing happens locally without API calls.
    """)
    
    st.markdown("---")
    st.markdown("**Destinations Available:**")
    st.write("""
    - **Ella**: Hill station with hiking and tea plantations
    - **Kandy**: Cultural capital with sacred temple
    - **Colombo**: Modern capital with beaches
    - **Galle**: Historic coastal fort
    """)
    
    st.markdown("---")
    st.markdown("**Version:** 1.0  \n**Status:** ✓ Production Ready")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <small>AI Travel Planner v1.0 | Powered by Multi-Agent System | © 2025</small>
</div>
""", unsafe_allow_html=True)
