import os
from django.conf import global_settings

DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'employee-feedback',
        'HOST': 'localhost',
        'PORT': 27017,
        'OPTIONS': {
            'OPERATIONS': {
                'save': {'w': 1}
            }
        }
    },
}

DEBUG = True

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'employeeFeedback'
)

STATIC_URL = '/static/'
ROOT_URLCONF = 'employeeFeedback.urls'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '5!9*nlhmhot^oy11a8h$72jc!n8g0hfp!ipg3-dhtwek0&d+@g'

# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
# )
#
# BASE_DIR = '/home/it/full_stack_dev_challenge/employeeFeedback/'
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'templates')],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
