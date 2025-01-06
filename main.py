import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre

items = [
    ("George", "Klooney"),
    ("Kianu", "Reaves"),
    ("Scarlett", "Keegan"),
    ("Will", "Smith"),
    ("Jaden", "Smith"),
    ("Scarlett", "Johansson")
]


def main() -> QuerySet:
    for item_first, item_second in items:
        Actor.objects.create(
            first_name=item_first,
            last_name=item_second
        )

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu")
    Actor.objects.filter(last_name="Reaves").update(last_name="Reeves")
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    smiths = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return smiths

    # print(Genre.objects.all().delete())
    # print(Actor.objects.all().delete())
