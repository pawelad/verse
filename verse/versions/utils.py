"""
Versions module utils file
"""


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
