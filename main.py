import init_django_orm  # noqa: F401

from django.db.models import QuerySet
<<<<<<< HEAD

from db.models import Genre, Actor


def main() -> QuerySet:
    Genre.objects.create(
        name="Western",
    )

    Genre.objects.create(
        name="Action",
    )

    Genre.objects.create(
        name="Dramma",
    )

    Actor.objects.create(
=======
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
>>>>>>> 57befa0720dca382dfa44d8d654b2b9523dbfbc0
        first_name="George",
        last_name="Klooney",
    )

<<<<<<< HEAD
    Actor.objects.create(
=======
    actor_2 = Actor.objects.create(
>>>>>>> 57befa0720dca382dfa44d8d654b2b9523dbfbc0
        first_name="Kianu",
        last_name="Reaves",
    )

<<<<<<< HEAD
    Actor.objects.create(
=======
    actor_3 = Actor.objects.create(
>>>>>>> 57befa0720dca382dfa44d8d654b2b9523dbfbc0
        first_name="Scarlett",
        last_name="Keegan",
    )

<<<<<<< HEAD
    Actor.objects.create(
=======
    actor_4 = Actor.objects.create(
>>>>>>> 57befa0720dca382dfa44d8d654b2b9523dbfbc0
        first_name="Will",
        last_name="Smith",
    )

<<<<<<< HEAD
    Actor.objects.create(
=======
    actor_5 = Actor.objects.create(
>>>>>>> 57befa0720dca382dfa44d8d654b2b9523dbfbc0
        first_name="Jaden",
        last_name="Smith",
    )

<<<<<<< HEAD
    Actor.objects.create(
=======
    actor_6 = Actor.objects.create(
>>>>>>> 57befa0720dca382dfa44d8d654b2b9523dbfbc0
        first_name="Scarlett",
        last_name="Johansson",
    )

<<<<<<< HEAD
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney"
                         ).update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu",
                         last_name="Reaves"
                         ).update(first_name="Keanu",
                                  last_name="Reeves")
=======
    Drama = Genre.objects.filter(name="Dramma").update(name="Drama")
    actor1_new = Actor.objects.filter(last_name="Klooney"
                                      ).update(last_name="Clooney")
    actor_2_new = Actor.objects.filter(first_name="Kianu",
                                       last_name="Reaves"
                                       ).update(first_name="Keanu",
                                                last_name="Reeves")
>>>>>>> 57befa0720dca382dfa44d8d654b2b9523dbfbc0

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
<<<<<<< HEAD


if __name__ == "__main__":
    main()
=======
    pass

>>>>>>> 57befa0720dca382dfa44d8d654b2b9523dbfbc0
