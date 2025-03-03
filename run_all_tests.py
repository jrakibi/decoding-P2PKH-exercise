#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path

def run_tests_for_exercise(exercise_dir):
    """Run pytest for a specific exercise directory and return the result"""
    print(f"\n{'='*80}")
    print(f"Running tests for: {exercise_dir}")
    print(f"{'='*80}")
    
    # Change to the exercise directory
    os.chdir(exercise_dir)
    
    # Run pytest and capture the output
    result = subprocess.run(
        ["pytest", "test_solution.py", "-v"],
        capture_output=True,
        text=True
    )
    
    # Print the output
    print(result.stdout)
    if result.stderr:
        print("Errors:")
        print(result.stderr)
    
    # Return to the original directory
    os.chdir(Path(exercise_dir).parent.parent)
    
    return result.returncode == 0  # True if tests passed

def main():
    # Get the root directory of the project
    root_dir = Path(__file__).parent.absolute()
    
    # List of exercise directories from the autograding.json
    exercises = [
        "exercises/ex1_transaction_basics",
        "exercises/ex2_transaction_digests",
        "exercises/ex3_signatures",
        "exercises/ex4_witness_data",
        "exercises/ex5_complete_transaction"
    ]
    
    # Store results for summary
    results = {}
    
    # Run tests for each exercise
    for exercise in exercises:
        exercise_path = root_dir / exercise
        if not exercise_path.exists():
            print(f"Warning: Exercise directory {exercise} not found!")
            results[exercise] = False
            continue
            
        results[exercise] = run_tests_for_exercise(exercise_path)
    
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