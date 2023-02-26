from .settings_common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-4dfh)1_mr0q*2f#i%*sjfy4#-6smg*0$c%c3!4oo$&p8^y7=4k"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#ロギング設定
LOGGING={
    'version':1,
    'disable_existing_loggers':False,

    #ロガーの設定
    'loggers':{
        #Djangoが使用するロガー
        'django': {
            'handlers':['console'],
            'level':'INFO',
        },
        #diaryアプリケーションが使用するロガー
        'input':{
            'handlers':['console'],
            'level':'DEBUG',
        },
    },

    #ハンドラの設定
    'handlers':{
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'dev'
        },
    },

    #フォーマッタの設定
    'formatters':{
        'dev':{
            'format':'\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'