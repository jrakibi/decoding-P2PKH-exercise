#!/usr/bin/env python3
import os
import shutil
import subprocess
import sys
from pathlib import Path

def test_solution(exercise_num):
    """Test a solution by copying it to the template file and running tests"""
    print(f"\n{'='*80}")
    print(f"Testing solution for Exercise {exercise_num}")
    print(f"{'='*80}")
    
    # Paths
    exercise_dir = f"exercises/exercise{exercise_num}"
    solution_file = f"solutions/exercise{exercise_num}/solution.py"
    template_file = f"{exercise_dir}/template.py"
    
    # Make backup of original template
    backup_file = f"{template_file}.bak"
    shutil.copy2(template_file, backup_file)
    
    try:
        # Copy solution to template
        print(f"Copying solution to {template_file}...")
        shutil.copy2(solution_file, template_file)
        
        # Run tests
        print("Running tests...")
        result = subprocess.run(
            ["python", "-m", "pytest", f"{exercise_dir}/test_exercise{exercise_num}.py", "-v"],
            capture_output=True,
            text=True
        )
        
        # Print output
        print(result.stdout)
        if result.stderr:
            print("Errors:")
            print(result.stderr)
        
        success = result.returncode == 0
        status = "PASSED" if success else "FAILED"
        print(f"Test result: {status}")
        
        return success
    
    finally:
        # Restore original template
        shutil.move(backup_file, template_file)
        print(f"Restored original template file.")

def main():
    # Test all solutions or specific ones
    if len(sys.argv) > 1:
        exercises = [int(ex) for ex in sys.argv[1:]]
    else:
        exercises = range(1, 6)  # Test exercises 1-5
    
    results = {}
    
    for ex_num in exercises:
        results[ex_num] = test_solution(ex_num)
    
    # Print summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    
    passed = 0
    for ex_num, success in results.items():
        status = "PASSED" if success else "FAILED"
        if success:
            passed += 1
        print(f"Exercise {ex_num}: {status}")
    
    print(f"\nPassed {passed}/{len(results)} solution tests")
    
    # Return non-zero exit code if any tests failed
    return 0 if all(results.values()) else 1

if __name__ == "__main__":
    sys.exit(main()) 