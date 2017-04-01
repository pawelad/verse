"""
Test `checkers.projects.frontend_frameworks` file
"""
import pytest

from checkers import base
from checkers.projects import frontend_frameworks


class TestBootstrapVersionChecker:
    """
    Test `frontend_frameworks.BootstrapVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return frontend_frameworks.BootstrapVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'bootstrap'
        assert instance.homepage == 'http://getbootstrap.com/'
        assert instance.repository == 'https://github.com/twbs/bootstrap'


class TestFontAwesomeVersionChecker:
    """
    Test `frontend_frameworks.FontAwesomeVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return frontend_frameworks.FontAwesomeVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'font-awesome'
        assert instance.homepage == 'http://fontawesome.io/'
        assert (
            instance.repository ==
            'https://github.com/FortAwesome/Font-Awesome'
        )

    def test_class_normalize_tag_name_method(self, instance):
        """Test class `_normalize_tag_name()` method"""
        assert instance._normalize_tag_name('v1.2.3') == 'v1.2.3'
        assert instance._normalize_tag_name('4.1.0') == ''

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=instance._normalize_tag_name
        )


class TestMDLVersionChecker:
    """
    Test `frontend_frameworks.MDLVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return frontend_frameworks.MDLVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'mdl'
        assert instance.homepage == 'https://getmdl.io/'
        assert (
            instance.repository ==
            'https://github.com/google/material-design-lite'
        )
