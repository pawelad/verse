"""
Verse application main urls config
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Django REST Framework
    url(r'^api-auth/', include('rest_framework.urls')),

    # Django Admin
    url(r'^django_admin/', admin.site.urls),
]

# Serve static files on runserver
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
