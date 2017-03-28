"""
Checkers for NoSQL projects
"""
from checkers.base import BaseVersionChecker


class RedisVersionChecker(BaseVersionChecker):
    """
    Redis project checker
    """
    name = 'redis'
    homepage = 'https://redis.io/'
    repository = 'https://github.com/antirez/redis'

    @staticmethod
    def _normalize_tag_name(name):
        """
        Normalizes GitHub tag name to be a PEP 404 compliant version name

        :param name: tag name
        :type name: str
        :returns: normalized version name
        :rtype: str
        """
        # All '1.3.x' versions start with 'v' *except* for '1.3.6',
        # which means that all with 'v' are at the very top while '1.3.6'
        # is at the very bottom. Ugh.
        if name == '1.3.6':
            return ''

        return name

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags(normalize_func=self._normalize_tag_name)

    def get_latest_version(self):
        """
        Returns latest project version

        :returns: latest version
        :rtype: packaging.version.Version
        """
        # Versions '1.3.x' have an 'v' in front of them which makes them
        # at the very top; this is very hackish but I *really* don't want
        # to sort versions in the backend every time
        for version in self.get_versions():
            if not version.is_postrelease and not version.is_prerelease:
                major = version._version.release[0]

                # We know for sure that the latest version is greater
                # then '1.x'
                if major > 1:
                    return str(version)
