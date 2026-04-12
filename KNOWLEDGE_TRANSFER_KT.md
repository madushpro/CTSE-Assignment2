# 🎓 KNOWLEDGE TRANSFER (KT) - How This System Works

## 📚 Table of Contents
1. System Overview
2. Technology Stack
3. How Each Component Works
4. Data Flow
5. Agent-by-Agent Breakdown
6. Tool Functionality
7. Ollama LLM Integration
8. Configuration & Customization

---

## 🏗️ SYSTEM OVERVIEW

### What is This System?

**AI Travel Planner** is a **Multi-Agent System (MAS)** that uses **4 specialized AI agents** working together to plan Sri Lankan travel itineraries.

### Why Multi-Agent?

Instead of one AI doing everything (creative, analytical, financial, validation), we have 4 specialized agents:
- **Agent 1**: Creative planning (itineraries)
- **Agent 2**: Research & insights
- **Agent 3**: Financial analysis (costs)
- **Agent 4**: Quality verification

This mimics how human teams work!

### High-Level Flow

```
User Input
(destination, duration, budget)
       ↓
    ┌─────────────────────────────┐
    │  Agent 1: Travel Planner    │
    │  Creates itinerary          │
    └─────────────────────────────┘
       ↓ (itinerary data)
    ┌─────────────────────────────┐
    │  Agent 2: Researcher        │
    │  Adds cultural insights     │
    └─────────────────────────────┘
       ↓ (enhanced plan)
    ┌─────────────────────────────┐
    │  Agent 3: Budget Estimator  │
    │  Calculates costs           │
    └─────────────────────────────┘
       ↓ (plan + costs)
    ┌─────────────────────────────┐
    │  Agent 4: Plan Validator    │
    │  Validates quality          │
    └─────────────────────────────┘
       ↓ (final plan)
    Output File (output.txt)
```

---

## 🔧 TECHNOLOGY STACK

### Programming Language
- **Python 3.8+**
  - Why? Popular for AI/ML, easy to learn, great libraries
  - Used for: All agents, tools, orchestration

### Framework & Libraries

| Technology | Purpose | Why Used |
|-----------|---------|---------|
| **Ollama** | Local LLM | Free, local, no API costs |
| **llama3:8b** | Language model | Fast, 8B parameters, good quality |
| **Streamlit** | Web UI | Easy interactive interface |
| **Pandas** | Data processing | Handle travel data |
| **Pytest** | Testing | Comprehensive test coverage |
| **Requests** | HTTP calls | Talk to Ollama API |

### Architecture Pattern
- **Sequential Pipeline**: Each agent's output → Next agent's input
- **State Management**: Dictionary-based context passing
- **LLM Integration**: HTTP calls to local Ollama server

### Version Control
- **Git** & **GitHub**: Team collaboration

---

## 🤖 HOW EACH AGENT WORKS

### AGENT 1: Travel Planner (Student 1)

**What it does:**
- Takes destination, duration, travel style
- Generates day-by-day itinerary
- Suggests activities, restaurants, hotels

**How it works:**

```python
FlowChart:
1. Input: "Ella, 3 days, adventure"
   ↓
2. Check if Ollama available
   ├─ YES: Send prompt to LLM
   │       "Create detailed 3-day Ella itinerary..."
   │       LLM responds with creative schedule
   │
   └─ NO: Use mock data (predefined itinerary)
   ↓
3. Return itinerary dictionary:
   {
     "destination": "Ella",
     "days": 3,
     "itinerary": "Day 1: ...",
     "activities": [...],
     "hotels": [...]
   }
```

**Technology Used:**
- Ollama LLM for creative content generation
- Temperature: 0.7 (creative, varied outputs)
- Token limit: 800 (detailed responses)

**Tool Used:**
- `cost_calculator_tool.py` - calculates base costs

---

### AGENT 2: Location Researcher (Student 2)

**What it does:**
- Takes the itinerary from Agent 1
- Adds cultural information
- Adds local tips and best times to visit
- Enhances with practical information

