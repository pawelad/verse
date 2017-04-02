"""
Test `projects.tasks` file
"""
from unittest.mock import MagicMock

from celery.schedules import crontab

from checkers.base import BaseVersionChecker
from projects import tasks


available_projects = {
    'python': MagicMock(spec=BaseVersionChecker),
    'django': MagicMock(spec=BaseVersionChecker),
}


def test_setup_periodic_tasks(mocker):
    """
    Test `tasks.setup_periodic_tasks`
    """
    mocked_add_periodic_task = MagicMock()
    sender = MagicMock()
    sender.add_periodic_task.return_value = mocked_add_periodic_task

    mocked_cache_all_projects_latest_version = mocker.patch(
        'projects.tasks.cache_all_projects_latest_version'
    )
    mocked_cache_all_projects_latest_major_versions = mocker.patch(
        'projects.tasks.cache_all_projects_latest_major_versions'
    )
    mocked_cache_all_projects_latest_minor_versions = mocker.patch(
        'projects.tasks.cache_all_projects_latest_minor_versions'
    )

    tasks.setup_periodic_tasks(sender)

    assert sender.add_periodic_task.call_count == 3

    sender.add_periodic_task.assert_any_call(
        crontab(minute=0),
        mocked_cache_all_projects_latest_version.s(),
    )

    sender.add_periodic_task.assert_any_call(
        crontab(minute=0, hour='*/6'),
        mocked_cache_all_projects_latest_major_versions.s(),
    )

    sender.add_periodic_task.assert_any_call(
        crontab(minute=0, hour='*/6'),
        mocked_cache_all_projects_latest_minor_versions.s(),
    )


def test_cache_latest_major_versions(mocker):
    """
    Test `tasks.cache_latest_major_versions`
    """
    mocker.patch('projects.tasks.AVAILABLE_CHECKERS', available_projects)
    project = available_projects['python']

    mocked_cache_set = mocker.patch('projects.tasks.cache.set')
    mocked_key = mocker.patch(
        'projects.tasks.utils.get_latest_major_versions_key',
    )

    tasks.cache_latest_major_versions('python')

    mocked_cache_set.assert_called_once_with(
        key=mocked_key.return_value,
        value=project.get_latest_major_versions(),
    )


def test_cache_all_projects_latest_major_versions(mocker):
    """
    Test `tasks.cache_all_projects_latest_major_versions`
    """
    mocker.patch('projects.tasks.AVAILABLE_CHECKERS', available_projects)
    mocked_cache_latest_major_versions = mocker.patch(
        'projects.tasks.cache_latest_major_versions',
    )

    tasks.cache_all_projects_latest_major_versions()

    assert (
        mocked_cache_latest_major_versions.delay.call_count ==
        len(available_projects)
    )


def test_cache_latest_minor_versions(mocker):
    """
    Test `tasks.cache_latest_minor_versions`
    """
    mocker.patch('projects.tasks.AVAILABLE_CHECKERS', available_projects)
    project = available_projects['python']

    mocked_cache_set = mocker.patch('projects.tasks.cache.set')
    mocked_key = mocker.patch(
        'projects.tasks.utils.get_latest_minor_versions_key',
    )

    tasks.cache_latest_minor_versions('python')

    mocked_cache_set.assert_called_once_with(
        key=mocked_key.return_value,
        value=project.get_latest_minor_versions(),
    )


def test_cache_all_projects_latest_minor_versions(mocker):
    """
    Test `tasks.cache_all_projects_latest_minor_versions`
    """
    mocker.patch('projects.tasks.AVAILABLE_CHECKERS', available_projects)
    mocked_cache_latest_minor_versions = mocker.patch(
        'projects.tasks.cache_latest_minor_versions',
    )

    tasks.cache_all_projects_latest_minor_versions()

    assert (
        mocked_cache_latest_minor_versions.delay.call_count ==
        len(available_projects)
    )


def test_cache_latest_project_version(mocker):
    """
    Test `tasks.cache_latest_project_version`
    """
    mocker.patch('projects.tasks.AVAILABLE_CHECKERS', available_projects)
    project = available_projects['python']

    latest_version = '1.0.0'
    mocked_key = mocker.patch('projects.tasks.utils.get_latest_version_key')
    mocked_cache_get = mocker.patch(
        'projects.tasks.cache.get', return_value=latest_version,
    )

    mocked_cache_latest_major_versions = mocker.patch(
        'projects.tasks.cache_latest_major_versions',
    )
    mocked_cache_latest_minor_versions = mocker.patch(
        'projects.tasks.cache_latest_minor_versions',
    )

    # Same version
    project.get_latest_version.return_value = '1.0.0'

    tasks.cache_latest_project_version('python')

    mocked_key.assert_called_once_with(project.name)
    mocked_cache_get.assert_called_once_with(mocked_key.return_value)
    project.get_latest_version.assert_called_once_with()

    # Different version
    project.get_latest_version.return_value = '0.9.0'

    tasks.cache_latest_project_version('python')

    mocked_cache_latest_major_versions.delay.assert_called_once_with(
        project.name,
    )
    mocked_cache_latest_minor_versions.delay.assert_called_once_with(
        project.name,
    )


def test_cache_all_projects_latest_version(mocker):
    """
    Test `tasks.cache_all_projects_latest_version`
    """
    mocker.patch('projects.tasks.AVAILABLE_CHECKERS', available_projects)
    mocked_cache_latest_project_version = mocker.patch(
        'projects.tasks.cache_latest_project_version',
    )

    tasks.cache_all_projects_latest_version()

    assert (
        mocked_cache_latest_project_version.delay.call_count ==
        len(available_projects)
    )
