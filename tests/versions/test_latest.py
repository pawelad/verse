"""
Test `versions.latest` file
"""
from unittest.mock import MagicMock

from checkers.projects import BaseVersionChecker
from versions import utils
from versions.latest import (
    get_latest_version, get_latest_major_versions, get_latest_minor_versions,
)


project = MagicMock(spec=BaseVersionChecker)


def test_get_latest_version_function(mocker):
    """Test `latest.get_latest_version()` function"""
    latest_version = '0.1.1'
    mocked_get_or_set = mocker.patch('versions.latest.cache.get_or_set')
    mocked_get_or_set.return_value = latest_version

    assert get_latest_version(project) == latest_version

    mocked_get_or_set.assert_called_once_with(
        key=utils.get_latest_version_key(project.name),
        default=project.get_latest_version,
    )


def test_get_latest_major_versions_function(mocker):
    """Test `latest.get_latest_major_versions()` function"""
    latest_versions = {
        '1': '1.2.3',
        '0': '0.12.0',
    }
    mocked_get_or_set = mocker.patch('versions.latest.cache.get_or_set')
    mocked_get_or_set.return_value = latest_versions

    assert get_latest_major_versions(project) == latest_versions

    mocked_get_or_set.assert_called_once_with(
        key=utils.get_latest_major_versions_key(project.name),
        default=project.get_latest_major_versions,
    )


def test_get_latest_minor_versions_function(mocker):
    """Test `latest.get_latest_minor_versions()` function"""
    latest_versions = {
        '1.2': '1.2.3',
        '1.1': '1.1.4',
        '1.0': '1.0.2',
    }
    mocked_get_or_set = mocker.patch('versions.latest.cache.get_or_set')
    mocked_get_or_set.return_value = latest_versions

    assert get_latest_minor_versions(project) == latest_versions

    mocked_get_or_set.assert_called_once_with(
        key=utils.get_latest_minor_versions_key(project.name),
        default=project.get_latest_minor_versions,
    )
