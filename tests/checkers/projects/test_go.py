"""
Test `checkers.projects.go` file
"""
from checkers.projects import go


def test_go_version_checker(mocker):
    """Test `go.GoVersionChecker` class"""
    instance = go.GoVersionChecker()

    assert instance.name == 'go'
    assert instance.homepage == 'https://golang.org/'
    assert instance.repository == 'https://github.com/golang/go'

    mocked_get_github_tags = mocker.patch.object(instance, '_get_github_tags')
    instance.get_latest_version()

    mocked_get_github_tags.assert_called_once_with(
        normalize_func=instance._normalize_tag_name
    )

    # Normalize tag name
    assert go.GoVersionChecker._normalize_tag_name('go1.8') == '1.8'
