"""
checker module utils
"""
from decouple import config
from github3 import GitHub


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
