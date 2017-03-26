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


class CeleryVersionChecker(BaseVersionChecker):
    """
    Celery project checker
    """
    name = 'celery'
    homepage = 'http://www.celeryproject.org/'
    repository = 'https://github.com/celery/celery'

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


class DjangoRESTFrameworkVersionChecker(BaseVersionChecker):
    """
    Django REST Framework project checker
    """
    name = 'django-rest-framework'
    homepage = 'http://www.django-rest-framework.org/'
    repository = 'https://github.com/tomchristie/django-rest-framework'

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


class RequestsVersionChecker(BaseVersionChecker):
    """
    Requests project checker
    """
    name = 'requests'
    homepage = 'http://docs.python-requests.org/'
    repository = 'https://github.com/kennethreitz/requests'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()


class ScrapyVersionChecker(BaseVersionChecker):
    """
    Scrapy project checker
    """
    name = 'scrapy'
    homepage = 'https://scrapy.org/'
    repository = 'https://github.com/scrapy/scrapy'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()
