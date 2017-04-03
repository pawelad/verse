"""
Test `checkers.projects.databases` file
"""
import pytest

from checkers import base
from checkers.projects import databases


class TestMySQLVersionChecker:
    """
    Test `databases.MySQLVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return databases.MySQLVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'MySQL'
        assert instance.slug == 'mysql'
        assert instance.homepage == 'https://www.mysql.com/'
        assert instance.repository == 'https://github.com/mysql/mysql-server'

    def test_class_normalize_tag_name_method(self, instance):
        """Test class `_normalize_tag_name()` method"""
        assert instance._normalize_tag_name('mysql-cluster-7.4.14') == ''
        assert instance._normalize_tag_name('mysql-8.0.0') == 'mysql-8.0.0rc1'
        assert instance._normalize_tag_name('mysql-5.6.35') == '5.6.35'
        assert instance._normalize_tag_name('5.6.35') == '5.6.35'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=instance._normalize_tag_name,
        )


class TestMySQLClusterVersionChecker:
    """
    Test `databases.MySQLClusterVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return databases.MySQLClusterVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'MySQL Cluster'
        assert instance.slug == 'mysql-cluster'
        assert instance.homepage == 'https://www.mysql.com/'
        assert instance.repository == 'https://github.com/mysql/mysql-server'

    def test_class_normalize_tag_name_method(self, instance):
        """Test class `_normalize_tag_name()` method"""
        assert instance._normalize_tag_name('mysql-5.6.35') == ''
        assert instance._normalize_tag_name('mysql-cluster-7.4.14') == '7.4.14'
        assert instance._normalize_tag_name('7.4.14') == '7.4.14'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=instance._normalize_tag_name,
        )


class TestPostgreSQLVersionChecker:
    """
    Test `databases.PostgreSQLVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return databases.PostgreSQLVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'PostgreSQL'
        assert instance.slug == 'postgresql'
        assert instance.homepage == 'https://www.postgresql.org/'
        assert instance.repository == 'https://github.com/postgres/postgres'

    def test_class_normalize_tag_name_method(self, instance):
        """Test class `_normalize_tag_name()` method"""
        assert instance._normalize_tag_name('REL9_2_20') == '9.2.20'
        assert instance._normalize_tag_name('9_2_20') == '9.2.20'
        assert instance._normalize_tag_name('9.2.20') == '9.2.20'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=instance._normalize_tag_name,
        )


class TestSQLiteVersionChecker:
    """
    Test `databases.SQLiteVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return databases.SQLiteVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'SQLite'
        assert instance.slug == 'sqlite'
        assert instance.homepage == 'https://www.sqlite.org/'
        assert instance.repository == 'https://github.com/mackyle/sqlite'

    def test_class_normalize_tag_name_method(self, instance):
        """Test class `_normalize_tag_name()` method"""
        assert instance._normalize_tag_name('version-3.17.0') == '3.17.0'
        assert instance._normalize_tag_name('3.17.0') == '3.17.0'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=instance._normalize_tag_name,
        )
