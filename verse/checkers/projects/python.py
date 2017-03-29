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


class AnsibleVersionChecker(BaseVersionChecker):
    """
    Ansible project checker
    """
    name = 'ansible'
    homepage = 'https://www.ansible.com/'
    repository = 'https://github.com/ansible/ansible'

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


class GunicornVersionChecker(BaseVersionChecker):
    """
    Gunicorn project checker
    """
    name = 'gunicorn'
    homepage = 'http://gunicorn.org/'
    repository = 'https://github.com/benoitc/gunicorn'

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

    @staticmethod
    def _normalize_tag_name(name):
        """
        Normalizes GitHub tag name to be a PEP 404 compliant version name

        :param name: tag name
        :type name: str
        :returns: normalized version name
        :rtype: str
        """
        # There is only one version without 'v' in front of it which appears
        # at the bottom - '2.0'
        if name == '2.0':
            return ''

        return name

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags(normalize_func=self._normalize_tag_name)


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
