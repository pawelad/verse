"""
Test `checkers.projects.git` file
"""
import pytest

from checkers.projects import git


class TestGitVersionChecker:
    """
    Test `git.GitVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return git.GitVersionChecker()

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'git'
        assert instance.homepage == 'https://git-scm.com/'
        assert instance.repository == 'https://github.com/git/git'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with()


class TestGitLabVersionChecker:
    """
    Test `git.GitLabVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return git.GitLabVersionChecker()

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'gitlab'
        assert instance.homepage == 'https://gitlab.com'
        assert instance.repository == 'https://github.com/gitlabhq/gitlabhq'

    def test_class_get_latest_version_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with()


class TestGogsVersionChecker:
    """
    Test `git.GogsVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return git.GogsVersionChecker()

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'gogs'
        assert instance.homepage == 'https://gogs.io/'
        assert instance.repository == 'https://github.com/gogits/gogs'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with()
