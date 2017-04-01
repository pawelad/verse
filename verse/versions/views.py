"""
Versions module API views
"""
from django.core.cache import cache
from django.http import Http404

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from checkers.projects import AVAILABLE_CHECKERS
from versions import utils


class ProjectsVersionsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint returns latest version information for the passed project.
    It's readonly and has four simple methods:

    - `/`: Returns a list of all currently supported projects with links to
      relevant API endpoints
    - `/:project`: Returns project latest stable version
    - `/:project/major`: Returns project latest stable version for each
      major release
    - `/:project/minor`: Returns project latest stable version for each
      minor release
    """
    def get_view_name(self):
        """
        Extends DRF's `get_view_name()` method and try to return more user
        friendly view names for the browsable API
        """
        suffix = getattr(self, 'suffix', None)
        if suffix == 'List':
            return 'Projects list'
        elif suffix == 'Latest':
            return 'Latest project version'
        elif suffix == 'Major':
            return 'Latest major versions'
        elif suffix == 'Minor':
            return 'Latest minor versions'

        return super().get_view_name()

    def get_object(self):
        """
        Tries to get specific project checker instance if it exists,
        returns HTTP 404 if it doesn't

        :returns: project checker instance
        :rtype: checkers.base.BaseChecker
        """
        project_name = self.kwargs.get('name', None)

        try:
            return AVAILABLE_CHECKERS[project_name]
        except KeyError:
            raise Http404

    def list(self, request, *args, **kwargs):
        """
        Returns a list of all currently supported projects with links to
        relevant API endpoints
        """
        # Project list can only change with code addition and app restart,
        # so it makes sense to cache it on first request after restart
        projects = cache.get_or_set(
            key=utils.AVAILABLE_PROJECTS_KEY,
            default=utils.get_projects(request),
            timeout=None,  # This will be invalidated on app restart
        )

        return Response(projects)

    def retrieve(self, request, *args, **kwargs):
        """
        Returns project latest stable version
        """
        project = self.get_object()

        latest_version = cache.get_or_set(
            key=utils.get_latest_version_key(project.name),
            default=project.get_latest_version,
            timeout=60 * 60,  # 1 hour
        )

        return Response({
            'latest': latest_version,
        })

    @detail_route(methods=['get'])
    def major(self, request, *args, **kwargs):
        """
        Returns project latest stable version for each major release
        """
        project = self.get_object()

        latest_versions = cache.get_or_set(
            key=utils.get_latest_major_versions_key(project.name),
            default=project.get_latest_major_versions,
            timeout=60 * 60 * 6,  # 6 hours
        )

        return Response(latest_versions)

    @detail_route(methods=['get'])
    def minor(self, request,  *args, **kwargs):
        """
        Returns project latest stable version for each minor release
        """
        project = self.get_object()

        latest_versions = cache.get_or_set(
            key=utils.get_latest_minor_versions_key(project.name),
            default=project.get_latest_minor_versions,
            timeout=60 * 60 * 6,  # 6 hours
        )

        return Response(latest_versions)