**How it works:**

```python
FlowChart:
1. Input: Itinerary from Agent 1
   ↓
2. Extract destination name
   ↓
3. Check if Ollama available
   ├─ YES: "Based on this itinerary, provide cultural insights..."
   │       LLM enhances with local knowledge
   │
   └─ NO: Use mock data (predefined tips)
   ↓
4. Return enhanced itinerary:
   {
     ...previous data...
     "cultural_insights": "...",
     "local_tips": "...",
     "best_time_to_visit": "..."
   }
```

**Technology Used:**
- Ollama LLM for knowledge generation
- Temperature: 0.6 (balanced, accurate)
- Token limit: 600 (practical information)

**Tool Used:**
- `location_data_tool.py` - retrieves destination data

---

### AGENT 3: Budget Estimator (Student 3)

**What it does:**
- Takes the itinerary + enhanced plan
- Calculates detailed costs
- Breaks down accommodation, meals, transport, activities
- Provides cost recommendations

**How it works:**

```python
FlowChart:
1. Input: Plan from Agent 2 + user budget
   ↓
2. Extract: destination, days, accommodation preference
   ↓
3. Calculate costs using tool:
   accommodation_cost = days × hotel_rate
   meal_cost = days × daily_meal_budget
   transport_cost = fixed + variable
   activity_cost = calculated from activities
   ↓
4. Check if Ollama available
   ├─ YES: "Generate budget recommendations..."
   │       LLM personalizes suggestions
   │
   └─ NO: Use rule-based suggestions
   ↓
5. Return cost analysis:
   {
     ...previous data...
     "total_cost": 30360,
     "cost_breakdown": {...},
     "budget_status": "OVER BUDGET",
     "recommendations": "..."
   }
```

**Technology Used:**
- Ollama LLM for personalized advice
- Temperature: 0.6 (practical recommendations)
- Token limit: 500 (concise advice)

**Tool Used:**
- `validation_tool.py` - validates cost data

---

### AGENT 4: Plan Validator (Student 4)

**What it does:**
- Takes complete plan from Agent 3
- Validates all aspects
- Generates quality score
- Provides final feedback
- Saves to file

**How it works:**

```python
FlowChart:
1. Input: Complete plan from Agent 3
   ↓
2. Validate plan structure:
   - Check all sections present
   - Check data completeness
   - Check logic consistency
   ↓
3. Calculate quality score:
   ├─ Itinerary quality (0-30 pts)
   ├─ Research quality (0-20 pts)
   ├─ Cost accuracy (0-30 pts)
   └─ Validation logic (0-20 pts)
   Total: 0-100
   ↓
4. Check if Ollama available
   ├─ YES: "Review plan and provide quality feedback..."
   │       LLM gives detailed critique
   │
   └─ NO: Use rule-based feedback
   ↓
5. Save plan to file using tool
   ↓
6. Return final validated plan:
   {
     ...all previous data...
     "quality_score": 70.0,
     "validation_feedback": "...",
     "saved_to_file": "output.txt"
   }
```

**Technology Used:**
- Ollama LLM for quality analysis
- Temperature: 0.6 (structured feedback)
- Token limit: 500 (actionable feedback)

**Tool Used:**
- `file_saver_tool.py` - saves to file

---

## 🛠️ TOOLS EXPLAINED

### Tool 1: Cost Calculator Tool (Student 1)

**File:** `tools/cost_calculator_tool.py`

**Purpose:** Calculate travel costs based on destination, duration, accommodation type

**How it works:**

```python
def calculate_travel_cost(destination, num_days, accommodation_type):
    """
    Calculates: accommodation, meals, transport, activities
    
    Input:
      - destination: str (e.g., "Ella")
      - num_days: int (e.g., 3)
      - accommodation_type: str ("budget", "mid-range", "luxury")
    
    Output:
      - Dictionary with cost breakdown
    
    Example:
      Input: ("Ella", 3, "mid-range")
      Output: {
        "accommodation": 300,
        "meals": 150,
        "transport": 200,
        "activities": 300,
        "total": 950
      }
    """
    # Logic: Fixed rates × number of days + fixed costs
```

