"""
Checkers for git related projects
"""
from checkers import base


class GitVersionChecker(base.GitHubVersionChecker):
    """
    Git project checker
    """
    name = 'git'
    homepage = 'https://git-scm.com/'
    repository = 'https://github.com/git/git'


class GitLabVersionChecker(base.GitHubVersionChecker):
    """
    GitLab project checker
    """
    name = 'gitlab'
    homepage = 'https://gitlab.com'
    repository = 'https://github.com/gitlabhq/gitlabhq'


class GogsVersionChecker(base.GitHubVersionChecker):
    """
    Gogs project checker
    """
    name = 'gogs'
    homepage = 'https://gogs.io/'
    repository = 'https://github.com/gogits/gogs'
