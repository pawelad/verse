"""
Test `checkers.projects.misc` file
"""
from checkers.projects import misc


class TestLinuxKernelVersionChecker:
    """Test `misc.LinuxKernelVersionChecker` class"""
    instance = misc.LinuxKernelVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'linux-kernel'
        assert self.instance.homepage == 'https://www.kernel.org/'
        assert self.instance.repository == 'https://github.com/torvalds/linux'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()


class TestRabbitMQVersionChecker:
    """Test `misc.RabbitMQVersionChecker` class"""
    instance = misc.RabbitMQVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'rabbitmq'
        assert self.instance.homepage == 'https://www.rabbitmq.com/'
        assert (
            self.instance.repository ==
            'https://github.com/rabbitmq/rabbitmq-server'
        )

    def test_class_normalize_tag_name_method(self):
        """Test class `_normalize_tag_name()` method"""
        assert self.instance._normalize_tag_name('rabbitmq_v3_6_8') == 'v3.6.8'
        assert self.instance._normalize_tag_name('v3.6.8') == 'v3.6.8'

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with(
            normalize_func=self.instance._normalize_tag_name,
        )


class TestSupervisorVersionChecker:
    """Test `misc.SupervisorVersionChecker` class"""
    instance = misc.SupervisorVersionChecker()

    def test_class_properties(self):
        """Test class properties"""
        assert self.instance.name == 'supervisor'
        assert self.instance.homepage == 'http://supervisord.org/'
        assert (
            self.instance.repository ==
            'https://github.com/Supervisor/supervisor'
        )

    def test_class_get_latest_version_method(self, mocker):
        """Test class `get_latest_version()` method"""
        mocked_get_github_tags = mocker.patch.object(
            self.instance, '_get_github_tags',
        )
        self.instance.get_latest_version()

        mocked_get_github_tags.assert_called_once_with()
