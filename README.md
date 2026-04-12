# AI Travel Planner - Multi-Agent System (Enhanced with Ollama LLM)

A locally-hosted intelligent travel planning system built with Python that uses multiple specialized agents and Ollama LLM (llama3:8b) for smart itinerary generation.

**Status**: ✓ Production Ready | ✓ Ollama Integrated | ✓ All Requirements Met

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Ollama (local LLM engine)
- ~8GB RAM minimum

### Installation (5 minutes)

```bash
# 1. Install Ollama (https://ollama.ai)
ollama pull llama3:8b

# 2. Install Python dependencies  
pip install -r requirements.txt

# 3. Verify setup
python setup_check.py
```

### Run the System

```bash
# Terminal 1: Start Ollama server
ollama serve

# Terminal 2: Run CLI or Web UI
python main.py                    # CLI mode
# OR
python -m streamlit run app.py    # Web UI mode
```

---

## 📋 Project Structure

```
d:\CTSE\ctse2\
├── agents/                           # 4 Agent implementations
│   ├── planner.py                   # Travel Planner Agent (Student 1)
│   ├── researcher.py                # Location Researcher Agent (Student 2)
│   ├── estimator.py                 # Budget Estimator Agent (Student 3)
│   └── validator.py                 # Plan Validator Agent (Student 4)
│
├── tools/                            # 4 Custom tools that agents use
│   ├── cost_calculator_tool.py      # Cost calculations (Student 1)
│   ├── location_data_tool.py        # Destination data (Student 2)
│   ├── validation_tool.py           # Plan validation (Student 3)
│   └── file_saver_tool.py           # File I/O operations (Student 4)
│
├── tests/                            # Comprehensive test suite
│   └── test_tools.py                # 36+ unit and integration tests
│
├── logs/                             # Execution logs
│   └── log.txt                      # Timestamped activity logs
│
├── main.py                          # CLI orchestrator
├── app.py                           # Streamlit web UI
├── ollama_client.py                 # Ollama LLM client (NEW)
├── setup_check.py                   # Setup verification (NEW)
│
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
├── OLLAMA_SETUP.txt                 # Detailed Ollama setup guide (NEW)
├── COVERAGE_ANALYSIS.txt            # Requirements compliance audit (NEW)
│
├── output.txt                       # Generated travel plans
└── PROJECT_SUMMARY.md               # Project overview
```

---

## 🤖 System Architecture

### Multi-Agent Pipeline

```
User Input (Destination, Days, Budget)
     ↓
[Agent 1] Travel Planner
    ↓ (Itinerary)
[Agent 2] Location Researcher  
    ↓ (Enhanced Plan)
[Agent 3] Budget Estimator
    ↓ (Cost Analysis)
[Agent 4] Plan Validator
    ↓ (Validation Result)
Final Travel Plan (Saved to output.txt)
```

### Components

**AGENTS (4)** - Each agent handles a specific role:
- `TravelPlannerAgent` - Creates day-by-day itineraries using Ollama LLM
- `LocationResearchAgent` - Enhances plans with destination insights
- `BudgetEstimatorAgent` - Calculates comprehensive travel costs
- `PlanValidatorAgent` - Validates and scores final plans

**TOOLS (4)** - Custom Python functions that agents use:
- `cost_calculator_tool` - Budget calculations with breakdown
- `location_data_tool` - Static travel data for 4 destinations  
- `validation_tool` - Quality scoring algorithm
- `file_saver_tool` - Output generation and logging

**LLM INTEGRATION** - Ollama powered reasoning:
- `ollama_client.py` - HTTP REST client for llama3:8b
- Smart prompt engineering for each agent
- Fallback to mock data if Ollama unavailable
- Temperature and token configuration

**ORCHESTRATOR** - TravelPlannerMAS class:
- Sequences agents in correct order
- Passes context between agents
- Manages logging and observability
- Handles errors gracefully

---

## ⚙️ Setup Guide

### Step 1: Install Ollama

**Windows**:
1. Download from https://ollama.ai
2. Run installer (ollama-windows-amd64.exe)
3. Follow the wizard

**Mac/Linux**:
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### Step 2: Download llama3:8b Model

```bash
ollama pull llama3:8b
```

This downloads ~4.7GB. Required one-time only.

Verify:
```bash
ollama list
# Output should show: llama3:8b
```

