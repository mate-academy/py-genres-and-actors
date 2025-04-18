import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor

def main() -> QuerySet:
    Western= Genre.objects.create(
        name="Western",
    )

    Action = Genre.objects.create(
        name="Action",
    )

    Dramma = Genre.objects.create(
        name="Dramma",
    )

    actor_1 = Actor.objects.create(
        first_name="George",
        last_name="Klooney",
    )

    actor_2 = Actor.objects.create(
        first_name="Kianu",
        last_name="Reaves",
    )

    actor_3 = Actor.objects.create(
        first_name="Scarlett",
        last_name="Keegan",
    )

    actor_4 = Actor.objects.create(
        first_name="Will",
        last_name="Smith",
    )

    actor_5 = Actor.objects.create(
        first_name="Jaden",
        last_name="Smith",
    )

    actor_6 = Actor.objects.create(
        first_name="Scarlett",
        last_name="Johansson",
    )

    Drama = Genre.objects.filter(name="Dramma").update(name="Drama")
    actor1_new = Actor.objects.filter(last_name="Klooney"
                                      ).update(last_name="Clooney")
    actor_2_new = Actor.objects.filter(first_name="Kianu",
                                       last_name="Reaves"
                                       ).update(first_name="Keanu",
                                                last_name="Reeves")

    Genre.objects.filter(
        name="Action"
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    Sorted_Actors = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
    print(Sorted_Actors)
    pass

