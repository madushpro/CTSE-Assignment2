import os
from datetime import datetime
from typing import Dict, Any, Optional


def save_travel_plan(plan_content: str, filename: str = "output.txt") -> Dict[str, Any]:
    """
    Save generated travel plan to a file.
    
    Args:
        plan_content (str): The travel plan text to save
        filename (str): Name of output file (default: 'output.txt')
    
    Returns:
        Dict[str, Any]: Result dictionary containing:
                       - 'success': Boolean indicating success
                       - 'filepath': Full path to saved file
                       - 'timestamp': When file was saved
                       - 'size_bytes': Size of saved content
                       - 'message': Status message
    
    Raises:
        ValueError: If plan_content is empty
        IOError: If file cannot be written
    
    Example:
        >>> result = save_travel_plan(plan, "my_plan.txt")
        >>> print(f"Saved to: {result['filepath']}")
    """
    
    if not plan_content or not isinstance(plan_content, str):
        raise ValueError("plan_content must be a non-empty string")
    
    if not filename.endswith('.txt'):
        filename = filename + '.txt'
    
    try:
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(filename)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        
        # Format content with header
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_content = f"""
{'='*70}
TRAVEL PLAN GENERATED
Generated on: {timestamp}
{'='*70}

{plan_content}

{'='*70}
End of Travel Plan
{'='*70}
"""
        
        # Write to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(formatted_content)
        
        file_size = len(formatted_content.encode('utf-8'))
        
        return {
            "success": True,
            "filepath": os.path.abspath(filename),
            "timestamp": timestamp,
            "size_bytes": file_size,
            "message": f"Plan saved successfully to {filename}"
        }
    
    except IOError as e:
        raise IOError(f"Failed to save file {filename}: {str(e)}")


def append_to_log(
    log_entry: str,
    log_filename: str = "logs/log.txt"
) -> Dict[str, Any]:
    """
    Append an entry to the execution log file.
    
    Args:
        log_entry (str): Text to append to log
        log_filename (str): Path to log file (default: 'logs/log.txt')
    
    Returns:
        Dict[str, Any]: Result dictionary with:
                       - 'success': Boolean
                       - 'log_file': Path to log file
                       - 'entry_size': Size of appended entry
                       - 'timestamp': When logged
    
    Raises:
        IOError: If log file cannot be written
    """
    
    if not log_entry or not isinstance(log_entry, str):
        raise ValueError("log_entry must be a non-empty string")
    
    try:
        # Create log directory if needed
        log_dir = os.path.dirname(log_filename)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_entry = f"[{timestamp}] {log_entry}\n"
        
        # Append to log file
        with open(log_filename, 'a', encoding='utf-8') as f:
            f.write(formatted_entry)
        
        return {
            "success": True,
            "log_file": os.path.abspath(log_filename),
            "entry_size": len(formatted_entry.encode('utf-8')),
            "timestamp": timestamp
        }
    
    except IOError as e:
        raise IOError(f"Failed to write to log file {log_filename}: {str(e)}")


def load_travel_plan(filename: str = "output.txt") -> Dict[str, Any]:
    """
    Load and retrieve a previously saved travel plan.
    
    Args:
        filename (str): Name of file to load (default: 'output.txt')
    
    Returns:
        Dict[str, Any]: Dictionary containing:
                       - 'success': Boolean indicating if file was found
                       - 'content': The plan text (or None if not found)
                       - 'filepath': Full path to file
                       - 'last_modified': When file was last updated
                       - 'size_bytes': File size
    
    Raises:
        FileNotFoundError: If file doesn't exist
        IOError: If file cannot be read
    """
    
    try:
        if not os.path.exists(filename):
            return {
                "success": False,
                "content": None,
                "filepath": filename,
                "message": f"File {filename} not found",
                "exists": False
            }
        
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        stat_info = os.stat(filename)
        last_modified = datetime.fromtimestamp(stat_info.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
        
        return {
            "success": True,
            "content": content,
            "filepath": os.path.abspath(filename),
            "last_modified": last_modified,
            "size_bytes": stat_info.st_size,
            "exists": True
        }
    
    except IOError as e:
        raise IOError(f"Failed to read file {filename}: {str(e)}")


def clear_log(log_filename: str = "logs/log.txt") -> Dict[str, Any]:
    """
    Clear the log file (useful for fresh start or testing).
    
    Args:
        log_filename (str): Path to log file to clear
    
    Returns:
        Dict[str, Any]: Result with success status and message
    
    Raises:
        IOError: If file cannot be cleared
    """
    
    try:
        # Create directory if needed
        log_dir = os.path.dirname(log_filename)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
        
        # Clear the file
        with open(log_filename, 'w', encoding='utf-8') as f:
            f.write("")
        
        return {
            "success": True,
            "log_file": os.path.abspath(log_filename),
            "message": "Log file cleared successfully"
        }
    
    except IOError as e:
        raise IOError(f"Failed to clear log file: {str(e)}")


def get_log_contents(log_filename: str = "logs/log.txt") -> str:
    """
    Get the current contents of the log file.
    
    Args:
        log_filename (str): Path to log file
    
    Returns:
        str: Contents of log file, or empty string if doesn't exist
    
    Example:
        >>> logs = get_log_contents()
        >>> print(logs)
    """
    
    try:
        if not os.path.exists(log_filename):
            return "No logs yet.\n"
        
        with open(log_filename, 'r', encoding='utf-8') as f:
            return f.read()
    
    except IOError:
        return "Error reading log file.\n"


if __name__ == "__main__":
    # Test the file saver tool
    print("\n=== File Saver Tool Tests ===\n")
    
    # Test travel plan
    test_plan = """
    ELLA TRAVEL PLAN - 3 DAYS
    
    Day 1: Arrival
    - Reach Ella
    - Check into mid-range hotel
    - Rest and explore local area
    
    Day 2: Sightseeing
    - Hike to Nine Arch Bridge
    - Visit Little Adam's Peak
    
    Day 3: Adventure
    - Tour Ravana Falls
    - Relax at café
    
    Total Estimated Cost: Rs. 15,000
    """
    
    try:
        # Test 1: Save plan
        print("Test 1: Save travel plan")
        result = save_travel_plan(test_plan, "test_plan.txt")
        print(f"  Success: {result['success']}")
        print(f"  Saved to: {result['filepath']}")
        print(f"  Size: {result['size_bytes']} bytes\n")
        
        # Test 2: Append to log
        print("Test 2: Append to log")
        log_result = append_to_log("Test log entry 1", "test_log.txt")
        print(f"  Success: {log_result['success']}")
        print(f"  Log file: {log_result['log_file']}\n")
        
        # Test 3: Load plan
        print("Test 3: Load travel plan")
        load_result = load_travel_plan("test_plan.txt")
        print(f"  Success: {load_result['success']}")
        print(f"  File size: {load_result['size_bytes']} bytes")
        print(f"  Last modified: {load_result['last_modified']}\n")
        
        # Test 4: Get log contents
        print("Test 4: Get log contents")
        logs = get_log_contents("test_log.txt")
        print(f"  Log content length: {len(logs)} chars")
        
    except (ValueError, IOError) as e:
        print(f"✗ Error: {e}")
    finally:
        # Cleanup
        for f in ["test_plan.txt", "test_log.txt"]:
            if os.path.exists(f):
                os.remove(f)
                print(f"✓ Cleaned up {f}")
