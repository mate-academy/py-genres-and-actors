import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    # Creating genres:
    for genre in ("Western", "Action", "Dramma"):
        Genre.objects.create(name=genre)

    # Creating actors:
    for actor_name, actor_surname in (
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ):
        Actor.objects.create(first_name=actor_name, last_name=actor_surname)

    # Updating
    Genre.objects.get(name="Dramma").name = "Drama"
    Actor.objects.get(
        first_name="George", last_name="Klooney"
    ).last_name = "Clooney"
    keanu_reeves = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    keanu_reeves.first_name = "Keanu"
    keanu_reeves.last_name = "Reeves"

    # Deletions
    Genre.objects.get(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
