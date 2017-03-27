"""
Checkers for git related projects
"""
from checkers.base import BaseVersionChecker


class GitVersionChecker(BaseVersionChecker):
    """
    Git project checker
    """
    name = 'git'
    homepage = 'https://git-scm.com/'
    repository = 'https://github.com/git/git'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()


class GitLabVersionChecker(BaseVersionChecker):
    """
    GitLab project checker
    """
    name = 'gitlab'
    homepage = 'https://gitlab.com'
    repository = 'https://github.com/gitlabhq/gitlabhq'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()


class GogsVersionChecker(BaseVersionChecker):
    """
    Gogs project checker
    """
    name = 'gogs'
    homepage = 'https://gogs.io/'
    repository = 'https://github.com/gogits/gogs'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()
