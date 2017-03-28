"""
Checkers for databases projects
"""
from checkers.base import BaseVersionChecker
from checkers.utils import remove_prefix


class PostgreSQLVersionChecker(BaseVersionChecker):
    """
    PostgreSQL project checker
    """
    name = 'postgresql'
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
