import sys
import os
import django
from django.core.management import call_command

sys.dont_write_bytecode = True
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

call_command("migrate", verbosity=0)
