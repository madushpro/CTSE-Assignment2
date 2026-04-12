# 🚀 QUICK START - 30 MINUTES TO RUNNING

## For Project Lead (First Person)

### Step 1: Create GitHub Repo (5 minutes)
```
1. Go to: https://github.com/new
2. Repository name: ctse-travel-planner
3. Description: AI Travel Planner Multi-Agent System with Ollama LLM
4. Set to: Public
5. Click: Create repository
6. Copy the URL: https://github.com/YOUR_USERNAME/ctse-travel-planner.git
```

### Step 2: Upload Code (5 minutes)
```powershell
cd D:\CTSE\ctse2

git init
git add .
git commit -m "Initial commit: AI Travel Planner MAS with Ollama LLM"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ctse-travel-planner.git
git push -u origin main

# Copy the repository URL to share with team
```

### Step 3: Share with Team
Send to all 3 team members:
```
Repository URL: https://github.com/YOUR_USERNAME/ctse-travel-planner.git
Setup instructions: See TEAM_SETUP_GUIDE.md in the repo
```

---

## For All Other Team Members (Students 2, 3, 4)

### Step 1: Clone Project (2 minutes)
```powershell
cd C:\Users\YourUsername\Documents

git clone https://github.com/PROJECT_LEAD_USERNAME/ctse-travel-planner.git

cd ctse-travel-planner
```

### Step 2: Install Python Packages (3 minutes)
```powershell
pip install -r requirements.txt
```

### Step 3: Verify Installation (2 minutes)
```powershell
python setup_check.py

# You should see: ✓ Python version, ✓ Packages, ✓ Directories
```

### Step 4: Install Ollama (15 minutes)
```powershell
# Go to: https://ollama.ai
# Download and install Ollama
# Then run:

ollama pull llama3:8b
# This downloads 4.7GB - be patient!
```

### Step 5: Test System (2 minutes)
```powershell
# Terminal 1
ollama serve
# Should show: API server running on 127.0.0.1:11434

# Terminal 2 (NEW terminal/PowerShell)
cd ctse-travel-planner
python main.py

# Should show: ✓ Travel plan generated successfully!
```

---

## ✅ DONE! System is Ready

All members should now see:
- ✓ `ollama serve` running in Terminal 1
- ✓ `python main.py` producing output in Terminal 2
- ✓ `output.txt` file created with complete travel plan

---

## 📋 Next: Read Your Role

Each member should read their section:

**Student 1**: Read `STUDENT_ASSIGNMENT_CHECKLIST.md` → STUDENT 1 section
**Student 2**: Read `STUDENT_ASSIGNMENT_CHECKLIST.md` → STUDENT 2 section
**Student 3**: Read `STUDENT_ASSIGNMENT_CHECKLIST.md` → STUDENT 3 section
**Student 4**: Read `STUDENT_ASSIGNMENT_CHECKLIST.md` → STUDENT 4 section

---

## 🎯 Your Task (All Students)

1. Understand your assigned agent + tool
2. Make 1-2 improvements to your code
3. Add 3-5 test cases
4. Write your section in technical report
5. Commit and push to GitHub

---

## Troubleshooting

**Problem**: "Cannot connect to Ollama"
**Fix**: Make sure `ollama serve` is running in Terminal 1

**Problem**: "ModuleNotFoundError"
**Fix**: Run `pip install -r requirements.txt`

**Problem**: "git command not found"
**Fix**: Install Git: https://git-scm.com/

**Problem**: Model not downloading
**Fix**: `ollama pull llama3:8b` in PowerShell, be patient (5-15 min)

---

## 📞 Support

For help, see:
- `TEAM_SETUP_GUIDE.md` - Detailed setup instructions
- `STUDENT_ASSIGNMENT_CHECKLIST.md` - Your specific role
- `README.md` - Project overview
- Run `python setup_check.py` - System verification

---

**Everyone ready? Let's go! 🚀**
