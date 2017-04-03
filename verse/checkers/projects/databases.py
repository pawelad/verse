"""
Checkers for databases projects
"""
from checkers import base
from checkers.utils import remove_prefix


class MySQLVersionChecker(base.GitHubVersionChecker):
    """
    MySQL project checker
    """
    name = 'MySQL'
    slug = 'mysql'
    homepage = 'https://www.mysql.com/'
    repository = 'https://github.com/mysql/mysql-server'

    @staticmethod
    def _normalize_tag_name(name):
        """
        Normalizes GitHub tag name to be a PEP 404 compliant version name

        :param name: tag name
        :type name: str
        :returns: normalized version name
        :rtype: str
        """
        # Don't ask me why but this repository contains both `mysql`
        # and `mysql-cluster` versions, so we have to split it in
        # two checkers and ignore one type
        if name.startswith('mysql-cluster'):
            return ''

        # Also, there is a '8.0.0' release even though it's a development
        # preview version
        if name == 'mysql-8.0.0':
            return name + 'rc1'

        # mysql-5.6.35 -> 5.6.35
        return remove_prefix(name, 'mysql-')

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags(normalize_func=self._normalize_tag_name)


class MySQLClusterVersionChecker(base.GitHubVersionChecker):
    """
    MySQL Cluster project checker
    """
    name = 'MySQL Cluster'
    slug = 'mysql-cluster'
    homepage = 'https://www.mysql.com/'
    repository = 'https://github.com/mysql/mysql-server'

    @staticmethod
    def _normalize_tag_name(name):
        """
        Normalizes GitHub tag name to be a PEP 404 compliant version name

        :param name: tag name
        :type name: str
        :returns: normalized version name
        :rtype: str
        """
        # Don't ask me why but this repository contains both `mysql`
        # and `mysql-cluster` versions, so we have to split it in
        # two checkers and ignore one type
        if name.startswith('mysql-') and not name.startswith('mysql-cluster'):
            return ''

        # mysql-cluster-7.4.14 -> 7.4.14
        return remove_prefix(name, 'mysql-cluster-')

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags(normalize_func=self._normalize_tag_name)


class PostgreSQLVersionChecker(base.GitHubVersionChecker):
    """
    PostgreSQL project checker
    """
    name = 'PostgreSQL'
    slug = 'postgresql'
    homepage = 'https://www.postgresql.org/'
    repository = 'https://github.com/postgres/postgres'

    @staticmethod
    def _normalize_tag_name(name):
        """
        Normalizes GitHub tag name to be a PEP 404 compliant version name,
        which in this case means removing 'REL' prefix and replacing
        underscores with dots
        Example:
            REL9_2_20 -> 9.2.20

        :param name: tag name
        :type name: str
        :returns: normalized version name
        :rtype: str
        """
        # REL9_2_20 -> 9_2_20
        name = remove_prefix(name, 'REL')

        # 9_2_20 -> 9.2.20
        return name.replace('_', '.')

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags(normalize_func=self._normalize_tag_name)


class SQLiteVersionChecker(base.GitHubVersionChecker):
    """
    SQLite project checker
    """
    name = 'SQLite'
    slug = 'sqlite'
    homepage = 'https://www.sqlite.org/'
    repository = 'https://github.com/mackyle/sqlite'

    @staticmethod
    def _normalize_tag_name(name):
        """
        Normalizes GitHub tag name to be a PEP 404 compliant version name,
        which in this case means removing 'version-' prefix
        Example:
            version-3.16.2 -> 3.16.2

        :param name: tag name
        :type name: str
        :returns: normalized version name
        :rtype: str
        """
        return remove_prefix(name, 'version-')

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags(normalize_func=self._normalize_tag_name)
