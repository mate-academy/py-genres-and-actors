from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet[Actor]:
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for element in ["Western", "Action", "Dramma"]:
        Genre.objects.create(name=element)

    for actor in actors:
        Actor.objects.create(first_name=actor[0], last_name=actor[1])

    genre_to_update = Genre.objects.get(name="Dramma")
    genre_to_update.name = "Drama"
    genre_to_update.save()

    actor_update = Actor.objects.get(first_name="George", last_name="Klooney")
    actor_update.last_name = "Clooney"
    actor_update.save()

    actor_to_update = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    actor_to_update.first_name = "Keanu"
    actor_to_update.last_name = "Reeves"
    actor_to_update.save()

    genre_to_delete = Genre.objects.get(name="Action")
    genre_to_delete.delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