**Business Logic:**
- Accommodation: Different rates per accommodation type × days
- Meals: Daily meal budget × days
- Transport: Base cost + distance-based
- Activities: Cost per activity × days

---

### Tool 2: Location Data Tool (Student 2)

**File:** `tools/location_data_tool.py`

**Purpose:** Retrieve information about a destination

**How it works:**

```python
def get_location_data(destination):
    """
    Returns: destination info, restaurants, activities, ratings
    
    Input:
      - destination: str (e.g., "Ella")
    
    Output:
      - Dictionary with:
        - description
        - weather
        - population
        - famous_for
        - restaurants (list)
        - activities (list)
        - hotels (list)
        - best_time_to_visit
        - cultural_tips
    
    Example:
      Input: "Ella"
      Output: {
        "description": "Hill station town...",
        "weather": "Cool, misty",
        "famous_for": ["Tea plantations", "Nine Arch Bridge"],
        "restaurants": ["..."],
        "activities": ["Hiking", "Bird watching"]
      }
    """
    # Logic: Dictionary lookup + data retrieval
```

**Data Structure:**
- Maintains database of Sri Lankan locations
- Each location has activities, restaurants, prices
- Returns curated information

---

### Tool 3: Validation Tool (Student 3)

**File:** `tools/validation_tool.py`

**Purpose:** Validate travel plan structure and quality

**How it works:**

```python
def validate_plan_structure(plan_dict):
    """
    Checks: plan completeness, logic consistency, validity
    
    Input:
      - plan_dict: dictionary with complete plan
    
    Output:
      - Validation result:
        - is_valid: bool
        - score: 0-100
        - issues: list of problems
        - feedback: text explanation
    
    Validates:
      - All required fields present
      - Data types correct
      - Values within valid ranges
      - Logical consistency
    
    Example:
      Input: {
        "destination": "Ella",
        "days": 3,
        "budget": 20000,
        "cost": 30360
      }
      Output: {
        "is_valid": True,
        "score": 70,
        "issues": ["Budget exceeded by 52%"],
        "feedback": "Plan is valid but over budget"
      }
    """
    # Logic: Series of validation checks
```

**Validation Checks:**
1. Field completeness check
2. Data type validation
3. Range checking (costs, days, etc.)
4. Logic validation (costs match activities, etc.)
5. Consistency checking (all pieces fit together)

---

### Tool 4: File Saver Tool (Student 4)

**File:** `tools/file_saver_tool.py`

**Purpose:** Save travel plan to file for user

**How it works:**

```python
def save_travel_plan(plan_dict, filename="output.txt"):
    """
    Format and save plan to file
    
    Input:
      - plan_dict: complete travel plan
      - filename: output file path
    
    Output:
      - File saved successfully: True/False
      - File path
      - File size
    
    Steps:
      1. Format plan data nicely
      2. Create text output
      3. Write to file
      4. Verify file created
      5. Return status
    """
    # Logic: Format + file I/O operations
```

**File Format:**
```
========================================
TRAVEL PLAN: Ella
========================================

ITINERARY
Day 1: ...
Day 2: ...
Day 3: ...

CULTURAL INSIGHTS
...

COST BREAKDOWN
Accommodation: Rs. 3,000
Meals: Rs. 1,500
...
TOTAL: Rs. 30,360

VALIDATION
Quality Score: 70/100
Status: ⚠ REVIEW NEEDED
```

---

## 🧠 OLLAMA LLM INTEGRATION

### What is Ollama?

**Ollama** = Free, local language model running on your machine

- **Local**: Runs on your computer, not cloud
- **Free**: No API costs, no subscriptions
- **Private**: Your data doesn't leave your machine
- **Fast**: Instant responses

### How Ollama Works

