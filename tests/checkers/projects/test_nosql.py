"""
Test `checkers.projects.nosql` file
"""
from packaging.version import Version

from checkers.projects import nosql


class TestCassandraVersionChecker:
    """Test `nosql.CassandraVersionChecker` class"""
    instance = nosql.CassandraVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'cassandra'
        assert self.instance.homepage == 'http://cassandra.apache.org/'
        assert self.instance.repository == 'https://github.com/apache/cassandra'

    def test_class_normalize_tag_name_method(self):
        """Test class `_normalize_tag_name()` method"""
        assert (
            self.instance._normalize_tag_name('cassandra-3.0.12') ==
            '3.0.12'
        )
        assert self.instance._normalize_tag_name('3.0.12') == '3.0.12'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=self.instance._normalize_tag_name,
        )


class TestMongoDBVersionChecker:
    """Test `nosql.MongoDBVersionChecker` class"""
    instance = nosql.MongoDBVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'mongodb'
        assert self.instance.homepage == 'https://www.mongodb.com/'
        assert self.instance.repository == 'https://github.com/mongodb/mongo'

    def test_class_normalize_tag_name_method(self):
        """Test class `_normalize_tag_name()` method"""
        assert self.instance._normalize_tag_name('r3.4.3') == '3.4.3'
        assert self.instance._normalize_tag_name('3.4.3') == '3.4.3'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=self.instance._normalize_tag_name,
        )


class TestRedisVersionChecker:
    """Test `nosql.RedisVersionChecker` class"""
    instance = nosql.RedisVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'redis'
        assert self.instance.homepage == 'https://redis.io/'
        assert self.instance.repository == 'https://github.com/antirez/redis'

    def test_class_normalize_tag_name_method(self):
        """Test class `_normalize_tag_name()` method"""
        assert self.instance._normalize_tag_name('1.3.6') == ''
        assert self.instance._normalize_tag_name('3.2.8') == '3.2.8'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=self.instance._normalize_tag_name,
        )

    def test_class_get_latest_version(self, mocker):
        """Test class `get_latest_version()` method"""
        versions = [
            'v1.3.2', 'v1.3.1', 'v1.3.0', '3.2.8',
        ]
        mocker.patch.object(
            self.instance, 'get_versions',
            return_value=[Version(v) for v in versions],
        )

        assert self.instance.get_latest_version() == '3.2.8'
