"""
Test `checkers.projects.git` file
"""
import pytest

from checkers import base
from checkers.projects import git


class TestGitVersionChecker:
    """
    Test `git.GitVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return git.GitVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'Git'
        assert instance.slug == 'git'
        assert instance.homepage == 'https://git-scm.com/'
        assert instance.repository == 'https://github.com/git/git'


class TestGitLabVersionChecker:
    """
    Test `git.GitLabVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return git.GitLabVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'GitLab'
        assert instance.slug == 'gitlab'
        assert instance.homepage == 'https://gitlab.com'
        assert instance.repository == 'https://github.com/gitlabhq/gitlabhq'


class TestGogsVersionChecker:
    """
    Test `git.GogsVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return git.GogsVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'Gogs'
        assert instance.slug == 'gogs'
        assert instance.homepage == 'https://gogs.io/'
        assert instance.repository == 'https://github.com/gogits/gogs'