```
Your Computer
├─ Ollama Server (runs on port 11434)
│  ├─ llama3:8b model loaded in memory
│  └─ Listens for HTTP requests
│
└─ Your Application
   ├─ Sends: HTTP POST to localhost:11434
   ├─ Sends: Prompt + config (temperature, tokens)
   ├─ Receives: LLM response
   └─ Processes: Response for application
```

### Ollama in This System

**File:** `ollama_client.py`

```python
class OllamaClient:
    def __init__(self):
        """Connect to Ollama server"""
        self.url = "http://localhost:11434/api/generate"
    
    def generate(self, prompt, temperature=0.7, tokens=500):
        """
        Send prompt to Ollama, get LLM response
        
        Process:
        1. Format prompt with model params
        2. Send HTTP POST to Ollama
        3. Parse JSON response
        4. Return text
        
        If Ollama unavailable:
        → Fallback to mock data
        → System still works!
        """
```

### Temperature Explanation

**Temperature** = How creative/random the LLM is

```
Temperature 0.0 (Deterministic)
└─ Same input = Same output
   █████████████████████
   Very consistent, boring

Temperature 0.5 (Balanced)
└─ Same input = Similar but varied output
   ██████████░░░░░░░░░░
   Balanced between consistent & creative

Temperature 0.9 (Creative)
└─ Same input = Very different outputs
   ████░░░░░░░░░░░░░░░░
   Very creative, unpredictable
   
Used in this system:
- Travel Planner: 0.7 (creative itineraries)
- Researcher: 0.6 (accurate insights)
- Estimator: 0.6 (practical recommendations)
- Validator: 0.6 (structured feedback)
```

### Token Limit Explanation

**Tokens** = Length of LLM response

```
1 token ≈ 4 characters

Token limit 800 = ~3200 characters response
Token limit 500 = ~2000 characters response

Used in this system:
- Travel Planner: 800 tokens (detailed itineraries)
- Researcher: 600 tokens (rich insights)
- Estimator: 500 tokens (concise advice)
- Validator: 500 tokens (actionable feedback)
```

### Graceful Fallback

When Ollama not available:

```python
try:
    response = ollama_client.generate(prompt)
    return response  # Use real LLM
except ConnectionError:
    return mock_data  # Fallback to predefined data
    print("Ollama unavailable, using mock data")
```

**Result**: System works with OR without Ollama!

---

## 📊 DATA FLOW IN DETAIL

### Complete Data Journey

```
1. USER INPUT
   ├─ Destination: "Ella"
   ├─ Duration: 3 days
   └─ Budget: Rs. 20,000

2. AGENT 1: Travel Planner
   ├─ Prompt: "Create 3-day itinerary for Ella"
   ├─ LLM Response: Detailed day-by-day plan
   └─ Output: 
      {
        "destination": "Ella",
        "days": 3,
        "itinerary": "Day 1: Arrive, settle in...",
        "activities": ["Hiking", "Tea tour"],
        "hotels": ["3 Seasons", "Ella Sky"]
      }

3. AGENT 2: Location Researcher
   ├─ Input: Previous output
   ├─ LLM Prompt: "Add cultural insights to this itinerary"
   ├─ LLM Response: Cultural tips, best times, local info
   └─ Output: All previous + "cultural_insights": "..."

4. AGENT 3: Budget Estimator
   ├─ Input: Plan with insights
   ├─ Calculation: cost_calculator_tool.calculate_travel_cost()
   ├─ LLM Prompt: "Generate budget recommendations"
   ├─ LLM Response: Personalized budget advice
   └─ Output: All previous + costs breakdown

5. AGENT 4: Plan Validator
   ├─ Input: Complete plan with costs
   ├─ Validation: validation_tool.validate_plan_structure()
   ├─ Scoring: Calculate 0-100 quality score
   ├─ LLM Prompt: "Review and provide feedback"
   ├─ LLM Response: Quality assessment
   ├─ File Save: file_saver_tool.save_travel_plan()
   └─ Output: Final plan JSON + output.txt file

6. OUTPUT FILE: output.txt
   Contains: Complete travel plan with all information
```

