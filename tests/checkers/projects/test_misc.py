"""
Test `checkers.projects.misc` file
"""
import pytest

from checkers import base
from checkers.projects import misc


class TestLinuxKernelVersionChecker:
    """
    Test `misc.LinuxKernelVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return misc.LinuxKernelVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'Linux kernel'
        assert instance.slug == 'linux-kernel'
        assert instance.homepage == 'https://www.kernel.org/'
        assert instance.repository == 'https://github.com/torvalds/linux'


class TestRabbitMQVersionChecker:
    """
    Test `misc.RabbitMQVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return misc.RabbitMQVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'RabbitMQ'
        assert instance.slug == 'rabbitmq'
        assert instance.homepage == 'https://www.rabbitmq.com/'
        assert (
            instance.repository ==
            'https://github.com/rabbitmq/rabbitmq-server'
        )

    def test_class_normalize_tag_name_method(self, instance):
        """Test class `_normalize_tag_name()` method"""
        assert instance._normalize_tag_name('rabbitmq_v3_6_8') == 'v3.6.8'
        assert instance._normalize_tag_name('v3.6.8') == 'v3.6.8'

    def test_class_get_versions_method(self, mocker, instance):
        """Test class `get_versions()` method"""
        mocked_get_github_tags = mocker.patch.object(
            instance, '_get_github_tags',
        )

        assert instance.get_versions() == mocked_get_github_tags.return_value

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=instance._normalize_tag_name,
        )


class TestSupervisorVersionChecker:
    """
    Test `misc.SupervisorVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return misc.SupervisorVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'Supervisor'
        assert instance.slug == 'supervisor'
        assert instance.homepage == 'http://supervisord.org/'
        assert (
            instance.repository ==
            'https://github.com/Supervisor/supervisor'
        )


class TestVagrantVersionChecker:
    """
    Test `misc.VagrantVersionChecker` class
    """
    @pytest.fixture
    def instance(self):
        return misc.VagrantVersionChecker()

    def test_class_inheritance(self, instance):
        """Test class inheritance"""
        assert isinstance(instance, base.BaseVersionChecker)
        assert isinstance(instance, base.GitHubVersionChecker)

    def test_class_properties(self, instance):
        """Test class properties"""
        assert instance.name == 'Vagrant'
        assert instance.slug == 'vagrant'
        assert instance.homepage == 'https://www.vagrantup.com/'
        assert instance.repository == 'https://github.com/mitchellh/vagrant'
