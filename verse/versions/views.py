"""
Versions module API views
"""
from django.http import Http404

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from checkers.projects import AVAILABLE_CHECKERS
from versions.latest import (
    get_latest_version, get_latest_major_versions, get_latest_minor_versions,
)


class ListProjects(APIView):
    """
    View that returns a list of all project with implemented checkers
    """
    def get(self, request, format=None):
        """
        Returns a list of all supported projects with links to
        API endpoints for their latest version
        """
        projects = dict()
        for project_name in AVAILABLE_CHECKERS:
            latest_url = reverse(
                'api:versions:latest', args=[project_name], request=request,
            )
            major_versions_url = reverse(
                'api:versions:major', args=[project_name], request=request,
            )
            minor_versions_url = reverse(
                'api:versions:minor', args=[project_name], request=request,
            )

            projects[project_name] = {
                'latest': latest_url,
                'latest_major': major_versions_url,
                'latest_minor': minor_versions_url,
            }

        return Response(projects)


class SpecificProjectMixin:
    """
    CBV mixin for specific project related API views
    """
    def get_object(self, name):
        """
        Try to get project checker if it exists, return HTTP 404
        if it doesn't

        :param name: name of the project
        :type name: str
        :returns: project checker instance
        :rtype: checkers.base.BaseChecker
        """
        try:
            return AVAILABLE_CHECKERS[name]()
        except KeyError:
            raise Http404


class GetLatestProjectVersion(SpecificProjectMixin, APIView):
    """
    View that returns project latest version
    """
    def get(self, request, name, format=None):
        """
        Returns project latest version
        """
        project = self.get_object(name)
        latest_version = get_latest_version(project)

        major_versions_url = reverse(
            'api:versions:major', args=[name], request=request,
        )
        minor_versions_url = reverse(
            'api:versions:minor', args=[name], request=request,
        )
        data = {
            'latest': latest_version,
            'major': major_versions_url,
            'minor': minor_versions_url,
        }
        return Response(data)


class GetLatestMajorProjectVersions(SpecificProjectMixin, APIView):
    """
    View that returns project latest major versions
    """
    def get(self, request, name, format=None):
        """
        Returns project latest major versions
        """
        project = self.get_object(name)
        latest_versions = get_latest_major_versions(project)
        return Response(latest_versions)


class GetLatestMinorProjectVersions(SpecificProjectMixin, APIView):
    """
    View that returns project latest minor versions
    """
    def get(self, request, name, format=None):
        """
        Returns project latest minor versions
        """
        project = self.get_object(name)
        latest_versions = get_latest_minor_versions(project)
        return Response(latest_versions)
