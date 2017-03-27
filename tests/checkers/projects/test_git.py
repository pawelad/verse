"""
Test `checkers.projects.git` file
"""
from checkers.projects import git


class TestGitVersionChecker:
    """Test `git.GitVersionChecker` class"""
    instance = git.GitVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'git'
        assert self.instance.homepage == 'https://git-scm.com/'
        assert self.instance.repository == 'https://github.com/git/git'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()
