import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre
from db.models import Actor


genres = ["Western", "Action", "Dramma"]
actors = [("George", "Klooney"), ("Kianu", "Reaves"), ("Scarlett", "Keegan"),
          ("Will", "Smith"), ("Jaden", "Smith"), ("Scarlett", "Johansson")]
def main() -> QuerySet:
    for genre in genres:
        Genre.objects.create(name=genre)
    for name, last_name in actors:
        Actor.objects.create(first_name=name, last_name=last_name)
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    (Actor.objects.filter(first_name="Kianu").
     update(first_name="Keanu", last_name="Reeves"))
    Actor.objects.filter(first_name="Scarlett").delete()
    Genre.objects.filter(name="Action").delete()
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
