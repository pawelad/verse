"""
Test `checkers.projects.databases` file
"""
from checkers.projects import databases


class TestPostgreSQLVersionChecker:
    """Test `databases.PostgreSQLVersionChecker` class"""
    instance = databases.PostgreSQLVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'postgresql'
        assert self.instance.homepage == 'https://www.postgresql.org/'
        assert (
            self.instance.repository ==
            'https://github.com/postgres/postgres'
        )

    def test_class_normalize_tag_name_method(self):
        """Test class `_normalize_tag_name()` method"""
        assert self.instance._normalize_tag_name('REL9_2_20') == '9.2.20'
        assert self.instance._normalize_tag_name('9_2_20') == '9.2.20'
        assert self.instance._normalize_tag_name('9.2.20') == '9.2.20'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=self.instance._normalize_tag_name
        )
