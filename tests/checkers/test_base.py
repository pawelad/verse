"""
Test `checkers.base` file
"""
import inspect
from unittest.mock import MagicMock

import pytest
from github3.repos import Repository
from github3.repos.tag import RepoTag
from packaging.version import Version

from checkers.base import BaseVersionChecker


class TestBaseVersionChecker:
    """Test `BaseVersionChecker` class"""
    klass = BaseVersionChecker
    versions = [
        'v2.1.2rc1', 'v2.1.1', 'v2.1', 'v2.0', 'v0.7.3', 'v0.7.2', 'v0.7.1',
        '0.7', '0.6.1', '0.6', '0.4', '0.3.1', '0.3', '0.2', '0.1',
    ]

    @pytest.fixture
    def instance(self, mocker):
        """Helper fixture for creating instance of an abstract class"""
        mocker.patch.multiple(self.klass, __abstractmethods__=set())
        instance = self.klass()
        return instance

    def test_class_abstraction(self):
        """Test if the class is an abstract class"""
        assert inspect.isabstract(self.klass)

    def test_class_get_github_tags_method(self, mocker, instance):
        """Test `BaseVersionChecker._get_github_tags()` method"""
        # Non GitHub URL
        with pytest.raises(ValueError):
            list(instance._get_github_tags('http://example.com'))

        mocked_repo = MagicMock(autospec=Repository)
        mocked_tags = list()
        versions = ['foobar'] + self.versions
        for version in versions:
            mocked_tag = MagicMock(autospec=RepoTag)
            mocked_tag.name = version
            mocked_tags.append(mocked_tag)

        mocked_github_client = mocker.patch('checkers.base.github_client')
        mocked_repo.iter_tags.return_value = mocked_tags
        mocked_github_client.repository.return_value = mocked_repo

        result = instance._get_github_tags('https://github.com/pawelad/verse')
        assert inspect.isgenerator(result)

        result = list(result)
        assert result == [Version(v) for v in self.versions]

        mocked_github_client.repository.assert_called_once_with(
            'pawelad', 'verse',
        )
        mocked_repo.iter_tags.assert_called_once_with()

    def test_class_get_versions_method(self, instance):
        """Test `BaseVersionChecker.get_versions()` method"""
        with pytest.raises(NotImplementedError):
            instance.get_versions()

    def test_class_get_latest_version_method(self, mocker, instance):
        """Test `BaseVersionChecker.get_latest_version()` method"""
        mocker.patch.object(
            instance, 'get_versions',
            return_value=[Version(v) for v in self.versions],
        )

        assert instance.get_latest_version() == '2.1.1'

    def test_class_get_latest_major_versions_method(self, mocker, instance):
        """Test `BaseVersionChecker.get_latest_major_versions()` method"""
        mocker.patch.object(
            instance, 'get_versions',
            return_value=[Version(v) for v in self.versions],
        )

        assert instance.get_latest_major_versions() == {
            '2': '2.1.1',
            '0': '0.7.3',
        }

    def test_class_get_latest_minor_versions_method(self, mocker, instance):
        """Test `BaseVersionChecker.get_latest_minor_versions()` method"""
        mocker.patch.object(
            instance, 'get_versions',
            return_value=[Version(v) for v in self.versions],
        )

        assert instance.get_latest_minor_versions() == {
            '2.1': '2.1.1',
            '2.0': '2.0',
            '0.7': '0.7.3',
            '0.6': '0.6.1',
            '0.4': '0.4',
            '0.3': '0.3.1',
            '0.2': '0.2',
            '0.1': '0.1',
        }
