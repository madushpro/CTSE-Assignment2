# 🧪 SYSTEM TESTING GUIDE - Complete Testing Strategy

## 📋 Testing Overview

### Types of Testing

```
1. SETUP VERIFICATION
   └─ Check all dependencies installed
   └─ Verify project structure
   └─ Confirm Ollama connection

2. UNIT TESTING
   └─ Test individual functions/tools
   └─ 36+ automated test cases
   └─ Run with pytest

3. INTEGRATION TESTING
   └─ Test agents working together
   └─ Test full pipeline
   └─ Manual end-to-end test

4. PERFORMANCE TESTING
   └─ Measure execution time
   └─ Check response quality
   └─ Verify resource usage

5. ERROR HANDLING TESTING
   └─ Test system without Ollama
   └─ Test with invalid input
   └─ Test edge cases
```

---

## ✅ QUICK TEST CHECKLIST (5 minutes)

### Test 1: Verify Setup
```powershell
cd d:\CTSE\ctse2

python setup_check.py

# Expected output:
# ✓ Python version: 3.14
# ✓ streamlit, pandas, pytest, requests all installed
# ✓ Directory structure complete
# ✓ All required files present
```

### Test 2: Check Ollama Status
```powershell
ollama --version
# Should show: ollama version X.X.X

# If not installed, install from https://ollama.ai
```

### Test 3: Start Ollama Server
```powershell
# Terminal 1 - START OLLAMA
ollama serve

# Should show:
# 2026/04/12 12:45:00 models path ...
# 2026/04/12 12:45:00 API server running on 127.0.0.1:11434
```

### Test 4: Run System
```powershell
# Terminal 2 - RUN SYSTEM
cd d:\CTSE\ctse2

python main.py

# When prompted:
# Enter destination: Ella
# Enter number of days: 3
# Enter budget (Rs.): 20000

# Expected result:
# ✓ Plan generated successfully!
# ✓ Plan saved to output.txt
```

### Test 5: Verify Output
```powershell
notepad output.txt

# Should contain:
# - Itinerary (from Agent 1)
# - Cultural insights (from Agent 2)
# - Cost breakdown (from Agent 3)
# - Validation score (from Agent 4)
```

---

## 🔍 DETAILED TESTING PROCEDURES

### PHASE 1: DEPENDENCY VERIFICATION (5 minutes)

#### Step 1.1: Python Version Check
```powershell
python --version
# Expected: Python 3.8 or higher
```

#### Step 1.2: Required Packages Check
```powershell
# Check each package
pip show streamlit
pip show pandas
pip show pytest
pip show requests

# All should show "Name: ..." indicating installed
```

#### Step 1.3: Run Automated Setup Check
```powershell
cd d:\CTSE\ctse2

python setup_check.py

# This will verify:
# ✓ Python version
# ✓ All packages installed
# ✓ Project directories exist
# ✓ All required files present
# ✓ Ollama server availability
# ✓ llama3:8b model status
# ✓ Ollama client connection
```

---

### PHASE 2: UNIT TESTING (10 minutes)

#### Step 2.1: Run ALL Tests
```powershell
cd d:\CTSE\ctse2

pytest tests/test_tools.py -v

# Output shows:
# test_calculate_cost_basic PASSED
# test_calculate_cost_luxury PASSED
# ... (36+ tests)
# ============= 36 passed in 2.34s =============
```

#### Step 2.2: Run Tests by Component

**Student 1 Tests (Cost Calculator):**
```powershell
pytest tests/test_tools.py::TestCostCalculator -v

# Expected: 10 tests pass
# Coverage: calculate_travel_cost function
```

**Student 2 Tests (Location Data):**
```powershell
pytest tests/test_tools.py::TestLocationDataTool -v

# Expected: 6 tests pass
# Coverage: get_location_data function
```

**Student 3 Tests (Validation):**
```powershell
pytest tests/test_tools.py::TestValidationTool -v

# Expected: 4 tests pass
# Coverage: validate_plan_structure function
```

