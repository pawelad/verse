"""
checker module base classes
"""
from abc import ABCMeta, abstractmethod

from packaging.version import parse as parse_version

from checkers.utils import remove_prefix, github_client


class BaseProject(metaclass=ABCMeta):
    """
    Base project abstract class that all projects should inherit from
    """
    name = None
    homepage = None
    repository = None

    def _get_github_tags(self, github_url=None):
        """
        Returns GitHub tags, normalized to `SimpleVersion` format

        :param github_url: project GitHub repository URL
        :type github_url: str
        :returns: generator of project versions
        :rtype: generator of str
        """
        if not github_url:
            github_url = self.repository

        github_prefix = 'https://github.com/'
        if not github_url.startswith(github_prefix):
            raise ValueError(
                "Passed URL is not a GitHub repository: {}".format(github_url)
            )

        owner, repo = remove_prefix(github_url, github_prefix).split('/')
        tags = github_client.repository(owner, repo).iter_tags()
        for tag in tags:
            yield tag.name

    @abstractmethod
    def get_versions(self):
        """
        Returns an iterable of *sorted* project versions

        :returns: a sorted iterable of versions
        :rtype: iterable of str
        """
        raise NotImplementedError(
            "You need to implement 'get_versions()' method in classes "
            "that inherit from 'BaseProject'"
        )

    def get_latest_version(self):
        """
        Returns latest project version

        :returns: latest version
        :rtype: packaging.version.Version
        """
        for version in self.get_versions():
            parsed_version = parse_version(version)
            if (not parsed_version.is_postrelease and
                    not parsed_version.is_prerelease):
                return parsed_version
