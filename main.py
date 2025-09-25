import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    # CREATE (listas + loops)
    genres = ["Western", "Action", "Dramma"]
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for name in genres:
        Genre.objects.create(name=name)
    for first, last in actors:
        Actor.objects.create(first_name=first, last_name=last)

    # UPDATE (genres)
    Genre.objects.filter(name="Dramma").update(name="Drama")

    # UPDATE (actors)
    updates = {
        ("George", "Klooney"): {"last_name": "Clooney"},
        ("Kianu", "Reaves"): {"first_name": "Keanu", "last_name": "Reeves"},
    }
    for (first, last), fields in updates.items():
        Actor.objects.filter(first_name=first, last_name=last).update(**fields)

    # DELETE
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # RETURN
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
