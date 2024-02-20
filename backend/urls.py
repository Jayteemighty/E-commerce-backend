from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from drf_spectacular.views import  SpectacularAPIView, SpectacularSwaggerView


schema_view = get_schema_view(
    openapi.Info(
        title="API Doc",
        default_version='v1',
        description="API description",
        #terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="tolujosh1@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes = (permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
    path('api/', include('product.urls')),
    path('api/', include('order.urls')),
    path('api/', include('accounts.urls')),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
