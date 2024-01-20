import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    Genre.objects.create(name="Western")
    genre_action = Genre.objects.create(name="Action")
    genre_drama = Genre.objects.create(name="Dramma")
    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")
    genre_drama.name = "Drama"
    genre_drama.save()
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu",
                                                    last_name="Reeves")
    genre_action.delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    queryset = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return queryset
