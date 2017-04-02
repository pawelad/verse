"""
Test `versions.utils` file
"""
from django.utils.crypto import get_random_string

import pytest

from checkers.projects import PythonVersionChecker, DjangoVersionChecker
from versions import utils


available_projects = {
    'python': PythonVersionChecker(),
    'django': DjangoVersionChecker(),
}


def test_get_projects_function(mocker):
    """Test `utils.get_projects()` function"""
    mocker.patch('versions.utils.AVAILABLE_CHECKERS', available_projects)

    projects = utils.get_projects(request=None)

    assert projects == {
        'python': {
            'homepage': 'https://www.python.org/',
            'latest': '/projects/python/',
            'latest_major': '/projects/python/major/',
            'latest_minor': '/projects/python/minor/'
        },
        'django': {
            'homepage': 'https://www.djangoproject.com/',
            'latest': '/projects/django/',
            'latest_major': '/projects/django/major/',
            'latest_minor': '/projects/django/minor/'
        },
    }


values = [
    ('python', False),
    ('test', False),
    (get_random_string(), False),
    ('', True),
    (None, True),
]


@pytest.mark.parametrize('project, raising', values)
def test_get_latest_version_key_function(project, raising):
    """Test `utils.get_latest_version_key()` function"""
    if raising:
        with pytest.raises(ValueError):
            utils.get_latest_version_key(project)
    else:
        assert (
            utils.get_latest_version_key(project) ==
            '{project}_latest_version'.format(project=project)
        )


@pytest.mark.parametrize('project, raising', values)
def test_get_latest_major_versions_key_function(project, raising):
    """Test `utils.get_latest_major_versions_key()` function"""
    if raising:
        with pytest.raises(ValueError):
            utils.get_latest_major_versions_key(project)
    else:
        assert (
            utils.get_latest_major_versions_key(project) ==
            '{project}_latest_major_versions'.format(project=project)
        )


@pytest.mark.parametrize('project, raising', values)
def test_get_latest_minor_versions_key_function(project, raising):
    """Test `utils.get_latest_minor_versions_key()` function"""
    if raising:
        with pytest.raises(ValueError):
            utils.get_latest_minor_versions_key(project)
    else:
        assert (
            utils.get_latest_minor_versions_key(project) ==
            '{project}_latest_minor_versions'.format(project=project)
        )
