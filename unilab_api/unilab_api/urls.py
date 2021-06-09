from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from users import views
#  JWT認証機能　jwtのViewにURLを通す
# https://jpadilla.github.io/django-rest-framework-jwt/#rest-framework-jwt-auth
# from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token 

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('users/', views.UserListView.as_view()),
    # path('token/obtain', obtain_jwt_token),     # JWT認証機能　トークン発行
    # path('token/verify', verify_jwt_token),     # JWT認証機能　トークンチェック
    # path('token/refresh', refresh_jwt_token),   # JWT認証機能　トークン更新
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
