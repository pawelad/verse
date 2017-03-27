"""
Checkers for webserver projects
"""
from checkers.base import BaseVersionChecker
from checkers.utils import remove_prefix


class ApacheVersionChecker(BaseVersionChecker):
    """
    Apache httpd project checker
    """
    name = 'apache-httpd'
    homepage = 'http://httpd.apache.org/'
    repository = 'https://github.com/apache/httpd'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()


class NginxVersionChecker(BaseVersionChecker):
    """
    Nginx project checker
    """
    name = 'nginx'
    homepage = 'http://nginx.org/'
    repository = 'https://github.com/nginx/nginx'

    @staticmethod
    def _normalize_tag_name(name):
        """
        Normalizes GitHub tag name to be a PEP 404 compliant version name,
        which in this case means removing 'release-' prefix
        Example:
           release-1.11.12  -> 1.11.12

        :param name: tag name
        :type name: str
        :returns: normalized version name
        :rtype: str
        """
        return remove_prefix(name, 'release-')

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags(normalize_func=self._normalize_tag_name)
