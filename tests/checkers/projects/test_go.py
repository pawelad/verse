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
    assert instance._normalize_tag_name('go1.8') == '1.8'


def test_docker_version_checker(mocker):
    """Test `go.DockerVersionChecker` class"""
    instance = go.DockerVersionChecker()

    assert instance.name == 'docker'
    assert instance.homepage == 'https://www.docker.com/'
    assert instance.repository == 'https://github.com/docker/docker'

    mocked_get_github_tags = mocker.patch.object(instance, '_get_github_tags')
    instance.get_latest_version()

    mocked_get_github_tags.assert_called_once_with(
        normalize_func=instance._normalize_tag_name
    )

    # Normalize tag name
    assert instance._normalize_tag_name('v17.03.0-ce') == 'v17.03.0'
    assert instance._normalize_tag_name('v17.03.0') == 'v17.03.0'
