import init_django_orm  # noqa: F401

from db.models import Actor, Genre


def main():
    Genre.objects.bulk_create([
        Genre(name="Western"),
        Genre(name="Action"),
        Genre(name="Dramma"),
    ])

    Actor.objects.bulk_create([
        Actor(first_name="George", last_name="Clooney"),
        Actor(first_name="Keanu", last_name="Reeves"),
        Actor(first_name="Scarlett", last_name="Keegan"),
        Actor(first_name="Will", last_name="Smith"),
        Actor(first_name="Jaden", last_name="Smith"),
        Actor(first_name="Scarlett", last_name="Johansson"),
    ])

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Klooney"
                         ).update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves"
                         ).update(first_name="Keanu",
                                  last_name="Reeves")
    actors_named_smith = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return actors_named_smith


if __name__ == "__main__":
    main()
