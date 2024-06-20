from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


urlpatterns = [
    # Admin
    path("staff/", admin.site.urls),

    # Core
    path("", include("apps.core.urls")),

    # Media
    re_path(
        r'^media/(?P<path>.*)$',
        serve,
        {'document_root': settings.MEDIA_ROOT}
    ),

    # Static
    re_path(
        r'^static/(?P<path>.*)$',
        serve,
        {'document_root': settings.STATIC_ROOT}
    ),
]

if settings.DEBUG:
    schema_view = get_schema_view(
        openapi.Info(
            title=settings.PROJECT_NAME,
            default_version=f"v{getattr(settings, 'VERSION', '0.1.0')}",
            terms_of_service="https://www.example.com/terms/",
            contact=openapi.Contact(email=settings.SWAGGER_OPENAPI_CONTACT),
            license=openapi.License(name=settings.SWAGGER_OPENAPI_LICENSE),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
        path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "redoc/",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc"
        ),
    ]
