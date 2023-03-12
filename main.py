import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def add_genres() -> None:
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Drama")


def add_actors() -> None:
    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")


def update_drama_genre() -> None:
    try:
        drama_genre = Genre.objects.get(name="Drama")
    except Genre.DoesNotExist:
        drama_genre = Genre(name="Drama")
        drama_genre.save()


def update_klooney_actor() -> None:
    Actor.objects.filter(
        last_name="Klooney"
    ).update(last_name="Clooney")


def update_reaves_actor() -> None:
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")


def delete_action_genre() -> None:
    action_genre = Genre.objects.get(name="Action")
    action_genre.delete()


def delete_scarlett_actors() -> None:
    actresses = Actor.objects.filter(first_name="Scarlett")
    actresses.delete()


def get_smith_actors() -> QuerySet[Actor]:
    actors = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return actors


def main() -> QuerySet[Actor]:
    add_genres()
    add_actors()

    update_drama_genre()
    update_klooney_actor()
    update_reaves_actor()

    delete_action_genre()
    delete_scarlett_actors()

    return get_smith_actors()


if __name__ == "__main__":
    print(main())
    print(Genre.objects.all())
    print(Actor.objects.all())
