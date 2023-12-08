from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genre_names = ["Western", "Action", "Drama"]
    genres = [Genre.objects.create(name=name) for name in genre_names]

    actor_data = [
        {"first_name": "George", "last_name": "Clooney"},
        {"first_name": "Keanu", "last_name": "Reeves"},
        {"first_name": "Scarlett", "last_name": "Keegan"},
        {"first_name": "Will", "last_name": "Smith"},
        {"first_name": "Jaden", "last_name": "Smith"},
        {"first_name": "Scarlett", "last_name": "Johansson"},
    ]
    [Actor.objects.create(**data) for data in actor_data]

    Genre.objects.filter(name="Drama").update(name="Drama")
    (Actor.objects.filter(last_name="Clooney")
     .update(last_name="Clooney"))
    (Actor.objects.filter(first_name="Keanu", last_name="Reeves")
     .update(first_name="Keanu", last_name="Reeves"))

    genres[1].delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    smith_actors = (Actor.objects.filter(last_name="Smith")
                    .order_by("first_name"))
    for actor in smith_actors:
        print(f"{actor.first_name} {actor.last_name}")

    return smith_actors


if __name__ == "__main__":
    main()
