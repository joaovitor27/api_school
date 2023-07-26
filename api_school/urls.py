from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title=settings.PROJECT_NAME,
        default_version='v1',
        description="API feita para fins de aprendizagem, no curso de django rest framework, na Alura.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email=settings.EMAIL_CONTACT),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()

urlpatterns = [
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger.yaml/', schema_view.without_ui(cache_timeout=0), name='schema-yaml'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('gerency-adm/', admin.site.urls),
    path('api/v1/', include('school.urls', namespace='v1')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
