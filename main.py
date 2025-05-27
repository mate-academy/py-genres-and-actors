import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor

genres = [
        "Western",
        "Action",
        "Dramma"
    ]
actors = [
    "George Klooney",
    "Kianu Reaves",
    "Scarlett Keegan",
    "Will Smith",
    "Jaden Smith",
    "Scarlett Johansson"]


def main() -> QuerySet:
    for genre in genres:
        Genre.objects.create(genre=genre)

    for actor in actors:
        Actor.objects.create(actor=actor)

    Genre.objects.filter(genre="Dramma").update(genre="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    (Actor.objects.filter(last_name="Reaves", first_name="Kianu")
     .update(last_name="Reeves", first_name="Keanu"))

    Genre.objects.filter(genre="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == '__main__':
    main()
