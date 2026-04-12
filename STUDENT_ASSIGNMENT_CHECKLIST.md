# 📋 Student Assignment Checklist - Who Does What

---

## 👤 STUDENT 1: Travel Planner Developer

### Assigned Component
- **Agent**: `agents/planner.py` - Travel Planner Agent
- **Tool**: `tools/cost_calculator_tool.py` - Cost Calculator Tool
- **Tests**: `tests/test_tools.py` → `TestCostCalculator` class

### Your Responsibilities

#### 1. Code Review & Understanding (Day 1)
- [ ] Read `agents/planner.py` completely
- [ ] Read `tools/cost_calculator_tool.py` completely
- [ ] Understand how they work together
- [ ] Read corresponding test cases in `TestCostCalculator`

#### 2. Modifications (Days 2-3)
Choose ONE of these to enhance:
- [ ] **Option A**: Improve itinerary generation logic
  - Add more destination support
  - Add more varied daily activities
  - Add better recommendations
  
- [ ] **Option B**: Improve cost calculator
  - Add seasonal pricing variations
  - Add different accommodation types
  - Add activity cost estimates
  
- [ ] **Option C**: Enhance both

#### 3. Testing (Day 4)
- [ ] Add 3-5 new test cases to `TestCostCalculator`
- [ ] Test edge cases (0 days, very high budget, etc.)
- [ ] Ensure all tests pass: `pytest tests/test_tools.py::TestCostCalculator -v`

#### 4. Documentation (Day 5)
- [ ] Write section in technical report:
  - **Title**: "Agent 1: Travel Planner & Cost Calculator"
  - **Content**: 
    - What my agent does
    - What my tool does
    - What changes I made
    - What tests I added
    - Challenges I faced

#### 5. Final Submission
- [ ] Commit code: `git add . && git commit -m "Student 1: Travel Planner enhancements"`
- [ ] Push to GitHub: `git push origin main`
- [ ] Add section to technical report

---

## 👤 STUDENT 2: Location Researcher Developer

### Assigned Component
- **Agent**: `agents/researcher.py` - Location Researcher Agent
- **Tool**: `tools/location_data_tool.py` - Location Data Tool
- **Tests**: `tests/test_tools.py` → `TestLocationDataTool` class

### Your Responsibilities

#### 1. Code Review & Understanding (Day 1)
- [ ] Read `agents/researcher.py` completely
- [ ] Read `tools/location_data_tool.py` completely
- [ ] Understand how they enhance the itinerary
- [ ] Read corresponding test cases in `TestLocationDataTool`

#### 2. Modifications (Days 2-3)
Choose ONE of these to enhance:
- [ ] **Option A**: Add more destinations
  - Add 3-5 new Sri Lankan locations
  - Add cultural information for each
  - Add local tips and recommendations
  
- [ ] **Option B**: Enhance data structure
  - Add weather information
  - Add best time to visit
  - Add local contact info
  
- [ ] **Option C**: Enhance both

#### 3. Testing (Day 4)
- [ ] Add 3-5 new test cases to `TestLocationDataTool`
- [ ] Test retrieval of different locations
- [ ] Test data completeness
- [ ] Ensure all tests pass: `pytest tests/test_tools.py::TestLocationDataTool -v`

#### 4. Documentation (Day 5)
- [ ] Write section in technical report:
  - **Title**: "Agent 2: Location Researcher & Location Data Tool"
  - **Content**:
    - What my agent does
    - What my tool does
    - Locations I added
    - Changes I made
    - Tests I added
    - Challenges I faced

#### 5. Final Submission
- [ ] Commit code: `git add . && git commit -m "Student 2: Location research enhancements"`
- [ ] Push to GitHub: `git push origin main`
- [ ] Add section to technical report

---

## 👤 STUDENT 3: Budget Estimator Developer

### Assigned Component
- **Agent**: `agents/estimator.py` - Budget Estimator Agent
- **Tool**: `tools/validation_tool.py` - Validation Tool
- **Tests**: `tests/test_tools.py` → `TestValidationTool` class

### Your Responsibilities

#### 1. Code Review & Understanding (Day 1)
- [ ] Read `agents/estimator.py` completely
- [ ] Read `tools/validation_tool.py` completely
- [ ] Understand how costs are calculated and validated
- [ ] Read corresponding test cases in `TestValidationTool`

#### 2. Modifications (Days 2-3)
Choose ONE of these to enhance:
- [ ] **Option A**: Improve cost estimation
  - Add inflation factors by region
  - Add group discount calculations
  - Add detailed cost breakdown
  
- [ ] **Option B**: Enhance validation logic
  - Add more validation rules
  - Add budget compatibility checks
  - Add feasibility analysis
  
- [ ] **Option C**: Enhance both

