"""
Versions module AppConfig integration
"""
from django.apps import AppConfig


class VersionsAppConfig(AppConfig):
    """
    Django AppConfig integration for `versions` module
    """
    name = 'versions'
    verbose_name = "versions"
