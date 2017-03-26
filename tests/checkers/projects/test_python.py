"""
Test `checkers.projects.python` file
"""
from checkers.projects import python


def test_python_version_checker(mocker):
    """Test `python.PythonVersionChecker` class"""
    instance = python.PythonVersionChecker()

    assert instance.name == 'python'
    assert instance.homepage == 'https://www.python.org/'
    assert instance.repository == 'https://github.com/python/cpython'

    mocked_get_github_tags = mocker.patch.object(instance, '_get_github_tags')
    instance.get_latest_version()

    mocked_get_github_tags.assert_called_once_with()


def test_django_version_checker(mocker):
    """Test `python.DjangoVersionChecker` class"""
    instance = python.DjangoVersionChecker()

    assert instance.name == 'django'
    assert instance.homepage == 'https://www.djangoproject.com/'
    assert instance.repository == 'https://github.com/django/django'

    mocked_get_github_tags = mocker.patch.object(instance, '_get_github_tags')
    instance.get_latest_version()

    mocked_get_github_tags.assert_called_once_with()


def test_flask_version_checker(mocker):
    """Test `python.FlaskVersionChecker` class"""
    instance = python.FlaskVersionChecker()

    assert instance.name == 'flask'
    assert instance.homepage == 'http://flask.pocoo.org/'
    assert instance.repository == 'https://github.com/pallets/flask'

    mocked_get_github_tags = mocker.patch.object(instance, '_get_github_tags')
    instance.get_latest_version()

    mocked_get_github_tags.assert_called_once_with()