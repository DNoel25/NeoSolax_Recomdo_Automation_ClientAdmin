import pytest
from confest import MainTestRunner

if __name__ == "__main__":
    # Setup WebDriver and login once
    MainTestRunner.setup()

    # Run all tests sequentially
    exit_code = pytest.main([
        "Tests/test_layered_navigation.py",
        "Tests/Test_Search_Results_Management/test_manual_suggestion",  # Add other test files here
        # "Tests/test_another_module.py",
    ])

    # Teardown WebDriver after all tests
    MainTestRunner.teardown()

    # Exit with the pytest exit code
    exit(exit_code)
