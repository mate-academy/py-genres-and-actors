import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    for value in ["Western", "Action", "Dramma"]:
        Genre.objects.create(name=value)

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for first_n, last_n in actors:
        Actor.objects.create(first_name=first_n, last_name=last_n)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )

    Genre.objects.get(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    smith_set = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return smith_set
