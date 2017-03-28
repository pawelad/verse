"""
Checkers for Go related projects
"""
from checkers.base import BaseVersionChecker
from checkers.utils import remove_prefix


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
