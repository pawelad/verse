"""
Projects module Celery tasks
"""
from django.core.cache import cache

from celery.schedules import crontab

from checkers.projects import AVAILABLE_CHECKERS
from projects import utils
from verse.celery import app as celery_app


@celery_app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # Updates latest versions for all projects every hour
    sender.add_periodic_task(
        crontab(minute=0),
        cache_all_projects_latest_version.s(),
    )

    # Updates latest major and minor versions for all projects every six hours
    sender.add_periodic_task(
        crontab(minute=0, hour='*/6'),
        cache_all_projects_latest_major_versions.s(),
    )
    sender.add_periodic_task(
        crontab(minute=0, hour='*/6'),
        cache_all_projects_latest_minor_versions.s(),
    )


@celery_app.task
def cache_latest_major_versions(project_name):
    """
    Celery task responsible for getting and caching latest major versions
    for passed project

    :param project_name: name of the project to check
    :type project_name: str
    """
    project = AVAILABLE_CHECKERS[project_name]

    cache.set(
        key=utils.get_latest_major_versions_key(project.name),
        value=project.get_latest_major_versions(),
    )


@celery_app.task
def cache_all_projects_latest_major_versions():
    """
    Celery task responsible for getting and caching latest major versions
    for all projects
    """
    for project in AVAILABLE_CHECKERS.values():
        cache_latest_major_versions.delay(project.name)


@celery_app.task
def cache_latest_minor_versions(project_name):
    """
    Celery task responsible for getting and caching latest minor versions
    for passed project

    :param project_name: name of the project to check
    :type project_name: str
    """
    project = AVAILABLE_CHECKERS[project_name]

    cache.set(
        key=utils.get_latest_minor_versions_key(project.name),
        value=project.get_latest_minor_versions(),
    )


@celery_app.task
def cache_all_projects_latest_minor_versions():
    """
    Celery task responsible for getting and caching latest minor versions
    for all projects
    """
    for project in AVAILABLE_CHECKERS.values():
        cache_latest_minor_versions.delay(project.name)


@celery_app.task
def cache_latest_project_version(project_name):
    """
    Celery task responsible for getting and caching latest version
    for passed project

    :param project_name: name of the project to check
    :type project_name: str
    """
    project = AVAILABLE_CHECKERS[project_name]

    key = utils.get_latest_version_key(project.name)
    current_version = cache.get(key)
    latest_version = project.get_latest_version()

    if latest_version != current_version:
        cache.set(key, latest_version)

        # Also update other values
        cache_latest_major_versions.delay(project.name)
        cache_latest_minor_versions.delay(project.name)


@celery_app.task
def cache_all_projects_latest_version():
    """
    Celery task responsible for getting and caching latest version
    for all projects
    """
    for project in AVAILABLE_CHECKERS.values():
        cache_latest_project_version.delay(project.name)
