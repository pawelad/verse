"""
Checkers for Go related projects
"""
import operator

from checkers.base import BaseVersionChecker


class AngularVersionChecker(BaseVersionChecker):
    """
    Angular project checker
    """
    name = 'angular'
    homepage = 'https://angular.io/'
    repository = 'https://github.com/angular/angular'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()


class BackboneVersionChecker(BaseVersionChecker):
    """
    Backbone project checker
    """
    name = 'backbone'
    homepage = 'http://backbonejs.org/'
    repository = 'https://github.com/jashkenas/backbone'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()


class D3JSVersionChecker(BaseVersionChecker):
    """
    D3.js project checker
    """
    name = 'd3js'
    homepage = 'https://d3js.org/'
    repository = 'https://github.com/d3/d3'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()


class EmberJSVersionChecker(BaseVersionChecker):
    """
    Ember.js project checker
    """
    name = 'emberjs'
    homepage = 'https://www.emberjs.com/'
    repository = 'https://github.com/emberjs/ember.js'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()


class jQueryVersionChecker(BaseVersionChecker):
    """
    jQuery project checker
    """
    name = 'jquery'
    homepage = 'https://jquery.com/'
    repository = 'https://github.com/jquery/jquery'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()


class NodeJSVersionChecker(BaseVersionChecker):
    """
    Node.js project checker
    """
    name = 'nodejs'
    homepage = 'https://nodejs.org/'
    repository = 'https://github.com/nodejs/node'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()


class ReactVersionChecker(BaseVersionChecker):
    """
    React project checker
    """
    name = 'react'
    homepage = 'https://facebook.github.io/react/'
    repository = 'https://github.com/facebook/react'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()


class VueJSVersionChecker(BaseVersionChecker):
    """
    Vue.js project checker
    """
    name = 'vuejs'
    homepage = 'http://vuejs.org/'
    repository = 'https://github.com/vuejs/vue'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        # They randomly use and don't use 'r' prefix so we have to sort
        # versions manually
        versions = list(self._get_github_tags())
        versions.sort(
            key=operator.attrgetter('base_version'),
            reverse=True,
        )
        return versions
