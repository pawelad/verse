"""
Verse application main urls config
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework.routers import SimpleRouter

from versions import views


router = SimpleRouter()
router.register(r'', views.ProjectsVersionsViewSet, base_name='versions')


urlpatterns = [
    # API
    url(r'^api/v1/', include([
        url(r'^', include(router.urls)),
    ])),

    # Django Admin
    url(r'^django_admin/', admin.site.urls),
]

# Serve static files on runserver
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
