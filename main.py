import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    def create_genre() -> None:
        genre_names = ["Western", "Action", "Dramma"]
        for i in genre_names:
            Genre.objects.create(
                name=i
            )

    def create_actors() -> None:
        actors = [("George", "Klooney"),
                  ("Kianu", "Reaves"),
                  ("Scarlett", "Keegan"),
                  ("Will", "Smith"),
                  ("Jaden", "Smith"),
                  ("Scarlett", "Johansson")]
        for first_name, last_name in actors:
            Actor.objects.create(
                first_name=first_name,
                last_name=last_name
            )

    def update_genre() -> None:
        Genre.objects.filter(
            name="Dramma"
        ).update(name="Drama")

    def update_actors() -> None:
        Actor.objects.filter(
            first_name="George",
            last_name="Klooney"
        ).update(last_name="Clooney")

        Actor.objects.filter(
            first_name="Kianu",
            last_name="Reaves"
        ).update(first_name="Keanu", last_name="Reeves")

    def delete_genre() -> None:
        Genre.objects.filter(
            name="Action"
        ).delete()

    def delete_actors() -> None:
        Actor.objects.filter(
            first_name="Scarlett",
        ).delete()

    create_genre()
    create_actors()
    update_genre()
    update_actors()
    delete_genre()
    delete_actors()

    total = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")

    return total


if __name__ == "__main__":
    main()
