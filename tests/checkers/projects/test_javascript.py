"""
Test `checkers.projects.javascript` file
"""
import operator

from packaging.version import Version

from checkers.projects import javascript


class TestAngularVersionChecker:
    """Test `javascript.AngularVersionChecker` class"""
    instance = javascript.AngularVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'angular'
        assert self.instance.homepage == 'https://angular.io/'
        assert self.instance.repository == 'https://github.com/angular/angular'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()


class TestBackboneVersionChecker:
    """Test `javascript.BackboneVersionChecker` class"""
    instance = javascript.BackboneVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'backbone'
        assert self.instance.homepage == 'http://backbonejs.org/'
        assert (
            self.instance.repository ==
            'https://github.com/jashkenas/backbone'
        )

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()


class TestD3JSVersionChecker:
    """Test `javascript.D3JSVersionChecker` class"""
    instance = javascript.D3JSVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'd3js'
        assert self.instance.homepage == 'https://d3js.org/'
        assert self.instance.repository == 'https://github.com/d3/d3'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()


class TestEmberJSVersionChecker:
    """Test `javascript.EmberJSVersionChecker` class"""
    instance = javascript.EmberJSVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'emberjs'
        assert self.instance.homepage == 'https://www.emberjs.com/'
        assert (
            self.instance.repository ==
            'https://github.com/emberjs/ember.js'
        )

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()


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


class TestVueJSVersionChecker:
    """Test `javascript.VueJSVersionChecker` class"""
    instance = javascript.VueJSVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'vuejs'
        assert self.instance.homepage == 'http://vuejs.org/'
        assert self.instance.repository == 'https://github.com/vuejs/vue'

    def test_class_get_versions_method(self, mocker):
        """Test class `get_versions()` method"""
        versions = [
            Version(v) for v in
            ['v1.3.2', 'v1.3.1', 'v1.3.0', '3.2.8']
        ]
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags', return_value=versions,
        )

        sorted_versions = sorted(
            versions,
            key=operator.attrgetter('base_version'),
            reverse=True,
        )

        assert self.instance.get_versions() == sorted_versions

        mocked_get_github_tags.assert_called_once_with()
