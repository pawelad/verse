"""
Verse main urls config
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView

from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from verse.views import IndexView


schema_view = get_schema_view(title='Verse API')


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),

    # API
    url(r'^', include('versions.urls')),

    url(
        r'^docs/',
        include_docs_urls(
            title="Verse API",
            description="Check what's the latest version of your favorite "
                        "open-source project",
        )
    ),
    url(r'^schema/$', schema_view),

    # Django Admin
    url(r'^django_admin/', admin.site.urls),
]

# Serve static files on runserver
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
