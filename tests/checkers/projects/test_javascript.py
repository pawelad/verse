"""
Test `checkers.projects.javascript` file
"""
import operator

import pytest
from packaging.version import Version

from checkers import base
from checkers.projects import javascript


class TestAngularVersionChecker:
    """
    Test `javascript.AngularVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return javascript.AngularVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'angular'
        assert instance.homepage == 'https://angular.io/'
        assert instance.repository == 'https://github.com/angular/angular'


class TestBackboneVersionChecker:
    """
    Test `javascript.BackboneVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return javascript.BackboneVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'backbone'
        assert instance.homepage == 'http://backbonejs.org/'
        assert instance.repository == 'https://github.com/jashkenas/backbone'


class TestD3JSVersionChecker:
    """
    Test `javascript.D3JSVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return javascript.D3JSVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'd3js'
        assert instance.homepage == 'https://d3js.org/'
        assert instance.repository == 'https://github.com/d3/d3'


class TestEmberJSVersionChecker:
    """
    Test `javascript.EmberJSVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return javascript.EmberJSVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'emberjs'
        assert instance.homepage == 'https://www.emberjs.com/'
        assert instance.repository == 'https://github.com/emberjs/ember.js'


class TestjQueryVersionChecker:
    """
    Test `javascript.jQueryVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return javascript.jQueryVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'jquery'
        assert instance.homepage == 'https://jquery.com/'
        assert instance.repository == 'https://github.com/jquery/jquery'


class TestNodeJSVersionChecker:
    """
    Test `javascript.NodeJSVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return javascript.NodeJSVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'nodejs'
        assert instance.homepage == 'https://nodejs.org/'
        assert instance.repository == 'https://github.com/nodejs/node'


class TestReactVersionChecker:
    """
    Test `javascript.ReactVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return javascript.ReactVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'react'
        assert instance.homepage == 'https://facebook.github.io/react/'
        assert instance.repository == 'https://github.com/facebook/react'


class TestVueJSVersionChecker:
    """
    Test `javascript.VueJSVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return javascript.VueJSVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'vuejs'
        assert instance.homepage == 'http://vuejs.org/'
        assert instance.repository == 'https://github.com/vuejs/vue'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        versions = [
            Version(v) for v in
            ['v1.3.2', 'v1.3.1', 'v1.3.0', '3.2.8']
        ]
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags', return_value=versions,
        )

        sorted_versions = sorted(
            versions,
            key=operator.attrgetter('base_version'),
            reverse=True,
        )

        assert instance.get_versions() == sorted_versions

        mocked_get_github_tags.assert_called_once_with()
