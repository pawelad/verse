"""
Test `versions.views` file
"""
from unittest.mock import MagicMock

from django.http import Http404
from django.utils.crypto import get_random_string

from rest_framework import viewsets, status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

import pytest

from checkers.base import BaseVersionChecker
from versions import utils
from versions.views import ProjectsVersionsViewSet


available_projects = {'python': MagicMock(spec=BaseVersionChecker)}


class TestProjectsVersionsViewSet:
    """
    Tests for 'versions.views.ProjectsVersionsViewSet'
    """
    client = APIClient()
    view = ProjectsVersionsViewSet
    base_name = 'versions'

    def test_view_inheritance(self):
        """Test view inheritance name"""
        assert isinstance(self.view(), viewsets.ReadOnlyModelViewSet)

    def test_view_lookup_field(self):
        """Test view lookup field"""
        assert self.view.lookup_field == 'name'

    @pytest.mark.parametrize('suffix, expected', [
        ('List', 'Projects list'),
        ('Instance', 'Latest project version'),
        ('Major', 'Latest major versions'),
        ('Minor', 'Latest minor versions'),
    ])
    def test_view_get_view_name_method(self, suffix, expected):
        """Test view `get_view_name()` method"""
        instance = self.view()
        instance.suffix = suffix

        assert instance.get_view_name() == expected

    def test_view_get_object_method(self, mocker):
        """Test view `get_object()` method"""
        mocker.patch('versions.views.AVAILABLE_CHECKERS', available_projects)
        instance = self.view()

        instance.kwargs = {'name': 'python'}
        assert isinstance(instance.get_object(), MagicMock)

        instance.kwargs = {'name': get_random_string()}
        with pytest.raises(Http404):
            instance.get_object()

    def test_view_list_method(self, mocker):
        """Test view `list()` method"""
        projects = {get_random_string(): get_random_string()}
        mocked_get_projects = mocker.patch(
            'versions.views.utils.get_projects',
        )
        mocked_get_or_set = mocker.patch(
            'versions.views.cache.get_or_set',
            return_value=projects
        )

        url = reverse('{0.base_name}-list'.format(self))
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
        mocker.patch('versions.views.AVAILABLE_CHECKERS', available_projects)
        project = available_projects['python']

        latest_version = '0.1.1'
        mocked_get_or_set = mocker.patch(
            'versions.views.cache.get_or_set', return_value=latest_version,
        )
        mocked_key = mocker.patch('versions.tasks.utils.get_latest_version_key')

        url = reverse('{0.base_name}-detail'.format(self), args=['python'])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'latest': latest_version,
        }

        # Wrong project name
        url = reverse(
            '{0.base_name}-detail'.format(self), args=[get_random_string()],
        )
        response = self.client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

        mocked_key.assert_called_once_with(project.name)

        mocked_get_or_set.assert_called_once_with(
            key=mocked_key.return_value,
            default=project.get_latest_version,
            timeout=60 * 60,
        )

    def test_view_major_method(self, mocker):
        """Test view `major()` method"""
        mocker.patch('versions.views.AVAILABLE_CHECKERS', available_projects)
        project = available_projects['python']

        latest_versions = {
            '1': '1.2.3',
            '0': '0.12.0',
        }
        mocked_get_or_set = mocker.patch(
            'versions.views.cache.get_or_set',
            return_value=latest_versions
        )
        mocked_key = mocker.patch(
            'versions.tasks.utils.get_latest_major_versions_key',
        )

        url = reverse('{0.base_name}-major'.format(self), args=['python'])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == latest_versions

        # Wrong project name
        url = reverse(
            '{0.base_name}-major'.format(self), args=[get_random_string()],
        )
        response = self.client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

        mocked_key.assert_called_once_with(project.name)

        mocked_get_or_set.assert_called_once_with(
            key=mocked_key.return_value,
            default=project.get_latest_major_versions,
            timeout=60 * 60 * 6,
        )

    def test_view_minor_method(self, mocker):
        """Test view `minor()` method"""
        mocker.patch('versions.views.AVAILABLE_CHECKERS', available_projects)
        project = available_projects['python']

        latest_versions = {
            '1.2': '1.2.3',
            '1.1': '1.1.4',
            '1.0': '1.0.2',
        }
        mocked_get_or_set = mocker.patch(
            'versions.views.cache.get_or_set',
            return_value=latest_versions,
        )
        mocked_key = mocker.patch(
            'versions.tasks.utils.get_latest_minor_versions_key',
        )

        url = reverse('{0.base_name}-minor'.format(self), args=['python'])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == latest_versions

        # Wrong project name
        url = reverse(
            '{0.base_name}-minor'.format(self), args=[get_random_string()],
        )
        response = self.client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

        mocked_key.assert_called_once_with(project.name)

        mocked_get_or_set.assert_called_once_with(
            key=mocked_key.return_value,
            default=project.get_latest_minor_versions,
            timeout=60 * 60 * 6,
        )
