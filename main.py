import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    # create
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")
    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # update
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    # delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # get
    actors_smith = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name").values()

    return actors_smith


if __name__ == "__main__":
    main()
