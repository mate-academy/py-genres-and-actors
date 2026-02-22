import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor

genres = ["Western", "Action", "Dramma"]
actors = [
    "George Klooney",
    "Kianu Reaves",
    "Scarlett Keegan",
    "Will Smith",
    "Jaden Smith",
    "Scarlett Johansson"]


def main() -> QuerySet:
    for genre in genres:
        Genre.objects.create(name=genre)

    for actor in actors:
        first_name = actor.split()[0]
        last_name = actor.split()[-1]
        Actor.objects.create(last_name=last_name, first_name=first_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    (Actor.objects.filter(last_name="Reaves", first_name="Kianu")
     .update(last_name="Reeves", first_name="Keanu"))

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    main()
