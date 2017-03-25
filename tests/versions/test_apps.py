"""
Test `versions.apps` file
"""
from django.apps import AppConfig
from django.apps import apps as verse_apps
from django.core.cache import cache
from django.utils.crypto import get_random_string

from versions import utils


def test_versions_app_config():
    """Test 'versions' module `AppConfig` instance"""
    versions_app_config = verse_apps.get_app_config('versions')

    assert isinstance(versions_app_config, AppConfig)
    assert versions_app_config.name == 'versions'
    assert versions_app_config.verbose_name == 'Project versions'


def test_versions_app_ready():
    """Test `versions` module `AppConfig.ready()` method"""
    # Project lists should be deleted from cache on app restart
    cache.set(
        key=utils.AVAILABLE_PROJECTS_KEY,
        value=get_random_string(),
    )

    versions_app_config = verse_apps.get_app_config('versions')
    versions_app_config.ready()

    assert cache.get(utils.AVAILABLE_PROJECTS_KEY) is None
