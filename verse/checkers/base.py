"""
Checkers module base classes
"""
from abc import ABCMeta, abstractmethod

from packaging.version import Version, InvalidVersion

from checkers.utils import github_client, deconstruct_github_url


class BaseVersionChecker(metaclass=ABCMeta):
    """
    Base checker abstract class that all checkers should inherit from
    """
    name = None
    slug = None  # has to be unique
    homepage = None
    repository = None

    def __init__(self, name=None, slug=None, homepage=None, repository=None):
        """
        Save passed arguments on initialization

        :param name: project name
        :type name: str
        :param slug: project slug
        :type slug: str
        :param homepage: project homepage URL
        :type homepage: str
        :param repository: project repository URL
        :type repository: str
        """
        if name:
            self.name = name
        if slug:
            self.slug = slug
        if homepage:
            self.homepage = homepage
        if repository:
            self.repository = repository

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
        :raises ValueError: when result of 'get_versions()' isn't sorted
        """
        major_versions = dict()
        last = None

        for version in self.get_versions():
            if not version.is_postrelease and not version.is_prerelease:
                major = version._version.release[0]

                if last != major:
                    # If it's already added then the versions aren't sorted
                    if str(major) in major_versions:
                        raise ValueError(
                            "Result of 'get_versions()' isn't "
                            "sorted:  {}".format(version)
                        )

                    major_versions[str(major)] = str(version)
                    last = major

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
        :raises ValueError: when result of 'get_versions()' isn't sorted
        """
        minor_versions = dict()
        last = None

        for version in self.get_versions():
            if not version.is_postrelease and not version.is_prerelease:
                major, minor = version._version.release[:2]

                if last != (major, minor):
                    minor_version = '{}.{}'.format(major, minor)

                    # If it's already added then the versions aren't sorted
                    if minor_version in minor_versions:
                        raise ValueError(
                            "Result of 'get_versions()' isn't "
                            "sorted:  {}".format(version)
                        )

                    minor_versions[minor_version] = str(version)

                    last = (major, minor)

        return minor_versions


class GitHubVersionChecker(BaseVersionChecker):
    """
    Checker class that takes available versions from GitHub tags
    """
    def _get_github_tags(self, github_url=None, normalize_func=None):
        """
        Yields GitHub tag names, serialized to `Version` object

        :param github_url: project GitHub repository URL
        :type github_url: str
        :param normalize_func: function that normalizes tag name
        :type normalize_func: callable
        :returns: generator of project versions
        :rtype: generator of packaging.version.Version
        :raises ValueError: when passed URL is not a GitHub repository
        """
        if not github_url:
            github_url = self.repository

        owner, name = deconstruct_github_url(github_url)
        tags = github_client.repository(owner, name).iter_tags()
        for tag in tags:
            if normalize_func:
                name = normalize_func(tag.name)
            else:
                name = tag.name

            # Add a minor version if it's not there, i.e. v1 -> v1.0
            if name and len(name.split('.')) == 1:
                name += '.0'

            try:
                version = Version(name)
            except InvalidVersion:
                continue

            yield version

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()
