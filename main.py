import init_django_orm  # noqa: F401
import json

from django.db.models import QuerySet

from db.models import Genre
from db.models import Actor


def main() -> QuerySet:
    with open("file.json") as f:
        data = json.load(f)

    for item in data["genre"]:
        Genre.objects.create(
            name=item["name"]
        )

    for item in data["actors"]:
        Actor.objects.create(
            first_name=item["first_name"],
            last_name=item["last_name"]
        )

    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")
    Actor.objects.filter(
        last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(
        name="Action"
    ).delete()
    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    print(main())
    print(Genre.objects.all())
    print(Actor.objects.all())