### State Management

**State** = All data passed through pipeline

```python
# State starts as dictionary
state = {}

# Agent 1 modifies state
state = agent1.create_itinerary(destination, days)
# state now has: destination, days, itinerary, activities, hotels

# Agent 2 receives same state, adds to it
state = agent2.enhance_itinerary(state)
# state now has: + cultural_insights, best_time

# Agent 3 receives augmented state
state = agent3.estimate_costs(state)
# state now has: + total_cost, cost_breakdown, budget_status

# Agent 4 receives fully populated state
state = agent4.validate_complete_plan(state)
# state now has: + quality_score, validation_feedback

# Final state saved to file
save_to_file(state)
```

---

## ⚙️ CONFIGURATION & CUSTOMIZATION

### How to Modify System Behavior

#### 1. Change Ollama Temperature (Creativity Level)

**File:** `agents/planner.py` (example for Agent 1)

```python
# Current: temperature=0.7 (creative)
response = self.ollama_client.generate(prompt, temperature=0.7)

# More creative: temperature=0.9
response = self.ollama_client.generate(prompt, temperature=0.9)

# More consistent: temperature=0.3
response = self.ollama_client.generate(prompt, temperature=0.3)
```

#### 2. Change Token Limit (Response Length)

**File:** `agents/planner.py`

```python
# Current: 800 tokens (longer responses)
response = self.ollama_client.generate(prompt, tokens=800)

# Shorter responses: 400 tokens
response = self.ollama_client.generate(prompt, tokens=400)

# Very detailed: 1200 tokens
response = self.ollama_client.generate(prompt, tokens=1200)
```

#### 3. Add New Destination

**File:** `tools/location_data_tool.py`

```python
# Add to LOCATIONS dictionary:
"Sigiriya": {
    "description": "Ancient rock fortress...",
    "weather": "Hot, dry",
    "famous_for": ["Rock climbing", "Ancient palace"],
    "restaurants": ["Risala", "Elephants Restaurant"],
    "activities": ["Climbing", "Photography"],
    "hotels": ["Sigiri Village", "Sigiri Rooms"],
    "best_time_to_visit": "November to March",
    "cultural_tips": "..."
}
```

#### 4. Modify Cost Calculation

**File:** `tools/cost_calculator_tool.py`

```python
# Current rates (modify as needed):
accommodation_rates = {
    "budget": 100,      # Rs per night
    "mid-range": 250,   # Rs per night
    "luxury": 500       # Rs per night
}

# Meal costs (modify as needed):
meal_budget_per_day = {
    "budget": 50,
    "mid-range": 100,
    "luxury": 200
}
```

#### 5. Change Validation Scoring

**File:** `tools/validation_tool.py`

```python
# Modify scoring weights:
itinerary_weight = 30   # How much itinerary affects score
research_weight = 20    # How much research affects score
cost_weight = 30        # How much cost accuracy affects score
validation_weight = 20  # How much validation logic affects score
```

---

## 🔄 ORCHESTRATION PROCESS

### How main.py Coordinates Everything

**File:** `main.py`

```python
class TravelPlannerMAS:
    def generate_plan(self, destination, days, budget):
        """
        Orchestrates all 4 agents
        """
        
        # 1. Input Validation
        if not self._validate_input(destination, days, budget):
            return error
        
        # 2. Agent 1: Create Itinerary
        planner_result = self.planner.create_itinerary(
            destination, days, preferences
        )
        
        # 3. Agent 2: Research & Enhance
        enhanced_itinerary = self.researcher.research_destination(
            destination, planner_result
        )
        
        # 4. Agent 3: Estimate Costs
        cost_analysis = self.estimator.estimate_budget(
            destination, days, enhanced_itinerary
        )
        
        # 5. Agent 4: Validate & Save
        final_plan = self.validator.validate_plan(cost_analysis)
        
        return final_plan
```

