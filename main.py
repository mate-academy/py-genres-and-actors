import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ("Western", "Action", "Dramma")
    actors = (("George", "Klooney"), ("Kianu", "Reaves"),
              ("Scarlett", "Keegan"), ("Will", "Smith"),
              ("Jaden", "Smith"), ("Scarlett", "Johansson"))
    for genre in genres:
        Genre.objects.create(name=genre)
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    genres_to_update = (("Dramma", "Drama"), )
    actors_to_update = (
        (("George", "Klooney"), ("George", "Clooney")),
        (("Kianu", "Reaves"), ("Keanu", "Reeves"))
    )

    for old_genre, new_genre in genres_to_update:
        Genre.objects.filter(name=old_genre).update(name=new_genre)

    for old_actor, new_actor in actors_to_update:
        old_actor_first_name, old_actor_last_name = old_actor
        new_actor_first_name, new_actor_last_name = new_actor
        Actor.objects.filter(
            first_name=old_actor_first_name,
            last_name=old_actor_last_name
        ).update(
            first_name=new_actor_first_name,
            last_name=new_actor_last_name
        )

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
