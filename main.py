import init_django_orm  # noqa: F401

from django.db.models import QuerySet


def main() -> QuerySet:
    Western = genre.objects.create(name="Western")
    Action = genre.objects.create(name="Action")
    Drama = genre.objects.create(name="Drama")

    George = Actor.objects.create(first_name="George", last_name="Klooney")
    Kianu = Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Scarlett = Actress.objects.create(first_name="Scarlett", last_name="Keegan")
    Will = Actor.objects.create(first_name="Will", last_name="Smith")
    Jaden = Actor.objects.create(first_name="Jaden", last_name="Smith")
    Scarlett = Actress.objects.create(first_name="Scarlett", last_name="Johansson")

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(last_name="Reeves")

    genre.objects.filter(name="Action").delete()
    Actress.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")

