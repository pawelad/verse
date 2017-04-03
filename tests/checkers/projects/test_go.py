"""
Test `checkers.projects.go` file
"""
import pytest

from checkers import base
from checkers.projects import go


class TestGoVersionChecker:
    """
    Test `go.GoVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return go.GoVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'Go'
        assert instance.slug == 'go'
        assert instance.homepage == 'https://golang.org/'
        assert instance.repository == 'https://github.com/golang/go'

    def test_class_normalize_tag_name_method(self, instance):
        """Test class `_normalize_tag_name()` method"""
        assert instance._normalize_tag_name('go1.8') == '1.8'
        assert instance._normalize_tag_name('1.8') == '1.8'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=instance._normalize_tag_name,
        )


class TestDockerVersionChecker:
    """
    Test `go.DockerVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return go.DockerVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'Docker'
        assert instance.slug == 'docker'
        assert instance.homepage == 'https://www.docker.com/'
        assert instance.repository == 'https://github.com/docker/docker'

    def test_class_normalize_tag_name_method(self, instance):
        """Test class `_normalize_tag_name()` method"""
        assert instance._normalize_tag_name('v17.03.0-ce') == 'v17.03.0'
        assert instance._normalize_tag_name('v17.03.0') == 'v17.03.0'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=instance._normalize_tag_name,
        )


class TestKubernetesVersionChecker:
    """
    Test `go.KubernetesVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return go.KubernetesVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'Kubernetes'
        assert instance.slug == 'kubernetes'
        assert instance.homepage == 'https://kubernetes.io/'
        assert (
            instance.repository ==
            'https://github.com/kubernetes/kubernetes'
        )
