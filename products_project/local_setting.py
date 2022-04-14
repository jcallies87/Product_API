# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m^qykr&-w@_ucn3f^+%c8$_^h4vf_)_^(wgkl!=w&bt*_3j8(n'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Password3'
    }
}