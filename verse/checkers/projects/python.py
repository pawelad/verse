"""
Checkers for Python related projects
"""
from checkers.base import BaseVersionChecker


class PythonVersionChecker(BaseVersionChecker):
    """
    Python project checker
    """
    name = 'python'
    homepage = 'https://www.python.org/'
    repository = 'https://github.com/python/cpython'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()


class DjangoVersionChecker(BaseVersionChecker):
    """
    Django project checker
    """
    name = 'django'
    homepage = 'https://www.djangoproject.com/'
    repository = 'https://github.com/django/django'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()


class FlaskVersionChecker(BaseVersionChecker):
    """
    Flask project checker
    """
    name = 'flask'
    homepage = 'http://flask.pocoo.org/'
    repository = 'https://github.com/pallets/flask'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()
