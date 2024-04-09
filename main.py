import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    genres_list = ["Western", "Action", "Drama"]
    actors_list = [("George", "Klooney",
                    "Kianu", "Reaves",
                    "Scarlet", "Keegan",
                    "Will", "Smith",
                    "Jaden", "Smith",
                    "Scarlet", "Johansson")]
    for genre in genres_list:
        Genre.objects.create(name=genre)

    for actor_name, actor_last_name in actors_list:
        Actor.objects.create(name=actor_name, last_name=actor_last_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney"
                         ).update(
        last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves"
                         ).update(
        first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlet").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
