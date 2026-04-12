# 🤝 TEAM SETUP GUIDE - 4 Member Project

## Overview
This project has **4 team members**, each responsible for **1 Agent + 1 Tool + Testing**.

---

## 📋 Team Structure

| Member | Agent | Tool | Responsibility |
|--------|-------|------|-----------------|
| **Student 1** | Travel Planner | Cost Calculator | Itinerary generation |
| **Student 2** | Location Researcher | Location Data | Cultural insights |
| **Student 3** | Budget Estimator | Validation | Cost estimation |
| **Student 4** | Plan Validator | File Saver | Quality validation |

---

## 🚀 STEP 1: Clone Project (Everyone)

### 1.1 Choose a Team Member (Project Lead)
The **Project Lead** will set up the GitHub repository first.

### 1.2 Project Lead: Create GitHub Repository
```powershell
# Go to https://github.com/new
# Create repository named: ctse-travel-planner
# Add description: AI Travel Planner with 4 Agents using Ollama LLM
# Set to Public
# Copy the repository URL
```

### 1.3 Project Lead: Push Code to GitHub
```powershell
# In your local folder (d:\CTSE\ctse2)
cd D:\CTSE\ctse2

git init
git add .
git commit -m "Initial commit: AI Travel Planner MAS with Ollama LLM integration"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ctse-travel-planner.git
git push -u origin main

# Share the repository URL with your team
# Example: https://github.com/yourname/ctse-travel-planner
```

### 1.4 All Other Members: Clone the Project
```powershell
# Each team member runs this command
# Replace USERNAME and REPO with actual values

cd C:\Users\YourUsername\Documents  # or preferred location

git clone https://github.com/USERNAME/ctse-travel-planner.git

cd ctse-travel-planner

# Verify it cloned successfully
dir /s agents  # Should see: planner.py, researcher.py, estimator.py, validator.py
```

---

## ⚙️ STEP 2: Set Up Environment (Each Member Independently)

### 2.1 Install Python Dependencies
```powershell
# From inside the project folder
cd ctse-travel-planner

# Install packages
pip install -r requirements.txt

# Verify installation
pip list | findstr streamlit

# You should see: streamlit, pandas, pytest, requests
```

### 2.2 Verify Project Structure
```powershell
# Check all folders exist
ls agents\       # Should see: planner.py, researcher.py, estimator.py, validator.py
ls tools\        # Should see: cost_calculator_tool.py, location_data_tool.py, validation_tool.py, file_saver_tool.py
ls tests\        # Should see: test_tools.py
ls logs\         # May be empty initially

# Create logs folder if missing
mkdir logs
```

### 2.3 Verify Installation
```powershell
# Run verification script
python setup_check.py

# You should see all ✓ (except Ollama checks if not set up yet)
```

---

## 🔌 STEP 3: Set Up Ollama (Everyone)

### 3.1 Download & Install Ollama
1. Go to: https://ollama.ai
2. Download Ollama for Windows
3. Run the installer
4. Follow installation wizard

### 3.2 Verify Installation
```powershell
# Should show version number
ollama --version

# Output: ollama version 0.X.X
```

### 3.3 Pull the Model (15-30 minutes first time)
```powershell
# Download llama3:8b model
ollama pull llama3:8b

# This downloads ~4.7GB
# Be patient - will take 5-15 minutes depending on internet
```

---

## 🎯 STEP 4: Run the System (Test Together)

### 4.1 Start Ollama Server (Terminal 1)

**Person 1 (Any member) - Opens Terminal/PowerShell:**
```powershell
cd d:\CTSE\ctse2  # or your project location

# Start Ollama server - KEEP THIS RUNNING
ollama serve

# You should see:
# API server running on 127.0.0.1:11434
```

### 4.2 Run System (Terminal 2, Different Person)

**Person 2 (Any member) - Opens NEW Terminal/PowerShell:**
```powershell
cd d:\CTSE\ctse2  # or your project location

# Run the system
python main.py

# You should see:
# ✓ Ollama LLM initialized
# Generating travel plan for Ella...
# ✓ Plan generated successfully!
```

