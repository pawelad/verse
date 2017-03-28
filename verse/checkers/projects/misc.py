"""
Checkers for misc projects
"""
from checkers.base import BaseVersionChecker
from checkers.utils import remove_prefix


class LinuxKernelVersionChecker(BaseVersionChecker):
    """
    Linux kernel project checker
    """
    name = 'linux-kernel'
    homepage = 'https://www.kernel.org/'
    repository = 'https://github.com/torvalds/linux'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()


class RabbitMQVersionChecker(BaseVersionChecker):
    """
    RabbitMQ project checker
    """
    name = 'rabbitmq'
    homepage = 'https://www.rabbitmq.com/'
    repository = 'https://github.com/rabbitmq/rabbitmq-server'

    @staticmethod
    def _normalize_tag_name(name):
        """
        Normalizes GitHub tag name to be a PEP 404 compliant version name,
        which in this case means removing 'rabbitmq_' prefix and replacing 
        underscores with dots
        Example:
            rabbitmq_v3_6_8 -> v3.6.8

        :param name: tag name
        :type name: str
        :returns: normalized version name
        :rtype: str
        """
        # rabbitmq_v3_6_8 -> v3_6_8
        name = remove_prefix(name, 'rabbitmq_')

        # v3_6_8 -> v3.6.8
        return name.replace('_', '.')

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags(normalize_func=self._normalize_tag_name)


class SupervisorVersionChecker(BaseVersionChecker):
    """
    Supervisor project checker
    """
    name = 'supervisor'
    homepage = 'http://supervisord.org/'
    repository = 'https://github.com/Supervisor/supervisor'

    def get_versions(self):
        """
        Get the versions from GitHub tags
        """
        return self._get_github_tags()
