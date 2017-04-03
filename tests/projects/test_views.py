"""
Test `projects.views` file
"""
from unittest.mock import MagicMock

from django.http import Http404
from django.utils.crypto import get_random_string
from rest_framework import viewsets, status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

import pytest
from github3.repos import Repository

from checkers.base import BaseVersionChecker, GitHubVersionChecker
from projects import utils
from projects import views


available_projects = {'python': MagicMock(spec=BaseVersionChecker)}


class TestProjectsVersionsViewSet:
    """
    Tests for 'views.ProjectsVersionsViewSet'
    """
    client = APIClient()
    base_name = 'projects'

    @pytest.fixture
    def instance(self):
        return views.ProjectsVersionsViewSet()

    def test_view_inheritance(self, instance):
        """Test view inheritance name"""
        assert isinstance(instance, viewsets.ReadOnlyModelViewSet)

    @pytest.mark.parametrize('suffix, expected', [
        ('List', 'Projects list'),
        ('Latest', 'Latest project version'),
        ('Major', 'Latest major versions'),
        ('Minor', 'Latest minor versions'),
    ])
    def test_view_get_view_name_method(self, instance, suffix, expected):
        """Test view `get_view_name()` method"""
        instance.suffix = suffix

        assert instance.get_view_name() == expected

    def test_view_get_object_method(self, mocker, instance):
        """Test view `get_object()` method"""
        mocker.patch('projects.views.AVAILABLE_CHECKERS', available_projects)

        instance.kwargs = {'project': 'python'}
        assert isinstance(instance.get_object(), MagicMock)

        # Nonexistent project
        instance.kwargs = {'project': get_random_string()}
        with pytest.raises(Http404):
            instance.get_object()

    def test_view_list_method(self, mocker):
        """Test view `list()` method"""
        projects = {get_random_string(): get_random_string()}
        mocked_get_projects = mocker.patch(
            'projects.views.utils.get_projects',
        )
        mocked_get_or_set = mocker.patch(
            'projects.views.cache.get_or_set',
            return_value=projects
        )

        url = reverse('{0.base_name}:list'.format(self))
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == projects

        mocked_get_or_set.assert_called_once_with(
            key=utils.AVAILABLE_PROJECTS_KEY,
            default=mocked_get_projects.return_value,
            timeout=None,
        )

    def test_view_retrieve_method(self, mocker):
        """Test view `retrieve()` method"""
        mocker.patch('projects.views.AVAILABLE_CHECKERS', available_projects)
        project = available_projects['python']

        latest_version = '0.1.1'
        mocked_get_or_set = mocker.patch(
            'projects.views.cache.get_or_set', return_value=latest_version,
        )
        mocked_key = mocker.patch(
            'projects.tasks.utils.get_latest_version_key'
        )

        url = reverse('{0.base_name}:latest'.format(self), args=['python'])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'latest': latest_version,
        }

        # Wrong project name
        url = reverse(
            '{0.base_name}:latest'.format(self), args=[get_random_string()],
        )
        response = self.client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

        mocked_key.assert_called_once_with(project.slug)

        mocked_get_or_set.assert_called_once_with(
            key=mocked_key.return_value,
            default=project.get_latest_version,
            timeout=60 * 60,
        )

    def test_view_major_method(self, mocker):
        """Test view `major()` method"""
        mocker.patch('projects.views.AVAILABLE_CHECKERS', available_projects)
        project = available_projects['python']

        latest_versions = {
            '1': '1.2.3',
            '0': '0.12.0',
        }
        mocked_get_or_set = mocker.patch(
            'projects.views.cache.get_or_set',
            return_value=latest_versions,
        )
        mocked_key = mocker.patch(
            'projects.tasks.utils.get_latest_major_versions_key',
        )

        url = reverse('{0.base_name}:major'.format(self), args=['python'])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == latest_versions

        # Wrong project name
        url = reverse(
            '{0.base_name}:major'.format(self), args=[get_random_string()],
        )
        response = self.client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

        mocked_key.assert_called_once_with(project.slug)

        mocked_get_or_set.assert_called_once_with(
            key=mocked_key.return_value,
            default=project.get_latest_major_versions,
            timeout=60 * 60 * 6,
        )

    def test_view_minor_method(self, mocker):
        """Test view `minor()` method"""
        mocker.patch('projects.views.AVAILABLE_CHECKERS', available_projects)
        project = available_projects['python']

        latest_versions = {
            '1.2': '1.2.3',
            '1.1': '1.1.4',
            '1.0': '1.0.2',
        }
        mocked_get_or_set = mocker.patch(
            'projects.views.cache.get_or_set',
            return_value=latest_versions,
        )
        mocked_key = mocker.patch(
            'projects.tasks.utils.get_latest_minor_versions_key',
        )

        url = reverse('{0.base_name}:minor'.format(self), args=['python'])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == latest_versions

        # Wrong project name
        url = reverse(
            '{0.base_name}:minor'.format(self), args=[get_random_string()],
        )
        response = self.client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

        mocked_key.assert_called_once_with(project.slug)

        mocked_get_or_set.assert_called_once_with(
            key=mocked_key.return_value,
            default=project.get_latest_minor_versions,
            timeout=60 * 60 * 6,
        )


class TestGitHubProjectsVersionsViewSet:
    """
    Tests for 'views.GitHubProjectsVersionsViewSet'
    """
    client = APIClient()
    base_name = 'github-projects'

    @pytest.fixture
    def instance(self):
        return views.GitHubProjectsVersionsViewSet()

    def test_view_inheritance(self, instance):
        """Test view inheritance name"""
        assert isinstance(instance, viewsets.ReadOnlyModelViewSet)

    @pytest.mark.parametrize('suffix, expected', [
        ('Latest', 'Latest GitHub repository version'),
        ('Major', 'Latest major versions'),
        ('Minor', 'Latest minor versions'),
    ])
    def test_view_get_view_name_method(self, instance, suffix, expected):
        """Test view `get_view_name()` method"""
        instance.suffix = suffix

        assert instance.get_view_name() == expected

    def test_view_get_object_method(self, mocker, instance):
        """Test view `get_object()` method"""
        instance.kwargs = {
            'owner': 'pawelad',
            'repo': 'verse',
        }

        mocked_repo = MagicMock(autospec=Repository)
        mocked_github_client = mocker.patch('projects.views.github_client')
        mocked_github_client.repository.return_value = mocked_repo

        checker = instance.get_object()

        assert isinstance(checker, GitHubVersionChecker)
        assert checker.slug == 'gh-pawelad-verse'
        assert checker.homepage == 'https://github.com/pawelad/verse'
        assert checker.repository == 'https://github.com/pawelad/verse'

        # Nonexistent GitHub repository
        mocked_github_client.repository.return_value = None

        with pytest.raises(Http404):
            instance.get_object()

    def test_view_list_method(self, instance):
        """Test view `list()` method"""
        with pytest.raises(Http404):
            instance.list(request=MagicMock())
