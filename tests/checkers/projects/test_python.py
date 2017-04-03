"""
Test `checkers.projects.python` file
"""
import pytest

from checkers import base
from checkers.projects import python


class TestPythonVersionChecker:
    """
    Test `python.PythonVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return python.PythonVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'Python'
        assert instance.slug == 'python'
        assert instance.homepage == 'https://www.python.org/'
        assert instance.repository == 'https://github.com/python/cpython'


class TestAnsibleVersionChecker:
    """
    Test `python.AnsibleVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return python.AnsibleVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'Ansible'
        assert instance.slug == 'ansible'
        assert instance.homepage == 'https://www.ansible.com/'
        assert instance.repository == 'https://github.com/ansible/ansible'


class TestCeleryVersionChecker:
    """
    Test `python.CeleryVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return python.CeleryVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'Celery'
        assert instance.slug == 'celery'
        assert instance.homepage == 'http://www.celeryproject.org/'
        assert instance.repository == 'https://github.com/celery/celery'


class TestDjangoVersionChecker:
    """
    Test `python.DjangoVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return python.DjangoVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'Django'
        assert instance.slug == 'django'
        assert instance.homepage == 'https://www.djangoproject.com/'
        assert instance.repository == 'https://github.com/django/django'


class TestDjangoRESTFrameworkVersionChecker:
    """
    Test `python.DjangoRESTFrameworkVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return python.DjangoRESTFrameworkVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'Django REST Framework'
        assert instance.slug == 'django-rest-framework'
        assert instance.homepage == 'http://www.django-rest-framework.org/'
        assert (
            instance.repository ==
            'https://github.com/tomchristie/django-rest-framework'
        )


class TestFlaskVersionChecker:
    """
    Test `python.FlaskVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return python.FlaskVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'Flask'
        assert instance.slug == 'flask'
        assert instance.homepage == 'http://flask.pocoo.org/'
        assert instance.repository == 'https://github.com/pallets/flask'


class TestGunicornVersionChecker:
    """
    Test `python.GunicornVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return python.GunicornVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'Gunicorn'
        assert instance.slug == 'gunicorn'
        assert instance.homepage == 'http://gunicorn.org/'
        assert instance.repository == 'https://github.com/benoitc/gunicorn'


class TestRequestsVersionChecker:
    """
    Test `python.RequestsVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return python.RequestsVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'Requests'
        assert instance.slug == 'python-requests'
        assert instance.homepage == 'http://docs.python-requests.org/'
        assert (
            instance.repository ==
            'https://github.com/kennethreitz/requests'
        )

    def test_class_normalize_tag_name_method(self, instance):
        """Test class `_normalize_tag_name()` method"""
        assert instance._normalize_tag_name('2.0') == ''
        assert instance._normalize_tag_name('v2.0.0') == 'v2.0.0'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=instance._normalize_tag_name,
        )


class TestScrapyVersionChecker:
    """
    Test `python.ScrapyVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return python.ScrapyVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'Scrapy'
        assert instance.slug == 'scrapy'
        assert instance.homepage == 'https://scrapy.org/'
        assert instance.repository == 'https://github.com/scrapy/scrapy'
