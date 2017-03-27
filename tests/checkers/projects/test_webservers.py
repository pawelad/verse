"""
Test `checkers.projects.webservers` file
"""
from checkers.projects import webservers


class TestApacheVersionChecker:
    """Test `webservers.ApacheVersionChecker` class"""
    instance = webservers.ApacheVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'apache-httpd'
        assert self.instance.homepage == 'http://httpd.apache.org/'
        assert self.instance.repository == 'https://github.com/apache/httpd'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()


class TestNginxVersionChecker:
    """Test `webservers.NginxVersionChecker` class"""
    instance = webservers.NginxVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'nginx'
        assert self.instance.homepage == 'http://nginx.org/'
        assert self.instance.repository == 'https://github.com/nginx/nginx'

    def test_class_normalize_tag_name_method(self):
        """Test class `_normalize_tag_name()` method"""
        assert self.instance._normalize_tag_name('release-1.11.9') == '1.11.9'
        assert self.instance._normalize_tag_name('1.11.9') == '1.11.9'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=self.instance._normalize_tag_name
        )
