"""
Checkers for NoSQL projects
"""
import operator

from checkers import base
from checkers.utils import remove_prefix


class CassandraVersionChecker(base.GitHubVersionChecker):
    """
    Cassandra project checker
    """
    name = 'cassandra'
    homepage = 'http://cassandra.apache.org/'
    repository = 'https://github.com/apache/cassandra'

    @staticmethod
    def _normalize_tag_name(name):
        """
        Normalizes GitHub tag name to be a PEP 404 compliant version name,
        which in this case means removing 'cassandra-' prefix
        Example:
           cassandra-3.0.12 -> 3.0.12

        :param name: tag name
        :type name: str
        :returns: normalized version name
        :rtype: str
        """
        return remove_prefix(name, 'cassandra-')

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags(normalize_func=self._normalize_tag_name)


class ElasticsearchVersionChecker(base.GitHubVersionChecker):
    """
    Elasticsearch project checker
    """
    name = 'elasticsearch'
    homepage = 'https://www.elastic.co/products/elasticsearch'
    repository = 'https://github.com/elastic/elasticsearch'


class MongoDBVersionChecker(base.GitHubVersionChecker):
    """
    MongoDB project checker
    """
    name = 'mongodb'
    homepage = 'https://www.mongodb.com/'
    repository = 'https://github.com/mongodb/mongo'

    @staticmethod
    def _normalize_tag_name(name):
        """
        Normalizes GitHub tag name to be a PEP 404 compliant version name,
        which in this case means removing 'r' prefix
        Example:
           r3.4.3 -> 3.4.3

        :param name: tag name
        :type name: str
        :returns: normalized version name
        :rtype: str
        """
        return remove_prefix(name, 'r')

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        # They randomly use and don't use 'r' prefix so we have to sort
        # versions manually
        versions = list(self._get_github_tags(
            normalize_func=self._normalize_tag_name,
        ))
        versions.sort(
            key=operator.attrgetter('base_version'),
            reverse=True,
        )
        return versions


class RedisVersionChecker(base.GitHubVersionChecker):
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
