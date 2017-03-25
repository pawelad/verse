"""
Versions module AppConfig integration
"""
from django.apps import AppConfig
from django.core.cache import cache

from versions import utils


class VersionsAppConfig(AppConfig):
    """
    Django AppConfig integration for `versions` module
    """
    name = 'versions'
    verbose_name = 'Project versions'

    def ready(self):
        # Delete cached projects list
        cache.delete(key=utils.AVAILABLE_PROJECTS_KEY)
