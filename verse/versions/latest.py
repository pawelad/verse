"""
Versions module helper functions regarding caching project latest versions
"""
from django.core.cache import cache

from versions import utils


def _get_latest(project, latest_type):
    """
    Helper method for returning latest versions data of given type

    :param project: project that we're inspecting
    :type project: checkers.base.BaseProject
    :param latest_type: type of 'latest' data (one of: 'version',
                        'major_versions', 'minor_versions')
    :type latest_type: str
    :returns: latest version data
    :rtype: dict
    """
    if latest_type == 'version':
        key = utils.get_latest_version_key(project.name)
        get_func = 'get_latest_version'
    elif latest_type == 'major_versions':
        key = utils.get_latest_major_versions_key(project.name)
        get_func = 'get_latest_major_versions'
    elif latest_type == 'minor_versions':
        key = utils.get_latest_minor_versions_key(project.name)
        get_func = 'get_latest_minor_versions'
    else:
        raise ValueError("Incorrect 'latest_type': {}".format(latest_type))

    return cache.get_or_set(key, getattr(project, get_func))


def get_latest_version(project):
    """
    Get project latest version, preferably from cache

    :param project: project that we're inspecting
    :type project: checkers.base.BaseProject
    :returns: latest version data
    :rtype: dict
    """
    return _get_latest(project, 'version')


def get_latest_major_versions(project):
    """
    Get project latest major versions, preferably from cache

    :param project: project that we're inspecting
    :type project: checkers.base.BaseProject
    :returns: latest version data
    :rtype: dict
    """
    return _get_latest(project, 'major_versions')


def get_latest_minor_versions(project):
    """
    Get project latest minor versions, preferably from cache

    :param project: project that we're inspecting
    :type project: checkers.base.BaseProject
    :returns: latest version data
    :rtype: dict
    """
    return _get_latest(project, 'minor_versions')