#### 3. Testing (Day 4)
- [ ] Add 3-5 new test cases to `TestValidationTool`
- [ ] Test various budget scenarios
- [ ] Test edge cases (over budget, under budget, etc.)
- [ ] Ensure all tests pass: `pytest tests/test_tools.py::TestValidationTool -v`

#### 4. Documentation (Day 5)
- [ ] Write section in technical report:
  - **Title**: "Agent 3: Budget Estimator & Validation Tool"
  - **Content**:
    - What my agent does
    - What my tool does
    - Calculation improvements
    - Validation rules I added
    - Tests I added
    - Challenges I faced

#### 5. Final Submission
- [ ] Commit code: `git add . && git commit -m "Student 3: Budget estimation enhancements"`
- [ ] Push to GitHub: `git push origin main`
- [ ] Add section to technical report

---

## 👤 STUDENT 4: Plan Validator Developer

### Assigned Component
- **Agent**: `agents/validator.py` - Plan Validator Agent
- **Tool**: `tools/file_saver_tool.py` - File Saver Tool
- **Tests**: `tests/test_tools.py` → `TestFileOperations` class

### Your Responsibilities

#### 1. Code Review & Understanding (Day 1)
- [ ] Read `agents/validator.py` completely
- [ ] Read `tools/file_saver_tool.py` completely
- [ ] Understand how plans are validated and saved
- [ ] Read corresponding test cases in `TestFileOperations`

#### 2. Modifications (Days 2-3)
Choose ONE of these to enhance:
- [ ] **Option A**: Improve validation logic
  - Add more quality metrics
  - Add compatibility checks
  - Add detailed scoring explanation
  
- [ ] **Option B**: Enhance file saving
  - Support multiple file formats (JSON, PDF)
  - Add timestamp to saved files
  - Add backup functionality
  
- [ ] **Option C**: Enhance both

#### 3. Testing (Day 4)
- [ ] Add 3-5 new test cases to `TestFileOperations`
- [ ] Test file creation and formatting
- [ ] Test error handling
- [ ] Ensure all tests pass: `pytest tests/test_tools.py::TestFileOperations -v`

#### 4. Documentation (Day 5)
- [ ] Write section in technical report:
  - **Title**: "Agent 4: Plan Validator & File Saver Tool"
  - **Content**:
    - What my agent does
    - What my tool does
    - Validation improvements
    - File saving enhancements
    - Tests I added
    - Challenges I faced

#### 5. Final Submission
- [ ] Commit code: `git add . && git commit -m "Student 4: Plan validation enhancements"`
- [ ] Push to GitHub: `git push origin main`
- [ ] Add section to technical report

---

## 🤝 ALL STUDENTS - Shared Tasks

### Technical Report (Shared Work)
The technical report has these sections - **divide them up**:

| Section | Writer | Pages | Due |
|---------|--------|-------|-----|
| Executive Summary | Project Lead | ½ | Day 5 |
| Problem Domain | Student 1 | ½ | Day 5 |
| System Architecture + Diagram | Student 2 | 1 | Day 5 |
| Agent Designs | All (1 page each) | 4 | Day 5 |
| Tool Descriptions | All (½ page each) | 2 | Day 5 |
| Testing & Results | Project Lead | 1 | Day 5 |
| Individual Contributions | Each student | 1 | Day 5 |
| **TOTAL** | **All** | **4-8 pages** | **Day 5** |

### Demo Video (Shared Recording)

**Assign roles:**
- [ ] Narrator (reads script)
- [ ] Screen Recorder (operates OBS)
- [ ] Presenter (shows system running)
- [ ] Editor (cuts video, uploads)

**Recording checklist:**
- [ ] Start with: "This is the AI Travel Planner MAS system"
- [ ] Show: `python main.py` running
- [ ] Demo: 2-3 travel scenarios
- [ ] Show: Generated plans and costs
- [ ] Show: Logs with all 4 agents working
- [ ] Duration: 4-5 minutes
- [ ] Upload to YouTube

### GitHub Repository (Project Lead)

- [ ] Create GitHub account (if needed)
- [ ] Create repository: `ctse-travel-planner`
- [ ] Push code: `git push origin main`
- [ ] Create README.md with setup instructions
- [ ] Create CONTRIBUTIONS.md documenting all 4 students
- [ ] Add links to:
  - Demo video (YouTube)
  - Technical report (PDF)
- [ ] Tag release: `v1.0`
- [ ] Share link with all team members

---

## 📅 Suggested Timeline

### Day 1 (Monday)
- All members: Clone project
- All members: Install dependencies
- All members: Run `python main.py` to verify setup
- Each student: Read their assigned agent and tool

### Day 2-3 (Tuesday-Wednesday)
- Each student: Implement enhancements
- Each student: Test their code
- Project Lead: Start writing report introduction

### Day 4 (Thursday)
- Each student: Add test cases
- All students: Run full test suite
- Pass code to other team members for review

