import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genre_names = ["Western",
                   "Action",
                   "Drama"]
    actor_data = [("George", "Klooney"),
                  ("Kianu", "Reaves"),
                  ("Scarlett", "Keegan"),
                  ("Will", "Smith"),
                  ("Jaden", "Smith"),
                  ("Scarlett", "Johansson")]

    Genre.objects.bulk_create(
        [Genre(name=name) for name in genre_names]
    )

    Actor.objects.bulk_create(
        [Actor(first_name=first_name, last_name=last_name)
         for first_name, last_name in actor_data]
    )

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu",
        last_name="Reeves"
    )
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
