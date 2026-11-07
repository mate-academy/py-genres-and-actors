from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    genres = [
        ("Western",),
        ("Action",),
        ("Dramma",),
    ]
    for (name,) in genres:
        Genre.objects.create(name=name)

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    genre_drama = Genre.objects.get(name="Dramma")
    genre_drama.name = "Drama"
    genre_drama.save()

    actor_george = Actor.objects.get(
        first_name="George", last_name="Klooney"
    )
    actor_george.last_name = "Clooney"
    actor_george.save()

    actor_keanu = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    actor_keanu.first_name = "Keanu"
    actor_keanu.last_name = "Reeves"
    actor_keanu.save()

    Genre.objects.get(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
