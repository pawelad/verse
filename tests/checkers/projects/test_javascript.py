"""
Test `checkers.projects.javascript` file
"""
from checkers.projects import javascript


class TestjQueryVersionChecker:
    """Test `javascript.jQueryVersionChecker` class"""
    instance = javascript.jQueryVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'jquery'
        assert self.instance.homepage == 'https://jquery.com/'
        assert self.instance.repository == 'https://github.com/jquery/jquery'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()


class TestNodeJSVersionChecker:
    """Test `javascript.NodeJSVersionChecker` class"""
    instance = javascript.NodeJSVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'nodejs'
        assert self.instance.homepage == 'https://nodejs.org/'
        assert self.instance.repository == 'https://github.com/nodejs/node'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()


class TestReactVersionChecker:
    """Test `javascript.ReactVersionChecker` class"""
    instance = javascript.ReactVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'react'
        assert self.instance.homepage == 'https://facebook.github.io/react/'
        assert self.instance.repository == 'https://github.com/facebook/react'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()
