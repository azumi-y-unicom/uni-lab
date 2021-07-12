from re import T
from django.db import models
from django.db.models.deletion import PROTECT
from datetime import datetime

# Labsモデル
class Labs(models.Model):
  class Meta:
    db_table = 'labs'
  
  id = models.AutoField(verbose_name='ID', primary_key=True, editable=False)
  title = models.CharField(verbose_name='タイトル', max_length=50)
  description = models.TextField(verbose_name='説明', null=True, blank=True )
  # 将来的に公開非公開分類がいる？
  is_active = models.BooleanField(verbose_name='アクティブフラグ', default=True,)
  create_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
  update_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

'''
  def __init__(self, title, description ):
    self.title = title
    self.description = description
    self.is_active = True
    self.create_at =  datetime.now()
    self.update_at =  datetime.now()
'''

# Decksモデル
class Decks(models.Model):
  class Meta:
    db_table = 'decks'
  
  id = models.AutoField(verbose_name='ID', primary_key=True, editable=False)
  # 外部キー
  lab = models.ForeignKey(Labs, verbose_name='Lab ID',
    on_delete=models.PROTECT, null=True, blank=True)
  title = models.CharField(verbose_name='タイトル', max_length=50)
  comment = models.TextField(verbose_name='コメント' )
  # テンプレなどを登録できるようにする
  create_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
  update_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

# Cardsモデル
class Cards(models.Model):
  class Meta:
    db_table = 'cards'
  
  id = models.AutoField(verbose_name='ID', primary_key=True, editable=False)
  # 外部キー
  lab = models.ForeignKey(Labs, verbose_name='Lab ID',
    on_delete=models.PROTECT, null=True, blank=True)
  deck = models.ForeignKey(Decks, verbose_name='Deck ID',
    on_delete=models.PROTECT, null=True, blank=True)
  title = models.CharField(verbose_name='タイトル', max_length=50)
  comment = models.TextField(verbose_name='コメント' )
  # テンプレなどを登録できるようにする
  create_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
  update_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)


# Recordsモデル
class Records(models.Model):
  class Meta:
    db_table = 'records'

  id = models.AutoField(verbose_name='ID', primary_key=True, editable=False)
  lab = models.ForeignKey(Labs, verbose_name='Lab ID',
    on_delete=models.PROTECT, null=True, blank=True)
  deck = models.ForeignKey(Decks, verbose_name='Deck ID',
    on_delete=models.PROTECT, null=True, blank=True)
  card = models.ForeignKey(Cards, verbose_name='Card ID',
    on_delete=models.PROTECT, null=True, blank=True)

  # 想定せいぜい5くらい
  rec_no = models.SmallIntegerField(verbose_name='カード内番号', null=True, blank=True)
  is_main_recode = models.BooleanField(verbose_name='メインレコードフラグ', default=False,)
  file_name = models.CharField(verbose_name='ファイル名', max_length=50)
  file = models.FileField( null=True, blank=True)
  create_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
  update_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

