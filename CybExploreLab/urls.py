from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/labs/', include('labs.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),  # for login, logout, password reset
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # for registration
    path('api/profiles/', include('profiles.urls')),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
