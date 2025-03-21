import init_django_orm  # noqa: F401

from django.db.models import QuerySet
import db.models as models


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        models.Genre.objects.create(name=genre)
    actors = [
        {"first_name": "George", "last_name": "Klooney"},
        {"first_name": "Kianu", "last_name": "Reaves"},
        {"first_name": "Scarlett", "last_name": "Keegan"},
        {"first_name": "Will", "last_name": "Smith"},
        {"first_name": "Jaden", "last_name": "Smith"},
        {"first_name": "Scarlett", "last_name": "Johansson"}
    ]
    for actor in actors:
        models.Actor.objects.create(**actor)

    models.Genre.objects.filter(name="Dramma").update(name="Drama")
    models.Actor.objects.filter(last_name="Klooney").update(
        last_name="Clooney"
    )
    models.Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves").update(
        first_name="Keanu",
        last_name="Reeves")
    models.Genre.objects.filter(name="Action").delete()
    models.Actor.objects.filter(first_name="Scarlett").delete()
    return models.Actor.objects.filter(
        last_name="Smith"
    ).all().order_by("first_name")

print(main())