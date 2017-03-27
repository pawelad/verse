"""
Verse main urls config
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import SimpleRouter
from rest_framework.schemas import get_schema_view

from versions import views


router = SimpleRouter()
router.register(r'', views.ProjectsVersionsViewSet, base_name='versions')

schema_view = get_schema_view(title='Verse API')


urlpatterns = [
    # API
    url(r'^api/v1/', include([
        url(r'^', include(router.urls)),
    ])),

    url(
        r'^docs/',
        include_docs_urls(
            title="Verse API",
            description="Latest project versions, simplified and centralized",
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
