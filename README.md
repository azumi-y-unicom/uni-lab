# uni-lab

## 開発環境
### 基本環境  
* Python 3.8.2  
* postgres:13.2  
* Node.js 14.16.0  

その他ライブラリは`.\requirements.txt`と`.\unilab_frontend\package.json`を参照  

<br>

### DB環境について
下記の手順で構築する。  

1. PostgreSQL 13.2のイメージを公式から取得する
```
docker pull postgres:13.2
```

2. コンテナを作成する  
```
cd .\docker\
docker-compose -f docker-compose.yml up
```

3. テーブル作成（マイグレーション）  
以下のコマンドからDjangoの機能を用いてテーブルを作成する
```
cd .\unilab_api\ 
python manage.py makemigrations
python manage.py migrate
```

※ ポート変更する場合  
下記をそれぞれ変更する  

`.\docker\docker-compose.yml`
```
services:
  db:
・・・
    ports:
      - "15432:5432"
・・・
```

`.\unilab_api\unilab_api\settings.py`
```
DATABASES = {
	'default': {
	・・・
		'PORT': '15432',
    }
}
```
