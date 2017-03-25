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
    verbose_name = "versions"

    def ready(self):
        # Update available projects cache
        cache.set(
            key=utils.AVAILABLE_PROJECTS_KEY,
            value=utils.get_projects(),
            timeout=None,  # This will be invalidated in app restart
        )
