import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    # 1
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        Genre.objects.create(name=genre)
    first_names = [("George", "Klooney"),
                   ("Kianu", "Reaves"),
                   ("Scarlett", "Keegan"),
                   ("Will", "Smith"),
                   ("Jaden", "Smith"),
                   ("Scarlett", "Johansson")]
    for first_name, last_name in first_names:
        Actor.objects.create(first_name=first_name,
                             last_name=last_name
                             )
    # 2
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(id=2).update(first_name="Keanu", last_name="Reeves")
    # 3
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    # 4
    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
