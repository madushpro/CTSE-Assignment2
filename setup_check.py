"""
Quick setup verification script for AI Travel Planner MAS
Checks that all dependencies and components are properly configured
"""

import os
import sys
from pathlib import Path

def check_python_version():
    """Verify Python 3.8+ is installed."""
    python_version = sys.version_info
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print(f"✗ Python 3.8+ required. Current: {python_version.major}.{python_version.minor}")
        return False
    print(f"✓ Python version: {python_version.major}.{python_version.minor}")
    return True


def check_required_packages():
    """Check if required Python packages are installed."""
    packages = {
        "streamlit": "Streamlit web UI",
        "pandas": "Data processing",
        "pytest": "Testing framework",
        "requests": "Ollama API calls"
    }
    
    all_ok = True
    for package, description in packages.items():
        try:
            __import__(package)
            print(f"✓ {package:15} ({description})")
        except ImportError:
            print(f"✗ {package:15} NOT INSTALLED  (use: pip install {package})")
            all_ok = False
    
    return all_ok


def check_project_structure():
    """Verify project directory structure."""
    required_dirs = ["agents", "tools", "tests", "logs"]
    all_ok = True
    
    for dir_name in required_dirs:
        if os.path.isdir(dir_name):
            print(f"✓ Directory: {dir_name}/")
        else:
            print(f"✗ Directory: {dir_name}/ NOT FOUND")
            all_ok = False
    
    return all_ok


def check_required_files():
    """Verify critical files exist."""
    required_files = {
        "agents/planner.py": "Travel Planner Agent",
        "agents/researcher.py": "Location Researcher Agent",
        "agents/estimator.py": "Budget Estimator Agent",
        "agents/validator.py": "Plan Validator Agent",
        "tools/cost_calculator_tool.py": "Cost Calculator Tool",
        "tools/location_data_tool.py": "Location Data Tool",
        "tools/validation_tool.py": "Validation Tool",
        "tools/file_saver_tool.py": "File Saver Tool",
        "main.py": "Main orchestrator",
        "app.py": "Streamlit web UI",
        "ollama_client.py": "Ollama LLM client",
        "requirements.txt": "Package dependencies"
    }
    
    all_ok = True
    for file_path, description in required_files.items():
        if os.path.isfile(file_path):
            print(f"✓ {file_path:30} ({description})")
        else:
            print(f"✗ {file_path:30} NOT FOUND")
            all_ok = False
    
    return all_ok


def check_ollama_connection():
    """Check if Ollama server is accessible."""
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            print("✓ Ollama server: Connected at http://localhost:11434")
            return True
        else:
            print(f"✗ Ollama server: Returned status {response.status_code}")
            print("  Start Ollama with: ollama serve")
            return False
    except requests.exceptions.ConnectionError:
        print("✗ Ollama server: NOT RUNNING")
        print("  To start Ollama: ollama serve")
        return False
    except Exception as e:
        print(f"✗ Ollama server: Error {str(e)}")
        return False


def check_ollama_model():
    """Check if llama3:8b model is downloaded."""
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get("models", [])
            model_names = [m["name"] for m in models]
            
            if any("llama3:8b" in name or "llama3" in name for name in model_names):
                print("✓ llama3:8b model: Downloaded and available")
                return True
            else:
                print("✗ llama3:8b model: NOT FOUND")
                print("  Download with: ollama pull llama3:8b")
                print(f"  Available models: {', '.join(model_names) if model_names else 'None'}")
                return False
        else:
            print("⚠ Ollama server: Cannot check models")
            return False
    except:
        print("⚠ Ollama server: Cannot check models")
        return False


def check_ollama_client():
    """Test Ollama client functionality."""
    try:
        from ollama_client import create_ollama_client
        client = create_ollama_client()
        print("✓ Ollama client: Successfully initialized")
        return True
    except ConnectionError as e:
        print(f"✗ Ollama client: Connection failed")
        print(f"  Error: {str(e)}")
        return False
    except Exception as e:
        print(f"✗ Ollama client: Error - {str(e)}")
        return False


def main():
    """Run all setup checks."""
    
    print("\n" + "="*70)
    print("AI TRAVEL PLANNER - SETUP VERIFICATION")
    print("="*70 + "\n")
    
    checks = [
        ("Python Version", check_python_version),
        ("Required Packages", check_required_packages),
        ("Project Structure", check_project_structure),
        ("Required Files", check_required_files),
        ("Ollama Server", check_ollama_connection),
        ("llama3:8b Model", check_ollama_model),
        ("Ollama Client", check_ollama_client)
    ]
    
    print("\nRUNNING CHECKS:\n")
    
    results = {}
    for check_name, check_func in checks:
        print(f"\n{check_name}:")
        print("-" * 40)
        try:
            results[check_name] = check_func()
        except Exception as e:
            print(f"✗ Check failed: {e}")
            results[check_name] = False
    
    # Summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    print(f"\nPassed: {passed}/{total}")
    
    if passed == total:
        print("\n✓ All checks passed! System is ready to use.")
        print("\nTo run the system:")
        print("  Option 1 (CLI):     python main.py")
        print("  Option 2 (Web UI):  python -m streamlit run app.py")
        return 0
    else:
        print("\n⚠ Some checks failed. Please fix the issues above.")
        print("\nCommon solutions:")
        print("  1. Install packages:      pip install -r requirements.txt")
        print("  2. Start Ollama:          ollama serve")
        print("  3. Download model:        ollama pull llama3:8b")
        print("  4. Check file structure:  ls agents/ tools/ tests/")
        return 1


if __name__ == "__main__":
    sys.exit(main())
