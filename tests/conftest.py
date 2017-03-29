"""
Verse pytest configuration
"""
import pytest


def pytest_addoption(parser):
    """
    Adds a custom pytest command line argument
    """
    parser.addoption(
        '--integration-tests',
        action='store_true',
        default=False,
        help="Run integration tests",
    )


def pytest_configure(config):
    """
    Adds a custom pytest marker
    """
    config.addinivalue_line(
        'markers',
        "integration_tests: mark integration tests",
    )


def pytest_runtest_setup(item):
    """
    Adds a custom pytest marker
    """
    integration_tests_marker = item.get_marker("integration_tests")
    if integration_tests_marker is not None:
        if not item.config.getoption('--integration-tests'):
            pytest.skip("Skipping integration tests")