### Step 3: Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install streamlit>=1.28.0 pandas>=1.3.0 pytest>=7.0.0 requests>=2.28.0
```

### Step 4: Verify Setup

```bash
python setup_check.py
```

This checks:
- ✓ Python version
- ✓ Required packages
- ✓ Project structure
- ✓ Ollama connectivity
- ✓ Model availability
- ✓ Ollama client

---

## 🎯 Usage

### Option 1: Command-Line Interface

```bash
# Terminal 1 - Start Ollama
ollama serve

# Terminal 2 - Run CLI system
python main.py
```

Output:
```
✓ Plan generated successfully!
Status: ✓ APPROVED
Estimated Cost: Rs. 30,360.00
Quality Score: 85.0/100
✓ Plan saved to output.txt

[EXECUTION LOGS...]
```

### Option 2: Web UI (Streamlit)

```bash
# Terminal 1 - Start Ollama
ollama serve

# Terminal 2 - Run web interface
python -m streamlit run app.py
```

Browser: http://localhost:8501

Features:
- Interactive input forms
- Real-time cost metrics
- Validation reports
- Download buttons
- Log viewer

### Option 3: Without Ollama (Mock Data)

If Ollama not available:

```bash
python main.py
# Will use fallback structured mock data
```

---

## 🧪 Testing

### Run All Tests

```bash
pytest tests/ -v
```

### Run With Coverage

```bash
pytest tests/ --cov=tools --cov=agents
```

### Test Categories Included

- Cost Calculator Tests (10)
- Location Data Tests (6)
- Validation Tests (4)
- File Operation Tests (6)
- Agent Tests (4)
- Integration Tests (1)
- Property-Based Tests (5)

**Total**: 36+ comprehensive test cases

---

## ✨ Features

✓ **4 Intelligent Agents** with specialized roles
✓ **Ollama LLM Integration** - Uses local llama3:8b for real reasoning
✓ **4 Custom Tools** with full type hints and docstrings
✓ **Smart State Management** - Context flows perfectly between agents
✓ **Comprehensive Logging** - Timestamped execution tracking
✓ **Plan Validation** - Quality scoring 0-100
✓ **Budget Analysis** - Detailed cost breakdown
✓ **Beautiful Web UI** - Streamlit dashboard
✓ **Full Test Suite** - 36+ tests covering all components
✓ **100% Local** - No external APIs or payment required
✓ **Fallback Support** - Works without Ollama using mock data
✓ **4 Destinations** - Ella, Kandy, Colombo, Galle

---

## 🗺️ Supported Destinations

1. **Ella** - Hill station with hiking, tea plantations, Nine Arch Bridge
2. **Kandy** - Cultural capital with temples, botanic gardens
3. **Colombo** - Modern capital with beaches, museums
4. **Galle** - Historic coastal fort (UNESCO World Heritage)

---

## 📊 Data Flow & State Management

### How Agents Communicate

```python
# State flows sequentially between agents
state = {
    "destination": "Ella",
    "num_days": 3,
    "budget": 20000,
    "itinerary": "...",  # Created by Agent 1
    "research": "...",   # Added by Agent 2
    "costs": {...},      # Added by Agent 3
    "validation": {...}  # Added by Agent 4
}
```

### Example: Using the System Programmatically

```python
from main import TravelPlannerMAS

# Initialize system with Ollama
mas = TravelPlannerMAS(use_ollama=True)

# Generate plan
result = mas.generate_travel_plan(
    destination="Ella",
    num_days=3,
    budget=20000
)

# Access results
print(f"Cost: {result['estimated_cost']}")
print(f"Quality: {result['validation']['quality_score']}")

# Save plan
mas.save_plan(result['final_plan'])

