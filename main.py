from django.db.models.query import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet[Actor]:
    genres = ["Western", "Action", "Dramma"]
    for name in genres:
        Genre.objects.get_or_create(name=name)

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first, last in actors:
        Actor.objects.get_or_create(first_name=first, last_name=last)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu",
        last_name="Reeves"
    )

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    queryset: QuerySet[Actor] = (
        Actor.objects.filter(last_name="Smith").order_by("first_name")
    )
    return queryset
