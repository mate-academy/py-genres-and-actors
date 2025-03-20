import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Drama"]
    actors = [
        ["George", "Klooney"],
        ["Kianu", "Reaves"],
        ["Scarlett", "Keegan"],
        ["Will", "Smith"],
        ["Jaden", "Smith"],
        ["Scarlett", "Johansson"]
    ]
    genres_to_update = {"Dramma": "Drama"}
    actors_to_update = [
        ["George Klooney", "George Clooney"],
        ["Kianu Reaves", "Keanu Reeves"]
    ]
    genres_to_delete = ["Action"]
    actors_to_delete = ["Scarlett"]
    to_return = "Smith"

    # CREATE
    for genre in genres:
        Genre.objects.create(name=genre)
        print(genre, "created!")

    for actor in actors:
        Actor.objects.create(first_name=actor[0], last_name=actor[1])
        print(actor, "created!")

    # UPDATE
    for key, value in genres_to_update.items():
        Genre.objects.filter(name=key).update(name=value)
        print(key, "updated!", "It stated to ", value)

    for actor in actors_to_update:
        current_name = actor[0].split()
        new_name = actor[1].split()
        Actor.objects.filter(
            first_name=current_name[0],
            last_name=current_name[1]
        ).update(
            first_name=new_name[0],
            last_name=new_name[1]
        )
        print(actor[0], "updated!", "new name is ", new_name)

    # DELETE
    for genre in genres_to_delete:
        Genre.objects.filter(name=genre).delete()
        print(genre, "deleted!")

    for actor in actors_to_delete:
        Actor.objects.filter(first_name=actor).delete()
        print(actor, "deleted!")

    query_set = Actor.objects.filter(
        last_name=to_return
    ).order_by("first_name")
    return query_set


if __name__ == "__main__":
    print(main())
