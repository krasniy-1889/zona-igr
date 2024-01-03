from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("apps.api.urls")),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
]


if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
