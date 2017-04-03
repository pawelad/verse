"""
Checkers for Python related projects
"""
from checkers import base


class PythonVersionChecker(base.GitHubVersionChecker):
    """
    Python project checker
    """
    name = 'Python'
    slug = 'python'
    homepage = 'https://www.python.org/'
    repository = 'https://github.com/python/cpython'


class AnsibleVersionChecker(base.GitHubVersionChecker):
    """
    Ansible project checker
    """
    name = 'Ansible'
    slug = 'ansible'
    homepage = 'https://www.ansible.com/'
    repository = 'https://github.com/ansible/ansible'


class CeleryVersionChecker(base.GitHubVersionChecker):
    """
    Celery project checker
    """
    name = 'Celery'
    slug = 'celery'
    homepage = 'http://www.celeryproject.org/'
    repository = 'https://github.com/celery/celery'


class DjangoVersionChecker(base.GitHubVersionChecker):
    """
    Django project checker
    """
    name = 'Django'
    slug = 'django'
    homepage = 'https://www.djangoproject.com/'
    repository = 'https://github.com/django/django'


class DjangoRESTFrameworkVersionChecker(base.GitHubVersionChecker):
    """
    Django REST Framework project checker
    """
    name = 'Django REST Framework'
    slug = 'django-rest-framework'
    homepage = 'http://www.django-rest-framework.org/'
    repository = 'https://github.com/tomchristie/django-rest-framework'


class FlaskVersionChecker(base.GitHubVersionChecker):
    """
    Flask project checker
    """
    name = 'Flask'
    slug = 'flask'
    homepage = 'http://flask.pocoo.org/'
    repository = 'https://github.com/pallets/flask'


class GunicornVersionChecker(base.GitHubVersionChecker):
    """
    Gunicorn project checker
    """
    name = 'Gunicorn'
    slug = 'gunicorn'
    homepage = 'http://gunicorn.org/'
    repository = 'https://github.com/benoitc/gunicorn'


class RequestsVersionChecker(base.GitHubVersionChecker):
    """
    Requests project checker
    """
    name = 'Requests'
    slug = 'python-requests'
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


class ScrapyVersionChecker(base.GitHubVersionChecker):
    """
    Scrapy project checker
    """
    name = 'Scrapy'
    slug = 'scrapy'
    homepage = 'https://scrapy.org/'
    repository = 'https://github.com/scrapy/scrapy'
