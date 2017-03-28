"""
Test `checkers.projects.ruby` file
"""
import pytest

from checkers.projects import ruby


class TestRubyVersionChecker:
    """
    Test `ruby.RubyVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return ruby.RubyVersionChecker()

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'ruby'
        assert instance.homepage == 'http://www.ruby-lang.org/'
        assert instance.repository == 'https://github.com/ruby/ruby'

    def test_class_normalize_tag_name_method(self, instance):
        """Test class `_normalize_tag_name()` method"""
        assert instance._normalize_tag_name('v2_2_7') == 'v2.2.7'
        assert instance._normalize_tag_name('v2.2.7') == 'v2.2.7'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=instance._normalize_tag_name,
        )


class TestRailsVersionChecker:
    """
    Test `ruby.RailsVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return ruby.RailsVersionChecker()

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'rails'
        assert instance.homepage == 'http://rubyonrails.org/'
        assert instance.repository == 'https://github.com/rails/rails'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with()


class TestJekyllVersionChecker:
    """
    Test `ruby.JekyllVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return ruby.JekyllVersionChecker()

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'jekyll'
        assert instance.homepage == 'https://jekyllrb.com/'
        assert instance.repository == 'https://github.com/jekyll/jekyll'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with()
