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
