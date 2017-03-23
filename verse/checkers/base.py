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
    name = None  # has to be unique
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
        :rtype: str
        """
        for version in self.get_versions():
            parsed_version = parse_version(version)
            if (not parsed_version.is_postrelease and
                    not parsed_version.is_prerelease):
                return version

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
            parsed_version = parse_version(version)
            major = parsed_version._version.release[0]

            if (not parsed_version.is_postrelease and
                    not parsed_version.is_prerelease):
                if lookup is None:
                    lookup = major

                if lookup == major:
                    major_versions[str(major)] = version

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
            parsed_version = parse_version(version)
            major, minor = parsed_version._version.release[:2]

            if (not parsed_version.is_postrelease and
                    not parsed_version.is_prerelease):
                # First run overall or first on new major version,
                # when we don't know the highest minor version is (3.0 -> 2.7)
                if lookup is None or lookup == (major, None):
                    lookup = (major, minor)

                if lookup == (major, minor):
                    minor_ver = '{}.{}'.format(major, minor)
                    minor_versions[minor_ver] = version

                    # We went through all major versions
                    if lookup == (0, 0):
                        break

                    if minor == 0:
                        lookup = (lookup[0] - 1, None)
                    else:
                        lookup = (lookup[0], lookup[1] - 1)

        return minor_versions