**Student 4 Tests (File Operations):**
```powershell
pytest tests/test_tools.py::TestFileOperations -v

# Expected: 6 tests pass
# Coverage: save_travel_plan function
```

#### Step 2.3: Check Test Coverage
```powershell
pytest tests/test_tools.py --cov=tools --cov=agents --cov-report=term-missing

# Shows which lines of code are tested
# Goal: 80%+ coverage
```

#### Step 2.4: Run Tests in Quiet Mode
```powershell
pytest tests/test_tools.py -q

# Output: Shows pass/fail summary
# Example: 36 passed in 2.34s
```

---

### PHASE 3: INTEGRATION TESTING (15 minutes)

#### Step 3.1: Start Ollama (Terminal 1)
```powershell
ollama serve

# Keep this running in background
# Terminal shows: API server running on 127.0.0.1:11434
```

#### Step 3.2: Test 1 - Ella (3 days, Budget Plan)
```powershell
# Terminal 2
cd d:\CTSE\ctse2

python main.py

# INPUT:
# Destination: Ella
# Days: 3
# Budget: 20000

# EXPECTED OUTPUT:
# ✓ Plan generated successfully!
# Status: ✅ EXCELLENT (or similar)
# Estimated Cost: Rs. 2,000-5,000
# Quality Score: 70-100/100
# ✓ Plan saved to output.txt
```

#### Step 3.3: Test 2 - Colombo (5 days, Luxury Travel)
```powershell
# Terminal 2
python main.py

# INPUT:
# Destination: Colombo
# Days: 5
# Budget: 50000

# EXPECTED OUTPUT:
# Different itinerary from Test 1
# Higher costs (more activities)
# Quality score similar or higher
```

#### Step 3.4: Test 3 - Galle (2 days, Budget Travel)
```powershell
# Terminal 2
python main.py

# INPUT:
# Destination: Galle
# Days: 2
# Budget: 8000

# EXPECTED OUTPUT:
# Shorter itinerary (2 days)
# Lower costs
# May show "BUDGET CONSTRAINT" status
```

#### Step 3.5: Verify All 4 Agents Worked
Check the logs:
```powershell
# Look for these log entries:
# [TIME] [AGENT 1] Travel Planner: Creating itinerary
# [TIME] [AGENT 2] Location Research: Finding destination info
# [TIME] [AGENT 3] Budget Estimator: Calculating costs
# [TIME] [AGENT 4] Plan Validator: Validating and scoring

# All should say: "created successfully" or similar
```

#### Step 3.6: Verify Output File Content
```powershell
notepad output.txt

# Should contain:
# 1. ITINERARY (from Agent 1)
#    Day 1: ...
#    Day 2: ...
#
# 2. CULTURAL INSIGHTS (from Agent 2)
#    Information about destination
#
# 3. COST BREAKDOWN (from Agent 3)
#    Accommodation, Meals, Transport, Activities
#    TOTAL: Rs. XXX
#
# 4. QUALITY SCORE (from Agent 4)
#    Score: XX/100
#    Status: ✅ or ⚠
```

---

### PHASE 4: ERROR HANDLING TESTING (10 minutes)

#### Test 4.1: System Without Ollama
```powershell
# Terminal 1 - STOP OLLAMA
# Ctrl+C in the ollama serve window

# Terminal 2 - RUN SYSTEM
python main.py

# INPUT: Ella, 3, 20000

# EXPECTED BEHAVIOR:
# Should still work!
# Log shows: "Ollama unavailable, using mock data"
# Plan generated with mock data
# All agents still complete
# Output file still created
```

#### Test 4.2: Invalid Destination
```powershell
python main.py

# INPUT: 
# Destination: ValidPlace (not in database)
# Days: 3
# Budget: 20000

# EXPECTED BEHAVIOR:
# Should either:
# A) Return generic plan for unknown location
# B) Use nearest matching location
# C) Show error but handle gracefully
```

#### Test 4.3: Invalid Number of Days
```powershell
python main.py

# INPUT:
# Destination: Ella
# Days: 50 (exceeds max)
# Budget: 20000

# EXPECTED BEHAVIOR:
# Should reject with error message
# Ask user to input valid number (1-30)
# Don't crash
```

