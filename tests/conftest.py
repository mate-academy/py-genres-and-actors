import django
from django.conf import settings

def pytest_configure():
    if not settings.configured:
        settings.configure(
            DEBUG=True,
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': ':memory:',
                }
            },
            INSTALLED_APPS=[
                'django.contrib.contenttypes',
                'django.contrib.auth',
                'db',
            ],
        )
        django.setup()
        from django.core.management import call_command
        call_command('migrate', verbosity=0)
