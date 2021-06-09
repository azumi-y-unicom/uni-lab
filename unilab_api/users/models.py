from django.db import models
from django.forms.models import model_to_dict

# Usersモデル
class Users(models.Model):
    class Meta:
        # DBで使用するテーブル名
        db_table = 'Users'
        # オブジェクトリスト取得時のソート順（idを昇順）
        ordering = ['id']
        # テーブルのコメント
        verbose_name = 'ユーザー情報'
    # カラム定義
    id = models.AutoField(verbose_name='ID', primary_key=True)
    userid = models.CharField(verbose_name='ログインID', max_length=50)
    password = models.CharField(verbose_name='パスワード', max_length=255)
    name = models.TextField(verbose_name='表示ユーザ名' )
    mail = models.CharField(verbose_name='メールアドレス', max_length=255)
    auth = models.CharField(verbose_name='権限', max_length=1)
    status = models.CharField(verbose_name='アカウントステータス', max_length=1)
    create_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.userid
