import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    genres = [
        "Western",
        "Action",
        "Drama"
    ]
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")

    ]

    # CREATE
    for genre in genres:
        Genre.objects.create(name=genre)

    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name,
                             last_name=last_name)

    # UPDATE
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu")
    Actor.objects.filter(last_name="Reaves").update(last_name="Reeves")

    # DELETE
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # RETURN
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