#### Test 4.4: Invalid Budget
```powershell
python main.py

# INPUT:
# Destination: Ella
# Days: 3
# Budget: -5000 (negative)

# EXPECTED BEHAVIOR:
# Should reject with error
# Ask for positive number
# Don't crash
```

#### Test 4.5: Budget Way Too Low
```powershell
python main.py

# INPUT:
# Destination: Ella
# Days: 5
# Budget: 1000 (unrealistic)

# EXPECTED BEHAVIOR:
# Should still generate plan
# Show warning: "BUDGET EXCEEDED"
# Recommend alternatives
# Complete successfully
```

---

### PHASE 5: PERFORMANCE TESTING (5 minutes)

#### Test 5.1: Response Time with Ollama
```powershell
# Terminal 1 - START OLLAMA
ollama serve

# Terminal 2 - RUN AND TIME SYSTEM
# Use system clock to time:
# [Start time]: python main.py
# [End time]: when output.txt created

# EXPECTED:
# Total time: 5-10 seconds
# Agent 1: 2-5 seconds
# Agent 2: 1-2 seconds
# Agent 3: 1-2 seconds
# Agent 4: 1-2 seconds
```

#### Test 5.2: Response Time with Mock Data
```powershell
# Terminal 1 - KEEP OLLAMA STOPPED

# Terminal 2 - RUN SYSTEM
# Time the execution

# EXPECTED:
# Total time: <500ms
# Much faster than with LLM
```

#### Test 5.3: Output File Size
```powershell
# Check file size
dir output.txt

# EXPECTED:
# Size: 1-5 KB
# Should be reasonable text file
```

---

### PHASE 6: LOGGING VERIFICATION (5 minutes)

#### Test 6.1: Check Logs
```powershell
notepad logs/log.txt

# Should contain:
# [2026-04-12 HH:MM:SS] AI Travel Planner MAS initialized
# [2026-04-12 HH:MM:SS] User Input: Destination=..., Days=..., Budget=...
# [2026-04-12 HH:MM:SS] Input validation: PASSED
# [2026-04-12 HH:MM:SS] [AGENT 1] Travel Planner: Creating itinerary
# [2026-04-12 HH:MM:SS] [AGENT 1] Travel Planner: Itinerary created
# [2026-04-12 HH:MM:SS] [AGENT 2] Location Research: Researching destination
# [2026-04-12 HH:MM:SS] [AGENT 2] Location Research: Plan enhanced
# [2026-04-12 HH:MM:SS] [AGENT 3] Budget Estimator: Calculating costs
# [2026-04-12 HH:MM:SS] [AGENT 3] Budget Estimator: Estimated cost
# [2026-04-12 HH:MM:SS] [AGENT 4] Plan Validator: Validating plan
# [2026-04-12 HH:MM:SS] [AGENT 4] Plan Validator: Validation complete
# [2026-04-12 HH:MM:SS] ✓ Travel plan generation COMPLETE
```

#### Test 6.2: Verify Timestamps
```powershell
# All entries should have:
# [YYYY-MM-DD HH:MM:SS] format
# Timestamps should progress chronologically
# Gaps show where time was spent
```

---

## 🎯 MANUAL END-TO-END TEST (10 minutes)

### Complete Test Scenario

**Setup:**
```powershell
# Terminal 1
ollama serve

# Wait for: API server running on 127.0.0.1:11434
```

**Test Execution:**
```powershell
# Terminal 2
cd d:\CTSE\ctse2

# Clear old output
del output.txt

# Run system
python main.py

# Enter inputs (copy-paste):
# Destination: Ella
# Days: 3
# Budget: 20000

# Press Enter after each
```

**Expected Results:**

