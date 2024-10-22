import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor

genres = ["Western", "Action", "Dramma"]
actors = [("George", "Klooney"), ("Kianu", "Reaves"),
          ("Scarlett", "Keegan"), ("Will", "Smith"),
          ("Jaden", "Smith"), ("Scarlett", "Johansson")]


def main() -> QuerySet:

    # 1. Create
    for genre in genres:
        Genre.objects.create(name=genre)

    for item_first, item_second in actors:
        Actor.objects.create(
            first_name=item_first,
            last_name=item_second
        )

    # 2. Update
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )

    # 3. Delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # 4. Return
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
