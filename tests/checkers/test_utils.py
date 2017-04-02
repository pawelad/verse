"""
Test `checkers.utils` file
"""
from unittest.mock import Mock

import pytest

from checkers import utils


def test_remove_prefix_function():
    """Test `utils.remove_prefix()` function"""
    text = 'prefix-actual-text'

    assert utils.remove_prefix(text, 'prefix-') == 'actual-text'
    assert utils.remove_prefix(text, 'prefix-', silent=False) == 'actual-text'

    assert utils.remove_prefix(text, 'non-prefix') == text

    with pytest.raises(ValueError):
        utils.remove_prefix(text, 'non-prefix', silent=False)


def test_get_github_api_client_function(mocker):
    """Test `utils.get_github_api_client()` function"""
    mocked_config = mocker.patch('checkers.utils.config', return_value='TOKEN')
    mocked_github = mocker.patch('checkers.utils.GitHub')

    assert isinstance(utils.get_github_api_client(), Mock)

    mocked_config.assert_called_once_with('GITHUB_TOKEN', default=None)
    mocked_github.assert_called_once_with(token='TOKEN')


def test_deconstruct_github_url():
    """Test `utils.deconstruct_github_url()` function"""
    assert (
        utils.deconstruct_github_url('https://github.com/test/foo-bar') ==
        ('test', 'foo-bar')
    )
    assert (
        utils.deconstruct_github_url('https://github.com/pawelad/verse') ==
        ('pawelad', 'verse')
    )

    # Wrong URL
    with pytest.raises(ValueError):
        utils.deconstruct_github_url('not-a-github-url')


def test_construct_github_url():
    """Test `utils.construct_github_url()` function"""
    assert (
        utils.construct_github_url('test', 'foo-bar') ==
        'https://github.com/test/foo-bar'
    )
    assert (
        utils.construct_github_url('pawelad', 'verse') ==
        'https://github.com/pawelad/verse'
    )
