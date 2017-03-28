"""
Checkers for misc projects
"""
from checkers.base import BaseVersionChecker


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
