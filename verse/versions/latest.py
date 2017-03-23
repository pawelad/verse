"""
Versions module helper functions regarding caching project latest versions
"""
from django.core.cache import cache

from versions import utils


def get_latest_version(project):
    """
    Get project latest version, preferably from cache

    :param project: project that we're inspecting
    :type project: checkers.base.BaseProject
    :returns: latest version data
    :rtype: dict
    """
    return cache.get_or_set(
        key=utils.get_latest_version_key(project.name),
        default=project.get_latest_version,
    )


def get_latest_major_versions(project):
    """
    Get project latest major versions, preferably from cache

    :param project: project that we're inspecting
    :type project: checkers.base.BaseProject
    :returns: latest version data
    :rtype: dict
    """
    return cache.get_or_set(
        key=utils.get_latest_major_versions_key(project.name),
        default=project.get_latest_major_versions,
    )


def get_latest_minor_versions(project):
    """
    Get project latest minor versions, preferably from cache

    :param project: project that we're inspecting
    :type project: checkers.base.BaseProject
    :returns: latest version data
    :rtype: dict
    """
    return cache.get_or_set(
        key=utils.get_latest_minor_versions_key(project.name),
        default=project.get_latest_minor_versions,
    )
