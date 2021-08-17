from django.db.models.query import QuerySet
from rest_framework import serializers
from .models import Labs, Decks, Cards, Records

class LabSerializer(serializers.ModelSerializer):

  deck_count = serializers.SerializerMethodField()

  class Meta:
  # 対象のモデルクラス
    model = Labs
    # 利用するモデルのフィールドを指定　
    fields = ['id', 'title', 'description', 'is_active','deck_count']
    validaters=[]

  def get_deck_count(self, obj):
    count = Decks.objects.all().filter( lab_id = obj.id).count()
    return count

class DeckSerializer(serializers.ModelSerializer):
  lab = LabSerializer
  card_count = serializers.SerializerMethodField()

  class Meta:
  # 対象のモデルクラス
    model = Decks
    # 利用するモデルのフィールドを指定
    fields = ['id', 'title', 'comment', 'create_at', 'update_at', 'card_count']

  def get_card_count(self, obj):
    count = Cards.objects.all().filter( lab_id=obj.lab_id ,deck_id = obj.id).count()
    return count

class CardSerializer(serializers.ModelSerializer):
  lab = LabSerializer
  deck = DeckSerializer
  class Meta:
  # 対象のモデルクラス
    model = Cards
    # 利用するモデルのフィールドを指定
    fields = ['id', 'title', 'comment', 'create_at', 'update_at']


class RecordSerializer(serializers.ModelSerializer):
  lab = LabSerializer
  deck = DeckSerializer
  card = CardSerializer
  class Meta:
  # 対象のモデルクラス
    model = Records
    # 利用するモデルのフィールドを指定
    fields = '__all__'






