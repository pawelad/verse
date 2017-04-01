"""
Versions module misc utilities
"""
from rest_framework.reverse import reverse

from checkers.projects import AVAILABLE_CHECKERS


def get_projects(request):
    """
    Helper method for generating a list available projects with links to
    their endpoints. It can only change with code addition and app restart so
    it makes sense to cache it on first request after restart.

    :param request: Django REST Framework request
    :type request: rest_framework.request.Request
    :returns: available projects
    :rtype: dict
    """
    projects = dict()
    for project in AVAILABLE_CHECKERS.values():
        latest_url = reverse(
            'versions:latest', args=[project.name], request=request,
        )
        major_versions_url = reverse(
            'versions:major', args=[project.name], request=request,
        )
        minor_versions_url = reverse(
            'versions:minor', args=[project.name], request=request,
        )

        projects[project.name] = {
            'homepage': project.homepage,
            'latest': latest_url,
            'latest_major': major_versions_url,
            'latest_minor': minor_versions_url,
        }

    return projects


AVAILABLE_PROJECTS_KEY = 'available_projects'


def get_latest_version_key(project_name):
    """
    Helper method for getting project latest version storage key

    :param project_name: project name
    :type project_name: str
    :returns: storage key for project latest version
    :rtype: str
    :raises ValueError: `when project_name` is empty
    """
    if not project_name:
        raise ValueError(
            "'project_name' can't be empty: {}".format(project_name)
        )

    return '{project}_latest_version'.format(project=project_name)


def get_latest_major_versions_key(project_name):
    """
    Helper method for getting project latest major versions storage key

    :param project_name: project name
    :type project_name: str
    :returns: storage key for project latest major versions
    :rtype: str
    :raises ValueError: `when project_name` is empty
    """
    if not project_name:
        raise ValueError(
            "'project_name' can't be empty: {}".format(project_name)
        )

    return '{project}_latest_major_versions'.format(project=project_name)


def get_latest_minor_versions_key(project_name):
    """
    Helper method for getting project latest minor versions storage key

    :param project_name: project name
    :type project_name: str
    :returns: storage key for project latest minor versions
    :rtype: str
    :raises ValueError: `when project_name` is empty
    """
    if not project_name:
        raise ValueError(
            "'project_name' can't be empty: {}".format(project_name)
        )

    return '{project}_latest_minor_versions'.format(project=project_name)
