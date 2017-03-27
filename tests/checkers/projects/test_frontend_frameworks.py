"""
Test `checkers.projects.frontend_frameworks` file
"""
from checkers.projects import frontend_frameworks


class TestBootstrapVersionChecker:
    """Test `frontend_frameworks.BootstrapVersionChecker` class"""
    instance = frontend_frameworks.BootstrapVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'bootstrap'
        assert self.instance.homepage == 'http://getbootstrap.com/'
        assert self.instance.repository == 'https://github.com/twbs/bootstrap'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()


class TestMDLVersionChecker:
    """Test `frontend_frameworks.MDLVersionChecker` class"""
    instance = frontend_frameworks.MDLVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'mdl'
        assert self.instance.homepage == 'https://getmdl.io/'
        assert (
            self.instance.repository ==
            'https://github.com/google/material-design-lite'
        )

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()


class TestFontAwesomeVersionChecker:
    """Test `frontend_frameworks.FontAwesomeVersionChecker` class"""
    instance = frontend_frameworks.FontAwesomeVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'font-awesome'
        assert self.instance.homepage == 'http://fontawesome.io/'
        assert (
            self.instance.repository ==
            'https://github.com/FortAwesome/Font-Awesome'
        )

    def test_class_normalize_tag_name_method(self):
        """Test class `_normalize_tag_name()` method"""
        assert self.instance._normalize_tag_name('v1.2.3') == 'v1.2.3'
        assert self.instance._normalize_tag_name('4.1.0') == ''

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=self.instance._normalize_tag_name
        )
