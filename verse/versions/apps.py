"""
Versions module AppConfig integration
"""
from contextlib import suppress

from django.apps import AppConfig
from django.core.cache import cache

import redis

from versions import utils


class VersionsAppConfig(AppConfig):
    """
    Django AppConfig integration for `versions` module
    """
    name = 'versions'
    verbose_name = 'Project versions'

    def ready(self):
        # Delete cached projects list
        with suppress(redis.exceptions.ConnectionError):
            cache.delete(key=utils.AVAILABLE_PROJECTS_KEY)
