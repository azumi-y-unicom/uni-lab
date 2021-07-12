from django.db.models.query import QuerySet
from rest_framework import serializers
from .models import Labs, Decks, Cards, Records

class LabSerializer(serializers.ModelSerializer):
  class Meta:
  # 対象のモデルクラス
    model = Labs
    # 利用するモデルのフィールドを指定　
    fields = ['id', 'title', 'description', 'is_active']
    validaters=[]

  def create(self, validated_data):
    instance = Labs(**validated_data)
    
    return instance


class DeckSerializer(serializers.ModelSerializer):
  lab = LabSerializer
  class Meta:
  # 対象のモデルクラス
    model = Decks
    # 利用するモデルのフィールドを指定
    fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
  lab = LabSerializer
  deck = DeckSerializer
  class Meta:
  # 対象のモデルクラス
    model = Cards
    # 利用するモデルのフィールドを指定
    fields = '__all__'


class RecordSerializer(serializers.ModelSerializer):
  lab = LabSerializer
  deck = DeckSerializer
  card = CardSerializer
  class Meta:
  # 対象のモデルクラス
    model = Records
    # 利用するモデルのフィールドを指定
    fields = '__all__'






