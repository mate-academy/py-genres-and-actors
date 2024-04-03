import init_django_orm  # noqa: F401
from db.models import Genre, Actor
from django.db.models import QuerySet


def main() -> QuerySet:
    pass
    for genre in ("Western", "Action", "Dramma"):
        Genre.objects.create(name=genre)

    for actor in (
            "George Klooney",
            "Kianu Reaves",
            "Scarlett Keegan",
            "Will Smith",
            "Jaden Smith",
            "Scarlett Johansson"
    ):
        Actor.objects.create(
            first_name=actor.split()[0],
            last_name=actor.split()[1],)

    Genre.objects.filter(name="Drama").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Clooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by('first_name')


if __name__ == "__main__":
    print(main())
    print(Genre.objects.all())
    print(Actor.objects.all())


def main() -> QuerySet:
    pass
    genres_list = ["Western", "Action", "Dramma"]
    actors_list = [("George", "Klooney"),
                   ("Kianu", "Reaves"),
                   ("Scarlett", "Keegan"),
                   ("Will", "Smith"),
                   ("Jaden", "Smith"),
                   ("Scarlett", "Johansson")]
    for genre in genres_list:
        Genre.objects.create(name=genre)
    for actor_name, actor_last_name in actors_list:
        Actor.objects.create(first_name=actor_name, last_name=actor_last_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