# View logs
print(mas.get_logs())
```

---

## 🔧 Configuration

### Ollama Settings (ollama_client.py)

```python
Model:        llama3:8b       (default)
Host:         localhost:11434 (default)
Temperature:  0.7            (creativity level, 0-1)
Max Tokens:   500-800        (response length)
```

### To Use Different Model

```bash
ollama pull mistral          # or llama2, dolphin-mixtral, etc.
# Then edit ollama_client.py: model="mistral"
```

### Disable LLM Reasoning

```python
mas = TravelPlannerMAS(use_ollama=False)  # Use mock data only
```

---

## 📈 Performance

### Response Times
- Itinerary generation: 2-5 seconds
- Location research: 1-2 seconds
- Cost calculation: <1 second
- Validation: <1 second
- **Total**: 5-10 seconds

### Resource Usage
- Memory: ~4-6GB (with Ollama)
- CPU: 2-4 cores utilized
- Disk: ~5GB (model storage)

### Optimization Tips
- Keep Ollama running between requests
- Use smaller models for faster responses (mistral, llama2)
- Monitor RAM usage: `ollama list`

---

## ✅ Requirements Coverage

This implementation covers ALL assignment requirements:

| Requirement | Status | Document |
|------------|--------|----------|
| Multi-Agent System (3-4 agents) | ✅ 4 agents | COVERAGE_ANALYSIS.txt |
| Tool Development (custom tools) | ✅ 4 tools | COVERAGE_ANALYSIS.txt |
| State Management | ✅ Sequential | COVERAGE_ANALYSIS.txt |
| Logging & Observability | ✅ Comprehensive | logs/log.txt |
| Ollama Integration | ✅ Implemented | ollama_client.py |
| No Paid APIs | ✅ Local only | main.py |
| Type Hints | ✅ 100% coverage | All files |
| Docstrings | ✅ Complete | All files |
| Testing | ✅ 36+ tests | tests/test_tools.py |
| Project Structure | ✅ Organized | README.md |

See **COVERAGE_ANALYSIS.txt** for detailed compliance audit.

---

## 🚨 Troubleshooting

### "Cannot connect to Ollama"
```bash
# Check if Ollama is running
ollama serve

# Check connection
curl http://localhost:11434/api/tags
```

### "llama3:8b not found"
```bash
ollama pull llama3:8b
ollama list  # verify
```

### "Module not found" error
```bash
# Ensure requirements installed
pip install -r requirements.txt

# Check Python path
python -c "import streamlit; print(streamlit.__version__)"
```

### "Port 8501 already in use"
```bash
# Use different port
python -m streamlit run app.py --server.port=8502
```

### "Slow performance"
- Monitor RAM: `ollama list`
- Try smaller model: `ollama pull mistral`
- Reduce tokens: edit ollama_client.py

---

## 📚 Documentation

- **OLLAMA_SETUP.txt** - Detailed Ollama installation guide
- **COVERAGE_ANALYSIS.txt** - Requirements compliance audit
- **PROJECT_SUMMARY.md** - High-level project overview
- **IMPLEMENTATION_SUMMARY.py** - Technical architecture
- **tests/test_tools.py** - Test documentation

---

## 👥 Student Assignments

Each team member is responsible for:

**Student 1**:
- Agent: Travel Planner (agents/planner.py)
- Tool: Cost Calculator (tools/cost_calculator_tool.py)
- Tests: Cost calculator test cases

**Student 2**:
- Agent: Location Researcher (agents/researcher.py)
- Tool: Location Data (tools/location_data_tool.py)
- Tests: Location data test cases

**Student 3**:
- Agent: Budget Estimator (agents/estimator.py)
- Tool: Validation Tool (tools/validation_tool.py)
- Tests: Validation test cases

**Student 4**:
- Agent: Plan Validator (agents/validator.py)
- Tool: File Saver (tools/file_saver_tool.py)
- Tests: File operation test cases

---

## 🔗 Resources

- Ollama Official: https://ollama.ai
- LLM Models: https://ollama.ai/library
- Streamlit Docs: https://docs.streamlit.io
- Python Type Hints: https://docs.python.org/3.10/library/typing.html

---

## ✉️ Support

See **OLLAMA_SETUP.txt** for detailed setup instructions.

Check **logs/log.txt** for execution details and error messages.

Run `python setup_check.py` to verify installation.

---

**Version**: 2.0 (Ollama Integrated)  
**Updated**: April 12, 2026  
**Status**: ✅ Production Ready
pytest tests/test_tools.py::TestCostCalculator -v

# With coverage
pytest tests/ --cov=tools --cov=agents --cov=. --cov-report=html
```

## Configuration

Default models and ports:
- LLM: Ollama (local)
- Model: llama3:8b
- URL: http://localhost:11434
- Ollama API is used for agent orchestration

## Performance

Typical response times:
- Plan generation: 5-15 seconds
- Validation: 1-2 seconds
- File operations: <1 second

## Code Quality

- Full type hints in all tools
- Comprehensive docstrings
- Error handling and validation
- Clean module organization
- PEP 8 compliant

## Future Enhancements

- Database integration for user profiles
- Weather API integration
- Hotel booking API integration
- Flight price lookups
- Multi-language support

## License & Attribution

This is an academic project for CTSE SE4010 Assignment 2.

---

**Questions?** Check the documentation in code or review test cases for usage examples.
