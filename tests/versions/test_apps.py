"""
Test `versions.apps` file
"""
from django.apps import AppConfig
from django.apps import apps as verse_apps

from versions import utils


def test_versions_app_config():
    """Test 'versions' module `AppConfig` instance"""
    versions_app_config = verse_apps.get_app_config('versions')

    assert isinstance(versions_app_config, AppConfig)
    assert versions_app_config.name == 'versions'
    assert versions_app_config.verbose_name == 'Project versions'


def test_versions_app_ready(mocker):
    """Test `versions` module `AppConfig.ready()` method"""
    # Project lists should be deleted from cache on app restart
    mocked_cache_set = mocker.patch('versions.apps.cache.delete')

    versions_app_config = verse_apps.get_app_config('versions')
    versions_app_config.ready()

    mocked_cache_set.assert_called_once_with(
        key=utils.AVAILABLE_PROJECTS_KEY,
    )
