"""
Checker module misc utilities
"""
from urllib.parse import urljoin

from decouple import config
from github3 import GitHub


GITHUB_PREFIX = 'https://github.com/'


def remove_prefix(text, prefix, silent=True):
    """
    Helper function for removing a prefix from a string.

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


def get_all_subclasses(cls):
    """
    Helper function for getting all subclasses of passed class, including
    sub-sub-classes, etc.

    :param cls: class
    :type cls: class
    :returns: list of all subclasses
    :rtype: list
    """
    all_subclasses = list()
    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(get_all_subclasses(subclass))

    return all_subclasses


def get_github_api_client():
    """
    Helper function for initializing GitHub API client

    :return: github3.Github
    """
    token = config('GITHUB_TOKEN', default=None)
    return GitHub(token=token)


github_client = get_github_api_client()


def deconstruct_github_url(url):
    """
    Helper function for deconstructing GitHub repository URL and returning its
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

    owner, repo = remove_prefix(url, GITHUB_PREFIX).split('/')[:2]

    return owner, repo


def construct_github_url(owner, repo):
    """
    Helper function for constructing GitHub repository URL from its owner
    and name

    :param owner: GitHub repository owner
    :type owner: str
    :param repo: GitHub repository name
    :type repo: str
    :returns: repository URL
    :rtype: str
    """
    return urljoin(
        GITHUB_PREFIX, '{}/{}'.format(owner, repo),
    )
