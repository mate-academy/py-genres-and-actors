import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    # create
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        print(Genre.objects.create(
            name=genre
        ))
    actors = [{"George": "Klooney"},
              {"Kianu": "Reaves"},
              {"Scarlett": "Keegan"},
              {"Will": "Smith"},
              {"Jaden": "Smith"},
              {"Scarlett": "Johansson"}]
    for actor in actors:
        for first_name, last_name in actor.items():
            print(Actor.objects.create(
                first_name=first_name,
                last_name=last_name
            ))
    # update
    print(Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama"))
    print(Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(
        last_name="Clooney"
    ))
    print(Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"))
    # delete
    print(Genre.objects.filter(
        name="Action"
    ).delete())
    print(Actor.objects.filter(
        first_name="Scarlett"
    ).delete())
    return Actor.objects.filter(
        last_name="Smith"
    ).order_by(
        "first_name"
    )


if __name__ == "__main__":
    main()
