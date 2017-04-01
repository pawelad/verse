"""
Checkers for JavaSript related projects
"""
import operator

from checkers import base


class AngularVersionChecker(base.GitHubVersionChecker):
    """
    Angular project checker
    """
    name = 'angular'
    homepage = 'https://angular.io/'
    repository = 'https://github.com/angular/angular'


class BackboneVersionChecker(base.GitHubVersionChecker):
    """
    Backbone project checker
    """
    name = 'backbone'
    homepage = 'http://backbonejs.org/'
    repository = 'https://github.com/jashkenas/backbone'


class D3JSVersionChecker(base.GitHubVersionChecker):
    """
    D3.js project checker
    """
    name = 'd3js'
    homepage = 'https://d3js.org/'
    repository = 'https://github.com/d3/d3'


class EmberJSVersionChecker(base.GitHubVersionChecker):
    """
    Ember.js project checker
    """
    name = 'emberjs'
    homepage = 'https://www.emberjs.com/'
    repository = 'https://github.com/emberjs/ember.js'


class jQueryVersionChecker(base.GitHubVersionChecker):
    """
    jQuery project checker
    """
    name = 'jquery'
    homepage = 'https://jquery.com/'
    repository = 'https://github.com/jquery/jquery'


class NodeJSVersionChecker(base.GitHubVersionChecker):
    """
    Node.js project checker
    """
    name = 'nodejs'
    homepage = 'https://nodejs.org/'
    repository = 'https://github.com/nodejs/node'


class ReactVersionChecker(base.GitHubVersionChecker):
    """
    React project checker
    """
    name = 'react'
    homepage = 'https://facebook.github.io/react/'
    repository = 'https://github.com/facebook/react'


class VueJSVersionChecker(base.GitHubVersionChecker):
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
