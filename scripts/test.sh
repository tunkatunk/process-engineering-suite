#!/bin/bash

# Test script for the Supreme App

# Default behavior: run all tests
run_all=true
specific_test=""
module=""

# Parse command line arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    -m|--module)
      run_all=false
      module="$2"
      shift 2
      ;;
    -t|--test)
      run_all=false
      specific_test="$2"
      shift 2
      ;;
    *)
      echo "Unknown option: $1"
      echo "Usage: $0 [-m|--module <module_name>] [-t|--test <test_file_path>]"
      exit 1
      ;;
  esac
done

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

echo "Running tests..."

# Run tests based on the arguments
if $run_all; then
    # Run all tests
    python -m pytest tests/ src/modules/*/tests/ -v
elif [ -n "$module" ]; then
    # Run tests for a specific module
    if [ -d "src/modules/$module/tests" ]; then
        python -m pytest src/modules/$module/tests/ -v
    else
        echo "Module not found: $module"
        exit 1
    fi
elif [ -n "$specific_test" ]; then
    # Run a specific test file
    if [ -f "$specific_test" ]; then
        python -m pytest $specific_test -v
    else
        echo "Test file not found: $specific_test"
        exit 1
    fi
fi

exit_code=$?

if [ $exit_code -eq 0 ]; then
    echo "All tests passed!"
else
    echo "Some tests failed."
fi

exit $exit_code