```
✓ Plan generated successfully!
Status: ⚠ REVIEW NEEDED (or similar)
Estimated Cost: Rs. 2,000-3,000
Quality Score: 70-80/100

✓ Plan saved to D:\CTSE\ctse2\output.txt

Execution Logs:
[2026-04-12 HH:MM:SS] AI Travel Planner MAS initialized
[2026-04-12 HH:MM:SS] ✓ Ollama LLM support ENABLED
[2026-04-12 HH:MM:SS] User Input: Destination=Ella, Days=3, Budget=Rs.20000
[2026-04-12 HH:MM:SS] Input validation: PASSED
[2026-04-12 HH:MM:SS] [AGENT 1] Travel Planner: Creating 3-day itinerary for Ella
[2026-04-12 HH:MM:SS] [AGENT 1] Travel Planner: Itinerary created successfully
[2026-04-12 HH:MM:SS] [AGENT 2] Location Research: Researching Ella
[2026-04-12 HH:MM:SS] [AGENT 2] Location Research: Plan enhanced with cultural insights
[2026-04-12 HH:MM:SS] [AGENT 3] Budget Estimator: Calculating costs for 3 days
[2026-04-12 HH:MM:SS] [AGENT 3] Budget Estimator: Estimated cost Rs. 2,000
[2026-04-12 HH:MM:SS] [AGENT 4] Plan Validator: Validating complete plan
[2026-04-12 HH:MM:SS] [AGENT 4] Plan Validator: Validation complete. Score: 75.0/100
[2026-04-12 HH:MM:SS] ✓ Travel plan generation COMPLETE
[2026-04-12 HH:MM:SS] Plan saved to output.txt
```

**Verify Output File:**
```powershell
notepad output.txt

# Should show:
# - Complete itinerary with 3 days
# - Specific activities for Ella
# - Hotel recommendations
# - Restaurant suggestions
# - Cultural information
# - Cost breakdown: Accommodation, Meals, Transport, Activities
# - TOTAL cost calculated
# - Quality score and validation feedback
```

---

## 📊 TEST RESULTS TRACKING

### Results Table Template

```
TEST NAME          | EXPECTED      | ACTUAL      | STATUS | NOTES
──────────────────────────────────────────────────────────────────
Setup Check        | All ✓         | ?           | ?      | Run setup_check.py
Packages           | streamlit, ✓  | ?           | ?      | pip list
Unit Tests         | 36 passed     | ?           | ?      | pytest -v
Ollama Connection  | Connected ✓   | ?           | ?      | ollama serve
Test 1: Ella 3d    | Plan + file   | ?           | ?      | Check output.txt
Test 2: Colombo 5d | Plan + file   | ?           | ?      | Check output.txt  
Test 3: Galle 2d   | Plan + file   | ?           | ?      | Check output.txt
No Ollama Test     | Works anyway  | ?           | ?      | Stop Ollama, run
Invalid Input Test | Rejects bad   | ?           | ?      | Try days=50
All Logs Present   | 12+ entries   | ?           | ?      | Check log.txt
Performance        | <10 sec       | ?           | ?      | Time execution
```

---

## ✅ COMPLETE TEST CHECKLIST

### Before Testing
```
[ ] Python 3.8+ installed
[ ] All packages installed (pip install -r requirements.txt)
[ ] Project folder accessible (d:\CTSE\ctse2)
[ ] Ollama downloaded and installed
[ ] llama3:8b model downloaded (ollama pull llama3:8b)
[ ] All files present (agents/, tools/, tests/, etc.)
```

### During Testing
```
[ ] Run setup_check.py - all ✓
[ ] Run pytest - 36 tests pass
[ ] Start ollama serve - API ready
[ ] Run main.py - Plan generates
[ ] Check output.txt - Contains full plan
[ ] Verify logs - 12+ entries
[ ] Test without Ollama - Still works
[ ] Test invalid input - Rejects properly
```

### After Testing
```
[ ] All test passes recorded
[ ] No errors or crashes
[ ] Output quality acceptable
[ ] Performance meets expectations
[ ] Ready for demo video
[ ] Ready for submission
```

---

## 🐛 TROUBLESHOOTING TEST FAILURES

### Problem: "ModuleNotFoundError: No module named 'streamlit'"