### 4.3 View Output
```powershell
# Open the generated file
notepad output.txt

# You should see a complete travel plan with:
# - Itinerary (from Agent 1)
# - Cultural insights (from Agent 2)
# - Cost breakdown (from Agent 3)
# - Validation score (from Agent 4)
```

---

## 👨‍💼 STEP 5: Each Member's Responsibility

### Student 1: Travel Planner Agent + Cost Calculator Tool

**Files to work with:**
- `agents/planner.py` - Travel Planner Agent
- `tools/cost_calculator_tool.py` - Cost Calculator Tool
- `tests/test_tools.py` - Test cases

**What to do:**
1. Review the agent code in `agents/planner.py`
2. Understand how it generates itineraries
3. Review the cost calculator in `tools/cost_calculator_tool.py`
4. Add/modify test cases in `tests/test_tools.py` (TestCostCalculator class)
5. Document your work in the technical report

**Key files:**
```
agents/planner.py              ← Your main agent
tools/cost_calculator_tool.py  ← Your main tool
tests/test_tools.py            ← Add your tests (class TestCostCalculator)
```

---

### Student 2: Location Researcher Agent + Location Data Tool

**Files to work with:**
- `agents/researcher.py` - Location Researcher Agent
- `tools/location_data_tool.py` - Location Data Tool
- `tests/test_tools.py` - Test cases

**What to do:**
1. Review the agent code in `agents/researcher.py`
2. Understand how it researches destinations
3. Review the location data tool in `tools/location_data_tool.py`
4. Add/modify test cases in `tests/test_tools.py` (TestLocationDataTool class)
5. Document your work in the technical report

**Key files:**
```
agents/researcher.py           ← Your main agent
tools/location_data_tool.py    ← Your main tool
tests/test_tools.py            ← Add your tests (class TestLocationDataTool)
```

---

### Student 3: Budget Estimator Agent + Validation Tool

**Files to work with:**
- `agents/estimator.py` - Budget Estimator Agent
- `tools/validation_tool.py` - Validation Tool
- `tests/test_tools.py` - Test cases

**What to do:**
1. Review the agent code in `agents/estimator.py`
2. Understand how it estimates costs
3. Review the validation tool in `tools/validation_tool.py`
4. Add/modify test cases in `tests/test_tools.py` (TestValidationTool class)
5. Document your work in the technical report

**Key files:**
```
agents/estimator.py            ← Your main agent
tools/validation_tool.py       ← Your main tool
tests/test_tools.py            ← Add your tests (class TestValidationTool)
```

---

### Student 4: Plan Validator Agent + File Saver Tool

**Files to work with:**
- `agents/validator.py` - Plan Validator Agent
- `tools/file_saver_tool.py` - File Saver Tool
- `tests/test_tools.py` - Test cases

**What to do:**
1. Review the agent code in `agents/validator.py`
2. Understand how it validates plans
3. Review the file saver tool in `tools/file_saver_tool.py`
4. Add/modify test cases in `tests/test_tools.py` (TestFileOperations class)
5. Document your work in the technical report

**Key files:**
```
agents/validator.py            ← Your main agent
tools/file_saver_tool.py       ← Your main tool
tests/test_tools.py            ← Add your tests (class TestFileOperations)
```

---

## 🧪 STEP 6: Run Tests (Everyone)

### 6.1 Run All Tests
```powershell
cd d:\CTSE\ctse2  # or your project location

# Run all tests
pytest tests/test_tools.py -v

# Output should show:
# test_calculate_cost_basic PASSED
# test_get_location_data PASSED
# ... (36+ tests)
```

### 6.2 Run Specific Test for Your Component
```powershell
# Student 1
pytest tests/test_tools.py::TestCostCalculator -v

# Student 2
pytest tests/test_tools.py::TestLocationDataTool -v

# Student 3
pytest tests/test_tools.py::TestValidationTool -v

# Student 4
pytest tests/test_tools.py::TestFileOperations -v
```

---

