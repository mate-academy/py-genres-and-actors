import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre

genres = ["Western", "Action", "Dramma"]
actors = [
    ("George", "Klooney"),
    ("Kianu", "Reaves"),
    ("Scarlett", "Keegan"),
    ("Will", "Smith"),
    ("Jaden", "Smith"),
    ("Scarlett", "Johansson")
]


def create_genres() -> None:
    for genre in genres:
        Genre.objects.create(name=genre)


def create_actors() -> None:
    for name, surname in actors:
        Actor.objects.create(
            first_name=name,
            last_name=surname
        )


def update_genres_and_actors() -> None:
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")


def delete_genres_and_actors() -> None:
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()


def main() -> QuerySet:
    create_genres()
    create_actors()
    update_genres_and_actors()
    delete_genres_and_actors()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    main()
