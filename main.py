import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres: QuerySet[Genre] = Genre.objects
    actors: QuerySet[Actor] = Actor.objects

    genres.create(name="Western")
    genres.create(name="Action")
    genres.create(name="Dramma")

    actors.create(first_name="George", last_name="Klooney")
    actors.create(first_name="Kianu", last_name="Reaves")
    actors.create(first_name="Scarlett", last_name="Keegan")
    actors.create(first_name="Will", last_name="Smith")
    actors.create(first_name="Jaden", last_name="Smith")
    actors.create(first_name="Scarlett", last_name="Johansson")

    genres.filter(name="Dramma").update(name="Drama")
    actors.filter(last_name="Klooney").update(last_name="Clooney")
    actors.filter(last_name="Reaves").update(
        first_name="Keanu",
        last_name="Reeves"
    )

    genres.filter(name="Action").delete()
    actors.filter(first_name="Scarlett").delete()

    return actors.filter(last_name="Smith").order_by("first_name")
