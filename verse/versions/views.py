"""
Versions module API views
"""
from django.core.cache import cache
from django.http import Http404

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from checkers.projects import AVAILABLE_CHECKERS
from versions.latest import (
    get_latest_version, get_latest_major_versions, get_latest_minor_versions,
)
from versions import utils


class ProjectsVersionsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for listing and viewing project versions
    """
    lookup_field = 'name'

    def get_object(self):
        """
        Try to get project checker if it exists, return HTTP 404
        if it doesn't

        :returns: project checker instance
        :rtype: checkers.base.BaseChecker
        """
        try:
            return AVAILABLE_CHECKERS[self.kwargs['name']]()
        except KeyError:
            raise Http404

    def list(self, request, *args, **kwargs):
        """
        Return a list of all supported projects with links to
        API endpoints for their latest versions
        """
        # It should always be cached on startup, but just in case let's
        # allow setting the value here as well
        projects = cache.get_or_set(
            key=utils.AVAILABLE_PROJECTS_KEY,
            default=utils.get_projects,
            timeout=None,  # This will be invalidated in app restart
        )

        return Response(projects)

    def retrieve(self, request, *args, **kwargs):
        """
        Return project latest version
        """
        project = self.get_object()
        latest_version = get_latest_version(project)
        return Response({
            'latest': latest_version,
        })

    @detail_route(methods=['get'])
    def major(self, request, *args, **kwargs):
        """
        Returns project latest major versions
        """
        project = self.get_object()
        latest_versions = get_latest_major_versions(project)
        return Response(latest_versions)

    @detail_route(methods=['get'])
    def minor(self, request,  *args, **kwargs):
        """
        Returns project latest minor versions
        """
        project = self.get_object()
        latest_versions = get_latest_minor_versions(project)
        return Response(latest_versions)
