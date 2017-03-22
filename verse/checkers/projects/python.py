"""
checkers for Python related projects
"""
from checkers.base import BaseProject


class PythonProject(BaseProject):
    """
    Python checker project
    """
    name = 'python'
    homepage = 'https://www.python.org/'
    repository = 'https://github.com/python/cpython'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()


class DjangoProject(BaseProject):
    """
    Django checker project
    """
    name = 'django'
    homepage = 'https://www.djangoproject.com/'
    repository = 'https://github.com/django/django'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()
