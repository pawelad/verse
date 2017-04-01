"""
Checker module misc utilities
"""
from urllib.parse import urljoin

from decouple import config
from github3 import GitHub


GITHUB_PREFIX = 'https://github.com/'


def remove_prefix(text, prefix, silent=True):
    """
    Helper method for removing a prefix from a string.

    :param text: text
    :type text: str
    :param prefix: prefix that needs to be removed
    :type prefix: str
    :param silent: determines whether function should fail silently
    :type silent: bool
    :returns: passed text with removed prefix
    :rtype: str
    :raises ValueError: if the string doesn't start with the passed prefix
                        and `silent` is set to False
    """
    if text.startswith(prefix):
        return text[len(prefix):]

    if silent:
        return text

    raise ValueError(
        "String doesn't start with the passed prefix - "
        "string: {}; prefix: {}".format(text, prefix)
    )


def get_github_api_client():
    """
    Helper method for initializing GitHub API client

    :return: github3.Github
    """
    token = config('GITHUB_TOKEN')
    return GitHub(token=token)


github_client = get_github_api_client()


def deconstruct_github_url(url):
    """
    Helper method for deconstructing GitHub repository URL and returning its
    owner and name
    
    :param url: GitHub repository URL
    :type url: str
    :returns: repository owner and name
    :rtype: tuple
    """
    if not url.startswith(GITHUB_PREFIX):
        raise ValueError(
            "Passed URL is not a GitHub repository: {}".format(url)
        )

    owner, name = remove_prefix(url, GITHUB_PREFIX).split('/')[:2]

    return owner, name


def construct_github_url(owner, name):
    """
    Helper method for constructing GitHub repository URL from its owner
    and name

    :param owner: GitHub repository owner
    :type owner: str
    :param name: GitHub repository name
    :type name: str
    :returns: repository URL
    :rtype: str
    """
    return urljoin(
        GITHUB_PREFIX, '{}/{}'.format(owner, name),
    )
