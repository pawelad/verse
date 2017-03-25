"""
Versions module misc utilities
"""
from rest_framework.reverse import reverse

from checkers.projects import AVAILABLE_CHECKERS


def get_projects():
    """
    Helper method for generating a list available projects with links to
    their endpoints. It can only change with code addition of new projects so
    it makes sense to cache it on app restart.

    :returns: available projects
    :rtype: dict
    """
    projects = dict()
    for project_class in AVAILABLE_CHECKERS.values():
        project = project_class()
        latest_url = reverse('versions-detail', args=[project.name])
        major_versions_url = reverse('versions-major', args=[project.name])
        minor_versions_url = reverse('versions-minor', args=[project.name])

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
    """
    return '{project}_latest_version'.format(project=project_name)


def get_latest_major_versions_key(project_name):
    """
    Helper method for getting project latest major versions storage key

    :param project_name: project name
    :type project_name: str
    :returns: storage key for project latest major versions
    :rtype: str
    """
    return '{project}_latest_major_versions'.format(project=project_name)


def get_latest_minor_versions_key(project_name):
    """
    Helper method for getting project latest minor versions storage key

    :param project_name: project name
    :type project_name: str
    :returns: storage key for project latest minor versions
    :rtype: str
    """
    return '{project}_latest_minor_versions'.format(project=project_name)
