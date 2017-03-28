"""
Test `checkers.projects.ruby` file
"""
from checkers.projects import ruby


class TestRubyVersionChecker:
    """Test `ruby.RubyVersionChecker` class"""
    instance = ruby.RubyVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'ruby'
        assert self.instance.homepage == 'http://www.ruby-lang.org/'
        assert self.instance.repository == 'https://github.com/ruby/ruby'

    def test_class_normalize_tag_name_method(self):
        """Test class `_normalize_tag_name()` method"""
        assert self.instance._normalize_tag_name('v2_2_7') == 'v2.2.7'
        assert self.instance._normalize_tag_name('v2.2.7') == 'v2.2.7'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=self.instance._normalize_tag_name,
        )


class TestRailsVersionChecker:
    """Test `ruby.RailsVersionChecker` class"""
    instance = ruby.RailsVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'rails'
        assert self.instance.homepage == 'http://rubyonrails.org/'
        assert self.instance.repository == 'https://github.com/rails/rails'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()


class TestJekyllVersionChecker:
    """Test `ruby.JekyllVersionChecker` class"""
    instance = ruby.JekyllVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'jekyll'
        assert self.instance.homepage == 'https://jekyllrb.com/'
        assert self.instance.repository == 'https://github.com/jekyll/jekyll'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()