### Error Handling

**What happens if something fails:**

```python
try:
    result = Agent.process(data)
except LLMError:
    print("Ollama unavailable")
    result = FallbackMockData()  # Use mock data
except ValidationError:
    print("Data validation failed")
    result = ApplyCorrectionLogic()  # Try to fix
except FileError:
    print("Cannot save file")
    result = ReturnDataInMemory()  # Keep in memory
```

**Result**: System is **resilient** - keeps working even if parts fail!

---

## 📈 SYSTEM METRICS

### Performance Metrics

```
With Ollama LLM (Real responses):
├─ Agent 1: 2-5 seconds
├─ Agent 2: 1-2 seconds
├─ Agent 3: 1-2 seconds
├─ Agent 4: 1-2 seconds
└─ Total: 5-10 seconds

With Mock Data (Fallback):
├─ Agent 1: <100ms
├─ Agent 2: <100ms
├─ Agent 3: <100ms
├─ Agent 4: <100ms
└─ Total: <500ms
```

### Quality Metrics

```
Quality Score Calculation:
├─ Itinerary completeness: 0-30 points
├─ Research depth: 0-20 points
├─ Cost accuracy: 0-30 points
└─ Overall validity: 0-20 points
Total: 0-100 points

Score Interpretation:
├─ 80-100: Excellent plan ✅
├─ 60-80: Good plan ✓
├─ 40-60: Fair plan (needs review) ⚠
└─ 0-40: Poor plan (not recommended) ❌
```

---

## 🎓 LEARNING SUMMARY

### What You've Learned:

1. **Multi-Agent Architecture**: Multiple specialized agents working together
2. **LLM Integration**: Using local Ollama for AI reasoning
3. **State Management**: Passing context between agents
4. **Tool Development**: Creating functions agents use
5. **Error Handling**: Graceful degradation when parts fail
6. **Testing**: Comprehensive test coverage
7. **Git/GitHub**: Team collaboration
8. **Python Best Practices**: Type hints, docstrings, error handling

### Key Concepts:

| Concept | What It Is | Why It Matters |
|---------|-----------|---|
| **Multi-Agent** | Multiple AIs with different roles | Solves complex problems better |
| **LLM** | Language model that generates text | Provides intelligent reasoning |
| **Ollama** | Local LLM server | Free, private, no API costs |
| **Orchestration** | Coordinating multiple components | Ensures smooth workflow |
| **State Management** | Passing data between agents | Preserves context |
| **Fallback** | Backup when primary fails | System resilience |
| **Tool** | Function agent uses | Extends agent capabilities |

---

## 🚀 Next Steps

Now that you understand how the system works:

1. **Read code in your assigned component**
   - Understand the logic
   - See how it integrates with others

2. **Modify your component**
   - Add features
   - Improve logic
   - Optimize performance

3. **Test thoroughly**
   - Write test cases
   - Verify your changes don't break others
   - Run full system end-to-end

4. **Document your changes**
   - Add comments
   - Update docstrings
   - Write in technical report

5. **Collaborate**
   - Push code to GitHub
   - Review team members' code
   - Discuss improvements

---

## 📞 Quick Reference

### What Does Each Agent Do?

```
Planner → Creates itinerary
Researcher → Adds cultural info
Estimator → Calculates costs
Validator → Checks quality & saves
```

### What Does Each Tool Do?

```
Cost Calculator → Calculates travel costs
Location Data → Retrieves destination info
Validation → Validates plan structure
File Saver → Saves to file
```

### How Does Ollama Help?

```
Provides intelligent responses instead of just using fixed data
Temperature/tokens control creativity and length
Falls back gracefully if server unavailable
```

### How Do Agents Coordinate?

```
Each agent receives complete data from previous agent
Adds its own contribution
Passes to next agent
Full state preserved throughout
```

---

**Ready to dive into the code? Start with your assigned component!** 🎯
