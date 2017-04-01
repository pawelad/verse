"""
Versions module URLs config
"""
from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

from versions import views


urlpatterns = [
    url(r'^latest/', include([
        url(
            r'^$',
            views.ProjectsVersionsViewSet.as_view(
                actions={'get': 'list'},
                suffix='List',
            ),
            name='list',
        ),
        url(
            r'^(?P<name>[-_\w]+)/$',
            views.ProjectsVersionsViewSet.as_view(
                actions={'get': 'retrieve'},
                suffix='Latest',
            ),
            name='latest',
        ),
        url(
            r'^(?P<name>[-_\w]+)/major/$',
            views.ProjectsVersionsViewSet.as_view(
                actions={'get': 'major'},
                suffix='Major',
            ),
            name='major',
        ),
        url(
            r'^(?P<name>[-_\w]+)/minor/$',
            views.ProjectsVersionsViewSet.as_view(
                actions={'get': 'minor'},
                suffix='Minor',
            ),
            name='minor',
        ),
    ], namespace='versions')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
