from pathlib import Path

# TODO：JWT_AUTH用
import datetime


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = '$!k3iy$#%)o2rg^%hm9e-alws09!0+n_^(eicg6gi%*vk$e=4b'
# DEBUG = False
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'lab.apps.LabConfig', 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders', # CORS対策追加
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # CORS対策追加
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'unilab_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'unilab_api.wsgi.application'


# Database
# postgresSQLを指定
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'unilab_db',
        'USER': 'unilab',
        'PASSWORD': 'unilab',
        'HOST': 'localhost',
        'PORT': '15432',
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

# 日本語・日本時間
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# TODO JWTを使用する
REST_FRAMEWORK = {
#    'DEFAULT_PERMISSION_CLASSES': (
#        'rest_framework.permissions.IsAuthenticated',
#    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
#        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DATETIME_FORMAT': "%Y/%m/%d %H:%M:%S",
    'PAGE_SIZE': 10
}
# JWT認証機能
#JWT_AUTH = {
#    'JWT_SECRET_KEY': SECRET_KEY,
#    'JWT_ALGORITHM': 'HS256',                                       # 暗号化アルゴリズム
#    'JWT_ALLOW_REFRESH': True,                                      # トークン更新　有効
#    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),             # リフレッシュした際のトークン期限　1日
#    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=28),    # リフレッシュしても切れる最大のトークン期限　28日
#}


# CORS対策 フロントエンド側のURLを指定
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
]
CORS_ALLOW_CREDENTIALS = True

