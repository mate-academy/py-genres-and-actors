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
    drama = Genre.objects.get(name="Dramma")
    drama.name = "Drama"
    drama.save()

    george_clooney = Actor.objects.get(
        first_name="George", last_name="Klooney"
    )
    george_clooney.last_name = "Clooney"
    george_clooney.save()

    keanu_reeves = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    keanu_reeves.first_name = "Keanu"
    keanu_reeves.last_name = "Reeves"
    keanu_reeves.save()

    # Deletions
    Genre.objects.get(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
