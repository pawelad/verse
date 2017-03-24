"""
Versions module URLs config
"""
from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

from versions import views


urlpatterns = [
    url(r'^$', views.ListProjects.as_view(), name='list'),
    url(r'^(?P<name>[\w-]+)/', include([
        url(
            r'^$',
            views.GetLatestProjectVersion.as_view(),
            name='latest',
        ),
        url(
            r'^major/$',
            views.GetLatestMajorProjectVersions.as_view(),
            name='major',
        ),
        url(
            r'^minor/$',
            views.GetLatestMinorProjectVersions.as_view(),
            name='minor',
        ),
    ])),
]

urlpatterns = format_suffix_patterns(urlpatterns)
