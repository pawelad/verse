"""
Checkers module base classes
"""
from abc import ABCMeta, abstractmethod

from packaging.version import parse as parse_version

from checkers.utils import remove_prefix, github_client


class BaseVersionChecker(metaclass=ABCMeta):
    """
    Base checker abstract class that all checkers should inherit from
    """
    name = None  # has to be unique
    homepage = None
    repository = None

    def _get_github_tags(self, github_url=None):
        """
        Yields GitHub tag names, serialized to `Version` object

        :param github_url: project GitHub repository URL
        :type github_url: str
        :returns: generator of project versions
        :rtype: generator of packaging.version.Version
        :raises ValueError: when passed URL is not a GitHub repository
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
            yield parse_version(tag.name)

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
            if not version.is_postrelease and not version.is_prerelease:
                return str(version)

    def get_latest_major_versions(self):
        """
        Returns a dictionary of latest major versions
        Example:
            {
                '2': '2.2.2',
                '1': '1.5.9',
            }

        :returns: dictionary of latest major versions
        :rtype: dict
        """
        major_versions = dict()
        lookup = None

        for version in self.get_versions():
            major = version._version.release[0]

            if not version.is_postrelease and not version.is_prerelease:
                if lookup is None:
                    lookup = major

                if lookup == major:
                    major_versions[str(major)] = str(version)

                    # We went through all major versions
                    if lookup == 0:
                        break
                    lookup -= 1

        return major_versions

    def get_latest_minor_versions(self):
        """
        Returns a dictionary of latest minor versions
        Example:
            {
                '2.2': '2.2.2',
                '2.1': '2.1.13',
                '2.0': '2.0.1',
                '1.1': '1.1.3',
                '1.0': '1.0.9',
            }

        :returns: dictionary of latest minor versions
        :rtype: dict
        """
        minor_versions = dict()
        lookup = None

        for version in self.get_versions():
            major, minor = version._version.release[:2]

            if not version.is_postrelease and not version.is_prerelease:
                # First run overall or first on new major version,
                # when we don't know the highest minor version is (3.0 -> 2.7)
                if lookup is None or lookup == (major, None):
                    lookup = (major, minor)

                if lookup == (major, minor):
                    minor_ver = '{}.{}'.format(major, minor)
                    minor_versions[minor_ver] = str(version)

                    # We went through all major versions
                    if lookup == (0, 0):
                        break

                    # Jump from X.0 to X-1.?
                    if minor == 0:
                        lookup = (lookup[0] - 1, None)
                    # Jump from X.N to X.N-1
                    else:
                        lookup = (lookup[0], lookup[1] - 1)

        return minor_versions
