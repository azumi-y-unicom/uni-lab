from django_filters import rest_framework as filters
from rest_framework import status, views

# Generic viewを使用する場合
# from rest_framework import generics

# Model ViewSetsを使用する場合
# from rest_framework import viewsets

from .models import Users
from .serializers import UserSerializer, UserListSerializer
from rest_framework.response import Response

""" フィルター定義 """
class UserFilter(filters.FilterSet):
    model = Users
    fields = '__all__'

# Todo 
class UserDetailUpdateDestroyView(views.APIView):
    # ユーザー情報の詳細取得、更新、削除
    def get(self, request, *args, **kwargs):
        """ ユーザー情報詳細取得 """
        return ''

    def put(self, request, *args, **kwargs):
        """ ユーザー更新 """
        return ''

    def delete(self, request, *args, **kwargs):
        """ ユーザー削除 """
        return ''

class UserListView(views.APIView):
    # ユーザー一覧取得
    def get(self, request, *args, **kwargs):
        """ ユーザー情報一覧取得 """
        # モデルオブジェクトの一覧を取得する
        user_list = Users.objects.all()
        # シリアライザオブジェクト作成
        serializer = UserSerializer(instance=user_list, many=True)
        # シリアライザオブジェクト中のデータをレスポンスに返す
        return Response(serializer.data, status.HTTP_200_OK)

# Todo 
class UserCreateView(views.APIView):
    # ユーザー情報登録    
    def post(self, request, *args, **kwargs):
        """ ユーザー情報登録 """
        # シリアライザオブジェクト作成
        # バリデーション実行
        # モデルオブジェクト登録
        # レスポンスオブジェクト作成
        return ''

