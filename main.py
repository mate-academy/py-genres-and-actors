import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    Genre(name="Western").save()
    Genre(name="Action").save()
    Genre(name="Dramma").save()
    Actor(first_name="George", last_name="Klooney").save()
    Actor(first_name="Kianu", last_name="Reaves").save()
    Actor(first_name="Scarlett", last_name="Keegan").save()
    Actor(first_name="Will", last_name="Smith").save()
    Actor(first_name="Jaden", last_name="Smith").save()
    Actor(first_name="Scarlett", last_name="Johansson").save()

    drama = Genre.objects.get(name="Dramma")
    drama.name = "Drama"
    drama.save()

    Actor.objects.filter(first_name="George", last_name="Klooney").update(
        last_name="Clooney"
    )

    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        last_name="Reeves",
        first_name="Keanu"
    )

    Genre.objects.get(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
