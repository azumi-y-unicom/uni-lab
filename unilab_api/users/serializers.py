from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # 対象のモデルクラス
        model = Users
        # 利用するモデルのフィールドを指定　今回はすべて
        fields = ['id','userid','name','create_at','update_at']



class UserListSerializer(serializers.ListSerializer):
    # 複数のユーザー情報モデルのシリアライザー
    child = UserSerializer()


