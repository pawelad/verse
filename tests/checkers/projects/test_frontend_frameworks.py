"""
Test `checkers.projects.frontend_frameworks` file
"""
from checkers.projects import frontend_frameworks


class TestBootstrapVersionChecker:
    """Test `webservers.BootstrapVersionChecker` class"""
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
