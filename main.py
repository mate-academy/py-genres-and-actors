import init_django_orm  # noqa: F401

from db.models import Actor, Genre


def main():
    # create
    genres_create = ["Western", "Action", "Dramma"]

    for genre in genres_create:
        Genre.objects.create(name=genre)

    actors_create = [
        ["George", "Klooney"],
        ["Kianu", "Reaves"],
        ["Scarlett", "Keegan"],
        ["Will", "Smith"],
        ["Jaden", "Smith"],
        ["Scarlett", "Johansson"]
    ]

    for actor in actors_create:
        Actor.objects.create(first_name=actor[0], last_name=actor[1])

    # update
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu", last_name="Reeves"
    )
    # delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
