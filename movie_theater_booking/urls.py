from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from django.urls import path, include

urlpatterns = [
     path('admin/', admin.site.urls),
    path('', include('bookings.urls')),  # This makes home the root URL
    path('api/', include('bookings.urls')),  # REST API endpoints
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)