### Day 5 (Friday)
- Each student: Write their report section
- Project Lead: Compile report
- All: Create and record demo video
- All: Upload to GitHub
- All: Final review

---

## ✅ Final Submission Checklist

Before submitting, verify:

### Code (Each Student)
- [ ] My agent works correctly
- [ ] My tool works correctly
- [ ] I added 3+ test cases
- [ ] My tests pass: `pytest ...`
- [ ] I committed to GitHub: `git push origin main`

### Technical Report (All Students)
- [ ] Report has 4-8 pages
- [ ] Report has all required sections
- [ ] My section is complete
- [ ] Report has architecture diagram
- [ ] Report lists all 4 students' contributions

### Demo Video (Project Lead to verify)
- [ ] Video is 4-5 minutes
- [ ] Video shows system running
- [ ] Video shows all 4 agents working
- [ ] Video uploaded to YouTube
- [ ] YouTube link in GitHub README

### GitHub (Project Lead to verify)
- [ ] Repository created
- [ ] All code pushed
- [ ] README.md complete with setup instructions
- [ ] CONTRIBUTIONS.md lists all students
- [ ] Links to demo video
- [ ] Links to technical report
- [ ] Tagged as v1.0

---

## 👥 Team Communication Tips

### Daily Check-ins
```
[Student 1]: "Finished cost calculator improvements. Tests passing."
[Student 2]: "Added 5 new locations. Ready for testing."
[Student 3]: "Enhanced validation logic. Needs review."
[Student 4]: "Created PDF export feature. All tests green."
```

### Before Pushing Code
```powershell
# Always pull latest first
git pull origin main

# Then push your changes
git add .
git commit -m "Student X: [Clear description]"
git push origin main
```

### Handling Conflicts
If two students edit the same file:
```powershell
# Person 2 pulls to see changes
git pull origin main

# Resolve conflicts manually
# Then commit and push
git add .
git commit -m "Resolved merge conflicts with Student X's changes"
git push origin main
```

---

## 🎓 Learning Outcomes

By the end of this project, you should understand:

**Student 1:**
- How itinerary generation works
- How cost calculations are done
- Testing financial calculations
- Integration with LLM

**Student 2:**
- How to manage external data sources
- How to structure location information
- Data retrieval and caching
- Testing data tools

**Student 3:**
- How to implement validation logic
- Cost estimation algorithms
- Budget compatibility checks
- Testing edge cases

**Student 4:**
- Advanced validation techniques
- File I/O in Python
- Data persistence
- Quality metrics

**All Students:**
- Multi-agent system coordination
- Git collaboration
- Python best practices
- Testing and debugging
- Technical documentation
- Working in a team

---

## ❓ FAQ

**Q: Can I modify code from other students?**  
A: Yes, but only if needed. Run `git pull` first and discuss changes in team.

**Q: What if I find a bug in someone else's code?**  
A: Let them know. Test it. Create an issue on GitHub.

**Q: Should I modify the orchestrator (main.py)?**  
A: No, keep it unchanged. All changes in agent/tool files only.

**Q: Can I use external libraries?**  
A: Check with team leader first. Should use what's in requirements.txt.

**Q: How do I know if my tests are good?**  
A: Run: `pytest tests/test_tools.py::TestYourComponent -v --cov`  
Should see 80%+ code coverage.

**Q: What if tests from day 1 fail after my changes?**  
A: Don't break existing tests. Fix your code, not the tests.

---

## 📞 Support Resources

### Commands to Remember

```powershell
# Get latest code
git pull origin main

# See your changes
git status

# Save your work
git add .
git commit -m "Description"
git push origin main

# Run system
ollama serve              # Terminal 1
python main.py           # Terminal 2

# Run tests
pytest tests/test_tools.py -v
pytest tests/test_tools.py::TestYourComponent -v

# Check setup
python setup_check.py
```

### Helpful Files to Read
- `TEAM_SETUP_GUIDE.md` - This setup document
- `README.md` - Project overview
- `REQUIREMENT_COMPLIANCE_REPORT.txt` - What's expected
- `OLLAMA_SETUP.txt` - Ollama instructions
- `COVERAGE_ANALYSIS.txt` - Standards compliance

---

## ✨ Success Criteria

Your project will be graded on:

| Criterion | What We Look For |
|-----------|-----------------|
| Agent Design (20%) | Does your agent solve its role well? |
| Tool Development (20%) | Is your tool useful and well-coded? |
| Testing (10%) | Are there good test cases? |
| Documentation (15%) | Is everything documented? |
| Code Quality (15%) | Type hints, docstrings, error handling? |
| Teamwork (10%) | All 4 components work together? |
| Collaboration (10%) | Did you use GitHub properly? |

**Final Score = Average of all above** → Target: 85-95%

---

**Ready to start? Everyone run:**
```powershell
python setup_check.py
```

**All members should see ✓ marks!**
