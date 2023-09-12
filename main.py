import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genre_list = ["Western", "Action", "Dramma"]
    actor_first_name_list = ["George", "Kianu", "Scarlett", "Will",
                             "Jaden", "Scarlett"]
    actor_last_name_list = ["Klooney", "Reaves", "Keegan", "Smith",
                            "Smith", "Johansson"]
    # create
    for genre in genre_list:
        Genre.objects.create(name=genre)

    for actor in range(len(actor_first_name_list)):
        Actor.objects.create(
            first_name=actor_first_name_list[actor],
            last_name=actor_last_name_list[actor]
        )
    # update
    Genre.objects.filter(name="Dramma"
                         ).update(name="Drama")
    Actor.objects.filter(last_name="Klooney"
                         ).update(last_name="Clooney")
    Actor.objects.filter(last_name="Reaves"
                         ).update(first_name="Keanu", last_name="Reeves")
    # delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    # Return
    return (Actor.objects.filter(last_name="Smith"
                                 ).order_by("first_name"))
