"""
Test `checkers.utils` file
"""
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
    mocked_github = mocker.patch('checkers.utils.GitHub', return_value='github')

    assert utils.get_github_api_client() == 'github'

    mocked_config.assert_called_once_with('GITHUB_TOKEN')
    mocked_github.assert_called_once_with(token='TOKEN')
