import init_django_orm  # noqa: F401
from db.models import Genre, Actor


def main():

    list_of_genres = [
        "Western",
        "Action",
        "Dramma"
    ]
    list_of_actors = [
        "George Klooney",
        "Kianu Reaves",
        "Scarlett Keegan",
        "Will Smith",
        "Jaden Smith",
        "Scarlett Johansson"
    ]

    for genre in list_of_genres:
        Genre.objects.create(name=genre)
    for actor in list_of_actors:
        first_name, last_name = actor.split()
        Actor.objects.create(first_name=first_name, last_name=last_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by('first_name')


if __name__ == "__main__":
    main()
