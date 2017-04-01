"""
Checkers for frontend framework projects
"""
from checkers import base


class BootstrapVersionChecker(base.GitHubVersionChecker):
    """
    Bootstrap project checker
    """
    name = 'bootstrap'
    homepage = 'http://getbootstrap.com/'
    repository = 'https://github.com/twbs/bootstrap'


class FontAwesomeVersionChecker(base.GitHubVersionChecker):
    """
    Font Awesome project checker
    """
    name = 'font-awesome'
    homepage = 'http://fontawesome.io/'
    repository = 'https://github.com/FortAwesome/Font-Awesome'

    @staticmethod
    def _normalize_tag_name(name):
        """
        Normalizes GitHub tag name to be a PEP 404 compliant version name

        :param name: tag name
        :type name: str
        :returns: normalized version name
        :rtype: str
        """
        # Our first hack : -)
        # Font Awesome has two tags without 'v' in front of them - '4.1.0' and
        # '2.0.0' - which GitHub sorts and sends at the end. '2.0.0' isn't a
        # problem as no '2.0.x' version was present before, but '4.1.x' is
        # declared in two very different places

        # 'v4.1.0' is present, so let's just get rid of '4.1.0'
        if name == '4.1.0':
            return ''

        return name

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags(normalize_func=self._normalize_tag_name)


class MDLVersionChecker(base.GitHubVersionChecker):
    """
    Material Design Lite project checker
    """
    name = 'mdl'
    homepage = 'https://getmdl.io/'
    repository = 'https://github.com/google/material-design-lite'
