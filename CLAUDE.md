# CLAUDE.md - Supreme App Development Guidelines

## Best Practices (MUST BE FOLLOWED)
- **Think Thoroughly**: Consider all implications before implementing solutions
- **Document Extensively**: Document all code, decisions, and design rationales
- **Use Best Coding Practices**: Follow established patterns and avoid anti-patterns
- **Comment Work**: Include clear, meaningful comments explaining complex logic
- **Review Changes**: Think twice about every change before committing
- **Test Rigorously**: Verify all functionality works as expected
- **Be Thorough**: Complete all aspects of implementation without shortcuts
- **Implement Fully**: Never simplify or reduce the scope of user requirements
- **Maintain Quality**: Never compromise on code quality even under time pressure
- **Follow Architecture**: Adhere to the established MVC pattern and module structure
- **Consider Performance**: Optimize where appropriate without premature optimization
- **Security First**: Consider security implications in all code written

## Build, Lint, & Test Commands
```bash
# Install dependencies
pip install -r requirements.txt

# Run application
python src/main.py

# Run tests
pytest tests/
pytest tests/test_models.py  # Run specific test file
pytest tests/test_integration.py::test_specific_function  # Run single test

# Generate documentation
sphinx-build -b html docs/ docs/api-docs/
```

## Code Style Guidelines
- **Language**: Python 3.9+
- **Formatting**: Follow PEP 8 standards
- **Imports**: Group imports (stdlib, third-party, local) with blank lines between
- **Type Hints**: Always use type hints for function arguments and return values
- **Docstrings**: Required for all functions/classes (including parameters and return values)
- **Error Handling**: Use specific exceptions with informative messages
- **Variable Naming**: snake_case for variables/functions, CamelCase for classes
- **Architecture**: Follow Model-View-Controller (MVC) pattern
- **Modules**: Keep each application module independent with clear APIs

## Testing Standards
- Use pytest for all tests
- Each module should have separate test files (models, views, controllers)
- Aim for 80%+ test coverage for all functionality