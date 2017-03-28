"""
Test `checkers.base` file
"""
import inspect
import random
from unittest.mock import MagicMock

import pytest
from github3.repos import Repository
from github3.repos.tag import RepoTag
from packaging.version import Version

from checkers.base import BaseVersionChecker


class TestBaseVersionChecker:
    """
    Test `BaseVersionChecker` class
    """
    klass = BaseVersionChecker
    versions = [
        '17.03.2-rc1', '17.03.1', '17.03.0', '1.3.1', '1.3.0', '1.2.2',
        '1.2.1', '1.2.0', '1.0', '0.6.1', '0.6.0', '0.5', '0.1.1', '0.1',
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

        # Test tag name normalization
        mocked_repo = MagicMock(autospec=Repository)

        mocked_tags = list()
        versions = [
            '17.03.2-rc1', '17.03.1', '2.1-foobar', '2.0.1', '2', 'v1.2',
            'v1.1', 'v1', 'v0.2.1', 'v0.2', '0.1.0', 'not a version',
        ]
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
        expected_versions = [
            '17.3.2rc1', '17.3.1', '2.0.1', '2.0', 'v1.2',
            'v1.1', 'v1.0', 'v0.2.1', 'v0.2', '0.1.0',
        ]
        assert result == [Version(v) for v in expected_versions]

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

        assert instance.get_latest_version() == '17.3.1'

    def test_class_get_latest_major_versions_method(self, mocker, instance):
        """Test `BaseVersionChecker.get_latest_major_versions()` method"""
        mocker.patch.object(
            instance, 'get_versions',
            return_value=[Version(v) for v in self.versions],
        )

        assert instance.get_latest_major_versions() == {
            '17': '17.3.1',
            '1': '1.3.1',
            '0': '0.6.1',
        }

        # Unsorted result from `get_version()`
        unsorted_versions = self.versions.copy()
        random.shuffle(unsorted_versions)
        mocker.patch.object(
            instance, 'get_versions',
            return_value=[Version(v) for v in unsorted_versions],
        )

        with pytest.raises(ValueError):
            instance.get_latest_major_versions()

    def test_class_get_latest_minor_versions_method(self, mocker, instance):
        """Test `BaseVersionChecker.get_latest_minor_versions()` method"""
        mocker.patch.object(
            instance, 'get_versions',
            return_value=[Version(v) for v in self.versions],
        )

        assert instance.get_latest_minor_versions() == {
            '17.3': '17.3.1',
            '1.3': '1.3.1',
            '1.2': '1.2.2',
            '1.0': '1.0',
            '0.6': '0.6.1',
            '0.5': '0.5',
            '0.1': '0.1.1',
        }

        # Unsorted result from `get_version()`
        unsorted_versions = self.versions.copy()
        random.shuffle(unsorted_versions)
        mocker.patch.object(
            instance, 'get_versions',
            return_value=[Version(v) for v in unsorted_versions],
        )

        with pytest.raises(ValueError):
            instance.get_latest_minor_versions()
