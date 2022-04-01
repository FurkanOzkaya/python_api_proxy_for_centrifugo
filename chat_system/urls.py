"""chat_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from user.views.v1.token import JWTTokenObtainPairView, JWTTokenRefreshView, refresh_token_ws

schema_view = get_schema_view(
    openapi.Info(
        title="User Api",
        default_version='v1',
        description="",
        contact=openapi.Contact(email="furkanozkaya45@gmail.com"),
        license=openapi.License(name="Quick Start User Api"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger',
                                      cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
    path('api/user/', include('user.views.v1.urls')),
    path('chat/', include('chat.urls')),
    path('api/token/', JWTTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', JWTTokenRefreshView.as_view(), name='token_refresh'),
    path('ws/token/refresh/', refresh_token_ws, name='token_refresh'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