**Solution:**
```powershell
pip install -r requirements.txt

# Or install individually:
pip install streamlit pandas pytest requests
```

### Problem: "Cannot connect to Ollama at localhost:11434"

**Solution:**
```powershell
# Make sure Ollama is running
# Terminal 1: ollama serve
# Then try again in Terminal 2

# If still fails:
ollama pull llama3:8b  # Download model
ollama serve           # Start server
```

### Problem: Tests failing with "AssertionError"

**Solution:**
```powershell
# Run specific failing test with more detail
pytest tests/test_tools.py::TestName::test_method -vvv

# Check the assertion that failed
# Review the function being tested
# Fix the logic if needed
```

### Problem: "output.txt not created"

**Solution:**
```powershell
# Make sure logs/ folder exists
mkdir logs

# Check file permissions
# File should be writable in project directory

# Try running as administrator
```

### Problem: System hangs when running

**Solution:**
```powershell
# Press Ctrl+C to stop
# Try running with timeout:
python -u main.py  # Unbuffered output

# Check if Ollama response is slow
# Try with mock data (stop Ollama)
```

---

## 📝 QUICK TEST SCRIPT

Copy this into a file named `quick_test.ps1`:

```powershell
# Quick Test Script for Windows PowerShell

Write-Host "🧪 SYSTEM TEST SUITE" -ForegroundColor Green
Write-Host ""

# Test 1: Setup
Write-Host "1️⃣ Running setup check..." -ForegroundColor Cyan
python setup_check.py
Write-Host ""

# Test 2: Unit Tests
Write-Host "2️⃣ Running unit tests..." -ForegroundColor Cyan
pytest tests/test_tools.py -q
Write-Host ""

# Test 3: Full System (requires Ollama)
Write-Host "3️⃣ Make sure Ollama is running in Terminal 1!"
Write-Host "   Run: ollama serve" -ForegroundColor Yellow
Read-Host "Press Enter when ready..."

Write-Host ""
Write-Host "Running end-to-end test..." -ForegroundColor Cyan

# Create test input
$testInput = @"
Ella
3
20000
"@

# Run test
$testInput | python main.py

# Verify output
if (Test-Path "output.txt") {
    Write-Host "✓ output.txt created" -ForegroundColor Green
    Get-Content output.txt | Select-Object -First 10
} else {
    Write-Host "✗ output.txt not found" -ForegroundColor Red
}

Write-Host ""
Write-Host "✅ Test suite complete!" -ForegroundColor Green
```

Run it:
```powershell
.\quick_test.ps1
```

---

## 🎯 SUCCESS CRITERIA

### System is working properly if:

```
✅ setup_check.py shows all ✓ marks
✅ All 36 pytest tests pass
✅ main.py runs without crashes
✅ output.txt is created with content
✅ All 4 agents log their actions
✅ Quality scores are 60-100
✅ Costs are calculated correctly
✅ System works without Ollama (mock data)
✅ Invalid input is rejected gracefully
✅ Performance is <10 seconds with LLM
✅ Logs are comprehensive and detailed
```

### System is NOT working if:

```
❌ setup_check.py shows ✗ marks
❌ Tests fail with errors
❌ main.py crashes
❌ output.txt not created
❌ No log entries
❌ Quality scores 0 or irrelevant
❌ Costs unrealistic or 0
❌ System crashes without Ollama
❌ Invalid input crashes system
❌ Hangs or takes >30 seconds
❌ Logs missing or empty
```

---

## 🚀 READY TO TEST?

### Next Steps:

1. **Verify Setup** - Run `python setup_check.py`
2. **Run Unit Tests** - Run `pytest tests/test_tools.py -v`
3. **Start Ollama** - Terminal 1: `ollama serve`
4. **Run System** - Terminal 2: `python main.py`
5. **Check Output** - View `output.txt`
6. **Review Logs** - View `logs/log.txt`
7. **Test Without Ollama** - Stop server, run again
8. **Test Invalid Input** - Try bad inputs

---

**Your system is ready for comprehensive testing!** 🧪✅
