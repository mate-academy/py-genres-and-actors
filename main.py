import init_django_orm  # noqa: F401

from db.models import Genre, Actor


def main():

    # CREATE

    new_genre1 = Genre.objects.create(
        name="Western",
    )
    new_genre2 = Genre.objects.create(
        name="Action",
    )
    new_genre3 = Genre.objects.create(
        name="Dramma",
    )

    new_actor1 = Actor.objects.create(
        first_name="George",
        last_name="Klooney",
    )
    new_actor2 = Actor.objects.create(
        first_name="Kianu",
        last_name="Reaves",
    )
    new_actor3 = Actor.objects.create(
        first_name="Scarlett",
        last_name="Keegan",
    )
    new_actor4 = Actor.objects.create(
        first_name="Will",
        last_name="Smith",
    )
    new_actor5 = Actor.objects.create(
        first_name="Jaden",
        last_name="Smith",
    )
    new_actor6 = Actor.objects.create(
        first_name="Scarlett",
        last_name="Johansson",
    )

    # UPDATE

    filtered_genre1 = Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")

    filtered_actor1 = Actor.objects.filter(
        last_name="Klooney",
    ).update(last_name="Clooney")
    filtered_actor2 = Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves",
    ).update(first_name="Keanu", last_name="Reeves")

    # DELETE

    Genre.objects.filter(
        name="Action",
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett",
    ).delete()

    # READ

    return_actors = Actor.objects.filter(
        last_name="Smith",
    ).order_by("first_name")
    print(return_actors)


if __name__ == "__main__":
    main()
