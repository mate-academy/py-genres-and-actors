import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres_list = ["Western", "Action", "Dramma"]
    actors = [("George", "Klooney"), ("Kianu", "Reaves"),
              ("Scarlett", "Keegan"), ("Will", "Smith"),
              ("Jaden", "Smith"), ("Scarlett", "Johansson")]

    for genre in genres_list:
        Genre.objects.create(
            name=genre
        )

    for actor in actors:
        first_name, last_name = actor
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name
        )
    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")

    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(
        name="Action"
    ).delete()

    final_return = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")

    return final_return


print(main())

print(Genre.objects.all())

print(Actor.objects.all())
