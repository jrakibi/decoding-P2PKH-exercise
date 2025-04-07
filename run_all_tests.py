#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path

def run_test_for_exercise(exercise_dir):
    """Run pytest for a specific exercise directory and return the result"""
    print(f"\n{'='*80}")
    print(f"Running tests for: {exercise_dir}")
    print(f"{'='*80}")
    
    # Get the test file name
    test_files = list(exercise_dir.glob('test_*.py'))
    if not test_files:
        print(f"No test files found in {exercise_dir}")
        return False
    
    test_file = test_files[0].name
    
    # Run pytest and capture the output
    result = subprocess.run(
        ["python", "-m", "pytest", str(exercise_dir / test_file), "-v"],
        capture_output=True,
        text=True
    )
    
    # Print the output
    print(result.stdout)
    if result.stderr:
        print("Errors:")
        print(result.stderr)
    
    return result.returncode == 0  # True if tests passed

def main():
    # Get the root directory of the project
    root_dir = Path(__file__).parent.absolute()
    
    # List of exercise directories
    exercises_dir = root_dir / "exercises"
    exercises = sorted(list(exercises_dir.glob("exercise*")))
    
    if not exercises:
        print("No exercise directories found!")
        return 1
    
    # Store results for summary
    results = {}
    
    # Run tests for each exercise
    for exercise in exercises:
        results[exercise.name] = run_test_for_exercise(exercise)
    
    # Print summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    
    passed = 0
    for exercise, passed_tests in results.items():
        status = "PASSED" if passed_tests else "FAILED"
        if passed_tests:
            passed += 1
        print(f"{exercise}: {status}")
    
    print(f"\nPassed {passed}/{len(exercises)} exercise test suites")
    
    # Return non-zero exit code if any tests failed
    return 0 if all(results.values()) else 1

if __name__ == "__main__":
    sys.exit(main()) 