
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/boards/', include('boards.urls')),
    path('api/v1/auth/base/', include("djoser.urls")),
    path('api/v1/auth/', include("djoser.urls.authtoken")),
    path('api/v1/jwt/', TokenObtainPairView.as_view()),
    path('api/v1/jwt/refresh/', TokenRefreshView.as_view()),
]
