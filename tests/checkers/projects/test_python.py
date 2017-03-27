"""
Test `checkers.projects.python` file
"""
from checkers.projects import python


class TestPythonVersionChecker:
    """Test `python.PythonVersionChecker` class"""
    instance = python.PythonVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'python'
        assert self.instance.homepage == 'https://www.python.org/'
        assert self.instance.repository == 'https://github.com/python/cpython'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()


class TestCeleryVersionChecker:
    """Test `python.CeleryVersionChecker` class"""
    instance = python.CeleryVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'celery'
        assert self.instance.homepage == 'http://www.celeryproject.org/'
        assert self.instance.repository == 'https://github.com/celery/celery'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()


class TestDjangoVersionChecker:
    """Test `python.DjangoVersionChecker` class"""
    instance = python.DjangoVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'django'
        assert self.instance.homepage == 'https://www.djangoproject.com/'
        assert self.instance.repository == 'https://github.com/django/django'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()


class TestDjangoRESTFrameworkVersionChecker:
    """Test `python.DjangoRESTFrameworkVersionChecker` class"""
    instance = python.DjangoRESTFrameworkVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'django-rest-framework'
        assert (
            self.instance.homepage ==
            'http://www.django-rest-framework.org/'
        )
        assert (
            self.instance.repository ==
            'https://github.com/tomchristie/django-rest-framework'
        )

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()


class TestFlaskVersionChecker:
    """Test `python.FlaskVersionChecker` class"""
    instance = python.FlaskVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'flask'
        assert self.instance.homepage == 'http://flask.pocoo.org/'
        assert self.instance.repository == 'https://github.com/pallets/flask'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()


class TestGunicornVersionChecker:
    """Test `python.GunicornVersionChecker` class"""
    instance = python.GunicornVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'gunicorn'
        assert self.instance.homepage == 'http://gunicorn.org/'
        assert (
            self.instance.repository ==
            'https://github.com/benoitc/gunicorn'
        )

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()


class TestRequestsVersionChecker:
    """Test `python.RequestsVersionChecker` class"""
    instance = python.RequestsVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'requests'
        assert self.instance.homepage == 'http://docs.python-requests.org/'
        assert (
            self.instance.repository ==
            'https://github.com/kennethreitz/requests'
        )

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()


class TestScrapyVersionChecker:
    """Test `python.ScrapyVersionChecker` class"""
    instance = python.ScrapyVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'scrapy'
        assert self.instance.homepage == 'https://scrapy.org/'
        assert self.instance.repository == 'https://github.com/scrapy/scrapy'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()
