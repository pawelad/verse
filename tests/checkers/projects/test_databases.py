"""
Test `checkers.projects.databases` file
"""
from checkers.projects import databases


class TestMySQLVersionChecker:
    """Test `databases.MySQLVersionChecker` class"""
    instance = databases.MySQLVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'mysql'
        assert self.instance.homepage == 'https://www.mysql.com/'
        assert (
            self.instance.repository ==
            'https://github.com/mysql/mysql-server'
        )

    def test_class_normalize_tag_name_method(self):
        """Test class `_normalize_tag_name()` method"""
        assert self.instance._normalize_tag_name('mysql-cluster-7.4.14') == ''
        assert (
            self.instance._normalize_tag_name('mysql-8.0.0') ==
            'mysql-8.0.0rc1'
        )
        assert self.instance._normalize_tag_name('mysql-5.6.35') == '5.6.35'
        assert self.instance._normalize_tag_name('5.6.35') == '5.6.35'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=self.instance._normalize_tag_name,
        )


class TestMySQLClusterVersionChecker:
    """Test `databases.MySQLClusterVersionChecker` class"""
    instance = databases.MySQLClusterVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'mysql-cluster'
        assert self.instance.homepage == 'https://www.mysql.com/'
        assert (
            self.instance.repository ==
            'https://github.com/mysql/mysql-server'
        )

    def test_class_normalize_tag_name_method(self):
        """Test class `_normalize_tag_name()` method"""
        assert self.instance._normalize_tag_name('mysql-5.6.35') == ''
        assert (
            self.instance._normalize_tag_name('mysql-cluster-7.4.14') ==
            '7.4.14'
        )
        assert self.instance._normalize_tag_name('7.4.14') == '7.4.14'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=self.instance._normalize_tag_name,
        )


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
            normalize_func=self.instance._normalize_tag_name,
        )


class TestSQLiteVersionChecker:
    """Test `databases.SQLiteVersionChecker` class"""
    instance = databases.SQLiteVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'sqlite'
        assert self.instance.homepage == 'https://www.sqlite.org/'
        assert self.instance.repository == 'https://github.com/mackyle/sqlite'

    def test_class_normalize_tag_name_method(self):
        """Test class `_normalize_tag_name()` method"""
        assert self.instance._normalize_tag_name('version-3.17.0') == '3.17.0'
        assert self.instance._normalize_tag_name('3.17.0') == '3.17.0'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=self.instance._normalize_tag_name,
        )
