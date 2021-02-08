"""
Django settings for auto_cmdb project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os,sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#xadmin
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-1$_bb6qjx*@=jh0ff)pbwm972+zhhr*%7yi!!2)y76uj4i)fu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'api',
    'cmdb',
    # DRF 需要加载的应用,需要先安装 pip3 install djangorestframework
    'rest_framework',
    'xadmin.apps.XAdminConfig', 
    'crispy_forms',
    'pure_pagination',
    "octoups",
    'django_celery_results',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'auto_cmdb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'auto_cmdb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'


STATIC_ROOT= os.path.join(BASE_DIR,"allstatic")

STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'static'),  # 最后有英文的逗号
]
AUTH_USER_MODEL = 'users.UsersProfile'


from django.urls import reverse_lazy
# 用户登录成功后跳转的 URL
LOGIN_REDIRECT_URL = "/"

# 用户登录 GET 请求的 URL和登录验证失败后跳转到的 URL
LOGIN_URL = reverse_lazy('users:login')

# # 自定义登录验证类
# AUTHENTICATION_BACKENDS = (
#     'users.users_auth.CustomBackend',  # 注意后面的逗号
# )


MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

PAGINATION_SETTINGS = { 
    'PAGE_RANGE_DISPLAYED': 10, 
    'MARGIN_PAGES_DISPLAYED': 2, 
    'SHOW_FIRST_PAGE_WHEN_INVALID': True, 
    }


INVENT_PATH=os.path.join(BASE_DIR,"octoups/inventory/hosts")

#celery中间人
CELERY_BROKER_URL="amqp://alice:alice@rabbitmq:5672/v_host1" 
# backend后端存储
CELERY_RESULT_BACKEND="redis://redis:6379/1"  

# 执行任务的并发工作进程/线程/绿色线程的数量。
# 如果您主要执行I / O，则可以有更多的进程，
# 但如果主要是CPU约束，请尝试使其与计算机上的CPU数量保持接近。
# 如果未设置，将使用主机上的CPU /内核数。
CELERY_WORKER_CONCURRENCY	 = 6


# 延迟确认 意味着任务消息将在任务执行后得到确认
CELERY_TASK_ACKS_LATE = True

# 每个 worker 最多执行 60 个任务就自动销毁，防止内存泄露
CELERY_WORKER_MAX_TASKS_PER_CHILD = 20

# 单个任务的硬时间限制（秒）。
# 超过此值时，处理任务的工作进程将被终止并替换为新的工作进程。
CELERY_TASk_TIME_LIMIT = 5 * 60