"""
Checkers for Ruby related projects
"""
from checkers.base import BaseVersionChecker
from checkers.utils import remove_prefix


class RubyVersionChecker(BaseVersionChecker):
    """
    Ruby project checker
    """
    name = 'ruby'
    homepage = 'http://www.ruby-lang.org/'
    repository = 'https://github.com/ruby/ruby'

    @staticmethod
    def _normalize_tag_name(name):
        """
        Normalizes GitHub tag name to be a PEP 404 compliant version name,
        which in this case means replacing underscores with dots
        Example:
            v2_2_7 -> v2.2.7

        :param name: tag name
        :type name: str
        :returns: normalized version name
        :rtype: str
        """
        return name.replace('_', '.')

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags(normalize_func=self._normalize_tag_name)
