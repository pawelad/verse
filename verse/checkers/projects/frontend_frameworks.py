"""
Checkers for frontend framework projects
"""
from checkers.base import BaseVersionChecker


class BootstrapVersionChecker(BaseVersionChecker):
    """
    Bootstrap project checker
    """
    name = 'bootstrap'
    homepage = 'http://getbootstrap.com/'
    repository = 'https://github.com/twbs/bootstrap'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()


class MDLVersionChecker(BaseVersionChecker):
    """
    Material Design Lite project checker
    """
    name = 'mdl'
    homepage = 'https://getmdl.io/'
    repository = 'https://github.com/google/material-design-lite'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()
