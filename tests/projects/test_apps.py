"""
Test `projects.apps` file
"""
from django.apps import AppConfig
from django.apps import apps as verse_apps

from projects import utils


def test_projects_app_config():
    """Test 'projects' module `AppConfig` instance"""
    projects_app_config = verse_apps.get_app_config('projects')

    assert isinstance(projects_app_config, AppConfig)
    assert projects_app_config.name == 'projects'
    assert projects_app_config.verbose_name == 'Projects'


def test_projects_app_ready(mocker):
    """Test `projects` module `AppConfig.ready()` method"""
    # Project lists should be deleted from cache on app restart
    mocked_cache_set = mocker.patch('projects.apps.cache.delete')

    versions_app_config = verse_apps.get_app_config('projects')
    versions_app_config.ready()

    mocked_cache_set.assert_called_once_with(
        key=utils.AVAILABLE_PROJECTS_KEY,
    )
