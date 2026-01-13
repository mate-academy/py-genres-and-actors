import init_django_orm    # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    future_genres = ["Western", "Action", "Dramma"]
    future_actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for genre in future_genres:
        Genre.objects.create(name=genre)

    for first_name, last_name in future_actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")

    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")

    Actor.objects.filter(last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    actor_query_set = (
        Actor.objects.filter(last_name="Smith").order_by("first_name")
    )
    return actor_query_set
