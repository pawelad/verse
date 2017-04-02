"""
Projects module AppConfig integration
"""
from contextlib import suppress

from django.apps import AppConfig
from django.core.cache import cache

import redis

from projects import utils


class ProjectsAppConfig(AppConfig):
    """
    Django AppConfig integration for `projects` module
    """
    name = 'projects'
    verbose_name = 'Projects'

    def ready(self):
        # Delete cached projects list
        with suppress(redis.exceptions.ConnectionError):
            cache.delete(key=utils.AVAILABLE_PROJECTS_KEY)
