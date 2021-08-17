from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from lab import views as lab_views

#  JWT認証機能　jwtのViewにURLを通す
# https://jpadilla.github.io/django-rest-framework-jwt/#rest-framework-jwt-auth
# from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token 

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    # path('users/', views.UserListView.as_view()),
    path('lab/', lab_views.LabListView.as_view()),
    path('lab/<int:pk>/', lab_views.LabView.as_view()),
    path('lab/<int:lab_id>/deck/', lab_views.DeckListView.as_view()),
    path('lab/<int:lab_id>/deck/<int:pk>/', lab_views.DeckView.as_view()),
    path('lab/<int:lab_id>/<int:deck_id>/card/', lab_views.CardListView.as_view()),
    path('lab/<int:lab_id>/<int:deck_id>/card/<int:pk>/', lab_views.CardView.as_view()),
    # path('token/obtain', obtain_jwt_token),     # JWT認証機能　トークン発行
    # path('token/verify', verify_jwt_token),     # JWT認証機能　トークンチェック
    # path('token/refresh', refresh_jwt_token),   # JWT認証機能　トークン更新
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
