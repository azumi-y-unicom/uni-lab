from functools import partial
from rest_framework import status, views
from rest_framework import response
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters

from .models import Labs, Decks
from .serializers import LabSerializer, DeckSerializer

class LabListView(views.APIView):
  # リスト
  def get(self, request, *args, **kwargs):
    labs_list = Labs.objects.filter(is_active=True)
    # シリアライザオブジェクト作成
    serializer = LabSerializer(instance=labs_list, many=True)
    # シリアライザオブジェクト中のデータをレスポンスに返す
    result = {"list": serializer.data}
    return Response(result, status.HTTP_200_OK)

  def post(self, request, *args, **kwargs):
    lab_model = Labs.objects.create(
      title = request.data["title"], 
      description = request.data["description"], 
      is_active =  request.data["is_active"])
    serializer = LabSerializer(lab_model)
    response = {"result": serializer.data}
    return Response(response,  status.HTTP_201_CREATED)

class LabView(views.APIView):
  # 詳細データ取得・編纂
  def get(self, request, pk, *args, **kwargs):
    # 主キーに一致するオブジェクト所得
    lab_model = get_object_or_404(Labs, pk=pk)
    serializer = LabSerializer(lab_model)
    return Response(serializer.data, status.HTTP_200_OK)

  def patch(self, request, pk, *args, **kwargs):
    lab_model = get_object_or_404(Labs, pk=pk)

    serializer = LabSerializer(instance=lab_model, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    response = {"result": serializer.data}    
    return Response(response, status.HTTP_200_OK)

  def delete(self,request,pk=None):
    lab_model = get_object_or_404(Labs, pk=pk)
    lab_model.delete()
    return Response(status.HTTP_204_NO_CONTENT_OK)


class DeckFilter(filters.FilterSet):
  # フィルター条件設定数値一致
  id = filters.NumberFilter()
  lab = filters.NumberFilter()
  # 大文字小文字無視の部分一致
  title = filters.CharFilter(lookup_expr='icontains')
  comment = filters.CharFilter(lookup_expr='icontains')

  update_at__range = filters.DateTimeFilter(lookup_expr='range')
  class Meta:
    model = Decks
    fields = []
    # fields = ['id','lab', 'title', 'comment', 'update_at']

class DeckListView(views.APIView):
  def get(self, request, lab_id , *args, **kwargs):
    # タイトル情報
    lab_model = get_object_or_404(Labs, pk=lab_id)
    infomation_serializer = LabSerializer(lab_model)

    # モデルオブジェクトの一覧を取得する
    filterset = DeckFilter(request.query_params, queryset=Decks.objects.filter(lab=lab_id))
    list_serializer =DeckSerializer(instance=filterset.qs, many=True)
    # シリアライザオブジェクト中のデータをレスポンスに返す
    result = {
      "infomation": infomation_serializer.data,
      "list": list_serializer.data}
    return Response(result, status.HTTP_200_OK)

  def post(self, request,lab_id, *args, **kwargs):
    # Labのインスタンスを取得
    lab_model = Labs.objects.get(id=lab_id)
    # Deckの登録
    deck_model = Decks.objects.create(
      title = request.data["title"], 
      comment = request.data["comment"], 
      lab = lab_model)
    serializer = DeckSerializer(deck_model)
    response = {"result_id": "1", "result": serializer.data}
    return Response(response,  status.HTTP_201_CREATED)
  
class DeckView(views.APIView):
  # 詳細データ取得・編纂
  def get(self, request, lab_id, pk, *args, **kwargs):
    deck_model = get_object_or_404(Decks, pk=pk)
    serializer = DeckSerializer(deck_model)
    return Response(serializer.data, status.HTTP_200_OK)

  def patch(self, request, lab_id, pk, *args, **kwargs):
    deck_model = get_object_or_404(Labs, pk=pk)

    serializer = DeckSerializer(instance=deck_model, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    response = {"result": serializer.data}    
    return Response(response, status.HTTP_200_OK)

  def delete(self,request,lab_id, pk=None):
    deck_model = get_object_or_404(Labs, pk=pk)
    deck_model.delete()
    return Response(status.HTTP_204_NO_CONTENT_OK)



class CardListView(views.APIView):
  def get(self, request, lab_id , *args, **kwargs):
    # タイトル情報
    lab_model = get_object_or_404(Labs, pk=lab_id)
    infomation_serializer = LabSerializer(lab_model)

    # モデルオブジェクトの一覧を取得する
    filterset = DeckFilter(request.query_params, queryset=Decks.objects.filter(lab=lab_id))
    list_serializer =DeckSerializer(instance=filterset.qs, many=True)
    # シリアライザオブジェクト中のデータをレスポンスに返す
    result = {
      "infomation": infomation_serializer.data,
      "list": list_serializer.data}
    return Response(result, status.HTTP_200_OK)

  def post(self, request,lab_id, *args, **kwargs):
    # Labのインスタンスを取得
    lab_model = Labs.objects.get(id=lab_id)
    # Deckの登録
    deck_model = Decks.objects.create(
      title = request.data["title"], 
      comment = request.data["comment"], 
      lab = lab_model)
    serializer = DeckSerializer(deck_model)
    response = {"result_id": "1", "result": serializer.data}
    return Response(response,  status.HTTP_201_CREATED)
  
class CardView(views.APIView):
  # 詳細データ取得・編纂
  def get(self, request, lab_id, pk, *args, **kwargs):
    deck_model = get_object_or_404(Decks, pk=pk)
    serializer = DeckSerializer(deck_model)
    return Response(serializer.data, status.HTTP_200_OK)

  def patch(self, request, lab_id, pk, *args, **kwargs):
    deck_model = get_object_or_404(Labs, pk=pk)

    serializer = DeckSerializer(instance=deck_model, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    response = {"result": serializer.data}    
    return Response(response, status.HTTP_200_OK)

  def delete(self,request,lab_id, pk=None):
    deck_model = get_object_or_404(Labs, pk=pk)
    deck_model.delete()
    return Response(status.HTTP_204_NO_CONTENT_OK)



