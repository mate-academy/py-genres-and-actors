from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet[Actor, Actor]:
    genres = [
        ("Western",),
        ("Action",),
        ("Dramma",),
    ]

    for genre, in genres:
        Genre.objects.create(name=genre)

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for first_name, last_name in actors:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name,
        )

    genre_updates = [
        ("Dramma", "Drama"),
    ]

    for old_name, new_name in genre_updates:
        Genre.objects.filter(name=old_name).update(name=new_name)

    actor_updates = [
        ("George", "Klooney", "George", "Clooney"),
        ("Kianu", "Reaves", "Keanu", "Reeves"),
    ]

    for (old_first_name, old_last_name,
         new_first_name, new_last_name) in actor_updates:
        Actor.objects.filter(
            first_name=old_first_name,
            last_name=old_last_name,
        ).update(
            first_name=new_first_name,
            last_name=new_last_name,
        )

    Genre.objects.filter(name="Action").delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
