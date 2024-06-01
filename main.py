import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Genre, Actor

genres = ["Western", "Action", "Dramma"]
actors = [
    {"first_name": "George", "last_name": "Klooney"},
    {"first_name": "Kianu", "last_name": "Reaves"},
    {"first_name": "Will", "last_name": "Smith"},
    {"first_name": "Jaden", "last_name": "Smith"},
    {"first_name": "Scarlett", "last_name": "Johansson"}
]


def main() -> QuerySet:
    for genre_name in genres:
        Genre.objects.create(name=genre_name)

    for actor in actors:
        Actor.objects.create(first_name=actor["first_name"],
                             last_name=actor["last_name"])

    genre_dramma = Genre.objects.get(name="Dramma")
    genre_dramma.name = "Drama"
    genre_dramma.save()

    actor_klooney = Actor.objects.get(first_name="George",
                                      last_name="Klooney")
    actor_klooney.last_name = "Clooney"
    actor_klooney.save()

    actor_reaves = Actor.objects.get(first_name="Kianu",
                                     last_name="Reaves")
    actor_reaves.first_name = "Keanu"
    actor_reaves.last_name = "Reeves"
    actor_reaves.save()

    Genre.objects.get(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    set_of_actors = (
        Actor.objects.filter(last_name="Smith").order_by("first_name")
    )
    return set_of_actors


if __name__ == "__main__":
    print(main())
