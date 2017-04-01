"""
Test `checkers.projects.nosql` file
"""
import operator

import pytest
from packaging.version import Version

from checkers import base
from checkers.projects import nosql


class TestCassandraVersionChecker:
    """
    Test `nosql.CassandraVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return nosql.CassandraVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'cassandra'
        assert instance.homepage == 'http://cassandra.apache.org/'
        assert instance.repository == 'https://github.com/apache/cassandra'

    def test_class_normalize_tag_name_method(self, instance):
        """Test class `_normalize_tag_name()` method"""
        assert (
            instance._normalize_tag_name('cassandra-3.0.12') ==
            '3.0.12'
        )
        assert instance._normalize_tag_name('3.0.12') == '3.0.12'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=instance._normalize_tag_name,
        )


class TestElasticsearchVersionChecker:
    """
    Test `nosql.ElasticsearchVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return nosql.ElasticsearchVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'elasticsearch'
        assert (
            instance.homepage ==
            'https://www.elastic.co/products/elasticsearch'
        )
        assert (
            instance.repository ==
            'https://github.com/elastic/elasticsearch'
        )


class TestMongoDBVersionChecker:
    """
    Test `nosql.MongoDBVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return nosql.MongoDBVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'mongodb'
        assert instance.homepage == 'https://www.mongodb.com/'
        assert instance.repository == 'https://github.com/mongodb/mongo'

    def test_class_normalize_tag_name_method(self, instance):
        """Test class `_normalize_tag_name()` method"""
        assert instance._normalize_tag_name('r3.4.3') == '3.4.3'
        assert instance._normalize_tag_name('3.4.3') == '3.4.3'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        versions = [
            Version(v) for v in
            ['v1.3.2', 'v1.3.1', 'v1.3.0', '3.2.8']
        ]
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags', return_value=versions,
        )

        sorted_versions = sorted(
            versions,
            key=operator.attrgetter('base_version'),
            reverse=True,
        )

        assert instance.get_versions() == sorted_versions

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=instance._normalize_tag_name,
        )


class TestRedisVersionChecker:
    """
    Test `nosql.RedisVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return nosql.RedisVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'redis'
        assert instance.homepage == 'https://redis.io/'
        assert instance.repository == 'https://github.com/antirez/redis'

    def test_class_normalize_tag_name_method(self, instance):
        """Test class `_normalize_tag_name()` method"""
        assert instance._normalize_tag_name('1.3.6') == ''
        assert instance._normalize_tag_name('3.2.8') == '3.2.8'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=instance._normalize_tag_name,
        )

    def test_class_get_latest_version(self, mocker, instance):
        """Test class `get_latest_version()` method"""
        versions = [
            'v1.3.2', 'v1.3.1', 'v1.3.0', '3.2.8',
        ]
        mocker.patch.object(
            instance, 'get_versions',
            return_value=[Version(v) for v in versions],
        )

        assert instance.get_latest_version() == '3.2.8'
