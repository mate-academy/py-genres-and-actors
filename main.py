import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre
from db.models import Actor


def main() -> QuerySet:
    genre_list = ["Western", "Action", "Dramma"]
    for genre in genre_list:
        Genre.objects.create(name=genre)
    actor_list = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for actor in actor_list:
        Actor.objects.create(first_name=actor[0], last_name=actor[1])
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu")
    Actor.objects.filter(last_name="Reaves").update(last_name="Reeves")
    Actor.objects.filter(first_name="Scarlett").delete()
    Genre.objects.filter(name="Action").delete()
    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    print(main())
