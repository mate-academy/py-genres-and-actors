import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Actor, Genre
import sys

try:
    import cgi
except ImportError:
    import legacy as cgi
    sys.modules["cgi"] = cgi


def main() -> QuerySet:
    Genre.objects.get_or_create(name="Western")
    Genre.objects.get_or_create(name="Action")
    Genre.objects.get_or_create(name="Dramma")

    Actor.objects.get_or_create(first_name="George", last_name="Klooney")
    Actor.objects.get_or_create(first_name="Kianu", last_name="Reverse")
    Actor.objects.get_or_create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.get_or_create(first_name="Will", last_name="Smith")
    Actor.objects.get_or_create(first_name="Jaden", last_name="Smith")
    Actor.objects.get_or_create(first_name="Scarlett", last_name="Johansson")

    Genre.objects.filter(name="Dramma").update(name="Drama")
    (Actor.objects.filter(first_name="George", last_name="Klooney").
     update(last_name="Clooney"))
    (Actor.objects.filter(first_name="Kianu", last_name="Reverse")
     .update(first_name="Keanu", last_name="Reeves"))

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
