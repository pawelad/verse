"""
Test `checkers.projects.go` file
"""
from checkers.projects import go


class TestGoVersionChecker:
    """Test `go.GoVersionChecker` class"""
    instance = go.GoVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'go'
        assert self.instance.homepage == 'https://golang.org/'
        assert self.instance.repository == 'https://github.com/golang/go'

    def test_class_normalize_tag_name_method(self):
        """Test class `_normalize_tag_name()` method"""
        assert self.instance._normalize_tag_name('go1.8') == '1.8'
        assert self.instance._normalize_tag_name('1.8') == '1.8'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=self.instance._normalize_tag_name
        )


class TestDockerVersionChecker:
    """Test `go.DockerVersionChecker` class"""
    instance = go.DockerVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'docker'
        assert self.instance.homepage == 'https://www.docker.com/'
        assert self.instance.repository == 'https://github.com/docker/docker'

    def test_class_normalize_tag_name_method(self):
        """Test class `_normalize_tag_name()` method"""
        assert self.instance._normalize_tag_name('v17.03.0-ce') == 'v17.03.0'
        assert self.instance._normalize_tag_name('v17.03.0') == 'v17.03.0'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=self.instance._normalize_tag_name
        )


class TestKubernetesVersionChecker:
    """Test `go.KubernetesVersionChecker` class"""
    instance = go.KubernetesVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'kubernetes'
        assert self.instance.homepage == 'https://kubernetes.io/'
        assert (
            self.instance.repository ==
            'https://github.com/kubernetes/kubernetes'
        )

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with( )
