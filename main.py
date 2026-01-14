import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        Genre.objects.create(
            name=genre,
        )

    actors = [tuple("George Klooney".split(" ")),
              tuple("Kianu Reaves".split(" ")),
              tuple("Scarlett Keegan".split(" ")),
              tuple("Will Smith".split(" ")),
              tuple("Jaden Smith".split(" ")),
              tuple("Scarlett Johansson".split(" "))]

    for first_name, last_name in actors:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name,
        )

    Genre.objects.filter(
        name="Dramma").update(name="Drama")

    Actor.objects.filter(
        last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(
        last_name="Reaves").update(last_name="Reeves", first_name="Keanu")

    Genre.objects.filter(
        name="Action").delete()
    Actor.objects.filter(
        first_name="Scarlett").delete()

    result = Actor.objects.filter(
        last_name="Smith").order_by("first_name")

    return result