## 📚 STEP 7: Understanding the Code Flow

### Data Flow Through the System

```
1. User provides: destination, days, budget
                    ↓
2. Agent 1 (Student 1) - Travel Planner
   ├─ Uses Tool 1: Cost Calculator
   └─ Output: Detailed itinerary
                    ↓
3. Agent 2 (Student 2) - Location Researcher
   ├─ Uses Tool 2: Location Data
   └─ Output: Itinerary + cultural insights
                    ↓
4. Agent 3 (Student 3) - Budget Estimator
   ├─ Uses Tool 3: Validation
   └─ Output: Plan + cost breakdown
                    ↓
5. Agent 4 (Student 4) - Plan Validator
   ├─ Uses Tool 4: File Saver
   └─ Output: Final validated plan + saved to file
                    ↓
6. File: output.txt saved with complete travel plan
```

---

## 📝 STEP 8: Reading Your Component Code

### Example: Student 1 Understanding Their Agent

**File**: `agents/planner.py`

```python
class TravelPlannerAgent:
    """
    Travel Planner creates detailed travel itineraries.
    
    This agent is responsible for:
    - Creating day-by-day schedules
    - Suggesting activities
    - Recommending restaurants and hotels
    """
    
    def __init__(self, use_ollama: bool = True):
        """Initialize the Travel Planner Agent."""
        self.use_ollama = use_ollama
        # ... initialization code
    
    def create_itinerary(self, destination: str, num_days: int, preferences: str):
        """
        Create a travel itinerary.
        
        Args:
            destination: Where to travel (e.g., "Ella")
            num_days: Duration in days
            preferences: Travel style (e.g., "adventure", "relaxation")
        
        Returns:
            dict: Complete itinerary
        """
        # This is where your agent does its work
        # It either:
        # 1. Uses Ollama LLM if available
        # 2. Uses mock data as fallback
```

**How to read it:**
1. Understand the class structure
2. Read the docstrings ("""...""")
3. Look at the method parameters
4. See what it returns
5. Understand the flow

---

## 🔧 STEP 9: Making Changes & Testing

### 9.1 Edit Your Component
```python
# Example: Student 1 modifies cost calculator

# File: tools/cost_calculator_tool.py

def calculate_travel_cost(destination, num_days, accommodation_type):
    """Calculate travel costs."""
    
    # MODIFY THIS SECTION:
    costs = {
        "accommodation": num_days * 100,  # Your change
        "meals": num_days * 50,           # Your change
        "transport": 200,
        "activities": 300,
    }
    
    return costs
```

### 9.2 Test Your Changes
```powershell
# Run your specific tests
pytest tests/test_tools.py::TestCostCalculator -v

# Should see: PASSED
```

### 9.3 Run Full System to Verify
```powershell
# Terminal 1 (if not running)
ollama serve

# Terminal 2
python main.py

# Check if output looks correct
notepad output.txt
```

---

## 💾 STEP 10: Commit & Push Changes

### 10.1 After Making Changes
```powershell
# See what changed
git status

# Add your changes
git add .

# Commit with meaningful message
git commit -m "Student 1: Enhanced cost calculator for better accuracy"

# Push to GitHub
git push origin main
```

### 10.2 Pull Latest Changes (Before Starting Work)
```powershell
# Always start by getting latest code
git pull origin main

# Now you're up to date with team changes
```

---

## 🐛 STEP 11: Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'streamlit'"
**Solution:**
```powershell
pip install -r requirements.txt
```

### Problem: "Cannot connect to Ollama at localhost:11434"
**Solution:**
```powershell
# Make sure Ollama is running
# Terminal 1: ollama serve
# Should see: API server running on 127.0.0.1:11434

# If not running, start it
ollama serve
```

### Problem: "AttributeError: 'NoneType' object has no attribute..."
**Solution:**
```powershell
# Make sure you have the model downloaded
ollama pull llama3:8b

# Restart Ollama
# Stop: Press Ctrl+C in ollama serve terminal
# Restart: ollama serve
```

