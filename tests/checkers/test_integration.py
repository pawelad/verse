"""
Checkers integration tests
"""
import pytest

from checkers.projects import AVAILABLE_CHECKERS


@pytest.mark.integration_tests
def test_checkers_integration():
    """
    Runs integration tests on all available checkers and makes sure
    that all of `get_latest_version()`, `get_latest_major_versions()`
    and `get_latest_minor_versions()` don't raise an exception.
    
    This is run only when '--integration-tests' argument is passed to pytest
    """
    for project in AVAILABLE_CHECKERS.values():
        assert project.get_latest_version()
        assert project.get_latest_major_versions()
        assert project.get_latest_minor_versions()
