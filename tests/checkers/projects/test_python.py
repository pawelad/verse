"""
Test `checkers.projects.python` file
"""
import pytest

from checkers.projects import python


class TestPythonVersionChecker:
    """
    Test `python.PythonVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return python.PythonVersionChecker()

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'python'
        assert instance.homepage == 'https://www.python.org/'
        assert instance.repository == 'https://github.com/python/cpython'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with()


class TestAnsibleVersionChecker:
    """
    Test `python.AnsibleVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return python.AnsibleVersionChecker()

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'ansible'
        assert instance.homepage == 'https://www.ansible.com/'
        assert instance.repository == 'https://github.com/ansible/ansible'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with()


class TestCeleryVersionChecker:
    """
    Test `python.CeleryVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return python.CeleryVersionChecker()

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'celery'
        assert instance.homepage == 'http://www.celeryproject.org/'
        assert instance.repository == 'https://github.com/celery/celery'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with()


class TestDjangoVersionChecker:
    """
    Test `python.DjangoVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return python.DjangoVersionChecker()

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'django'
        assert instance.homepage == 'https://www.djangoproject.com/'
        assert instance.repository == 'https://github.com/django/django'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with()


class TestDjangoRESTFrameworkVersionChecker:
    """
    Test `python.DjangoRESTFrameworkVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return python.DjangoRESTFrameworkVersionChecker()

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'django-rest-framework'
        assert instance.homepage == 'http://www.django-rest-framework.org/'
        assert (
            instance.repository ==
            'https://github.com/tomchristie/django-rest-framework'
        )

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with()


class TestFlaskVersionChecker:
    """
    Test `python.FlaskVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return python.FlaskVersionChecker()

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'flask'
        assert instance.homepage == 'http://flask.pocoo.org/'
        assert instance.repository == 'https://github.com/pallets/flask'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with()


class TestGunicornVersionChecker:
    """
    Test `python.GunicornVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return python.GunicornVersionChecker()

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'gunicorn'
        assert instance.homepage == 'http://gunicorn.org/'
        assert instance.repository == 'https://github.com/benoitc/gunicorn'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with()


class TestRequestsVersionChecker:
    """
    Test `python.RequestsVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return python.RequestsVersionChecker()

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'requests'
        assert instance.homepage == 'http://docs.python-requests.org/'
        assert (
            instance.repository ==
            'https://github.com/kennethreitz/requests'
        )

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with()


class TestScrapyVersionChecker:
    """
    Test `python.ScrapyVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return python.ScrapyVersionChecker()

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'scrapy'
        assert instance.homepage == 'https://scrapy.org/'
        assert instance.repository == 'https://github.com/scrapy/scrapy'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with()