### Problem: Tests failing
**Solution:**
```powershell
# Run tests with verbose output
pytest tests/test_tools.py -v

# See which test failed
# Review that test code
# Fix the issue in your agent/tool
# Re-run test
```

---

## 📋 STEP 12: Collaboration Workflow

### Daily Workflow Example

**9:00 AM - Start of day:**
```powershell
# Get latest code from team
git pull origin main

# Run verification
python setup_check.py

# Work on your component
# ... make code changes ...
```

**During day:**
```powershell
# Test your changes
pytest tests/test_tools.py::TestYourComponent -v

# Run full system
python main.py
```

**End of day:**
```powershell
# See what you changed
git status

# Add changes
git add .

# Commit with message
git commit -m "Student X: Added feature XYZ"

# Push to team
git push origin main
```

**Next morning:**
```powershell
# Get team's changes
git pull origin main

# Continue working...
```

---

## ✅ Quick Checklist

After setup, verify everything works:

```
[ ] All 4 members cloned the project
[ ] All members installed requirements.txt
[ ] Ollama downloaded and installed
[ ] llama3:8b model downloaded (ollama pull llama3:8b)
[ ] Ollama server runs (ollama serve)
[ ] python main.py completes successfully
[ ] output.txt generated with complete plan
[ ] pytest tests/test_tools.py passes all tests
[ ] Each member understands their agent
[ ] GitHub repository created and shared
[ ] All members can git pull/push
```

---

## 📞 Quick Commands Reference

```powershell
# Clone project
git clone https://github.com/USERNAME/ctse-travel-planner.git

# Install packages
pip install -r requirements.txt

# Start Ollama (Terminal 1)
ollama serve

# Pull model
ollama pull llama3:8b

# Run system (Terminal 2)
python main.py

# Test your component
pytest tests/test_tools.py::TestYourComponent -v

# Check what changed
git status

# Save your work
git add .
git commit -m "Your message"
git push origin main

# Get team's changes
git pull origin main

# Verify setup
python setup_check.py
```

---

## 📚 File Location Reference

```
project-root/
├── agents/
│   ├── planner.py              ← Student 1
│   ├── researcher.py           ← Student 2
│   ├── estimator.py            ← Student 3
│   └── validator.py            ← Student 4
│
├── tools/
│   ├── cost_calculator_tool.py ← Student 1
│   ├── location_data_tool.py   ← Student 2
│   ├── validation_tool.py      ← Student 3
│   └── file_saver_tool.py      ← Student 4
│
├── tests/
│   └── test_tools.py           ← All students add tests here
│
├── logs/
│   └── log.txt                 ← Auto-generated logs
│
├── main.py                     ← Main orchestrator (don't touch)
├── app.py                      ← Web UI (don't touch)
├── ollama_client.py            ← Ollama integration (don't touch)
├── requirements.txt            ← Python packages
├── README.md                   ← Project overview
└── setup_check.py              ← Verification script
```

---

## 🎯 Summary

**For Project Lead:**
1. Create GitHub repository
2. Push initial code
3. Share link with team

**For All Team Members:**
1. Clone project: `git clone [URL]`
2. Install: `pip install -r requirements.txt`
3. Install Ollama + model
4. Test: `python main.py`
5. Work on your assigned agent/tool
6. Add tests
7. Commit and push: `git push origin main`

**Each student's work:**
- Student 1: agents/planner.py + tools/cost_calculator_tool.py
- Student 2: agents/researcher.py + tools/location_data_tool.py
- Student 3: agents/estimator.py + tools/validation_tool.py
- Student 4: agents/validator.py + tools/file_saver_tool.py

**Collaboration:**
- Clone → Update → Code → Test → Push → Repeat

**All together:**
- Create demo video
- Write technical report
- Submit on GitHub

---

## Need Help?

Run: `python setup_check.py` to verify everything is set up correctly.

All 4 of you should see ✓ marks for:
- ✓ Python version
- ✓ Required packages
- ✓ Project structure
- ✓ Ollama server
- ✓ llama3:8b model
- ✓ Ollama client connected
