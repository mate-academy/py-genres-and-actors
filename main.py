import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Action", "Western", "Dramma"]
    for genre_name in genres:
        Genre.objects.create(name=genre_name)

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

    genre_updates = [
        ({"name": "Dramma"}, {"name": "Drama"}),
    ]
    for filter_kwargs, update_kwargs in genre_updates:
        Genre.objects.filter(**filter_kwargs).update(**update_kwargs)

    actor_updates = [
        (
            {"first_name": "George", "last_name": "Klooney"},
            {"last_name": "Clooney"},
        ),
        (
            {"first_name": "Kianu", "last_name": "Reaves"},
            {"first_name": "Keanu", "last_name": "Reeves"},
        ),
    ]
    for filter_kwargs, update_kwargs in actor_updates:
        Actor.objects.filter(**filter_kwargs).update(**update_kwargs)

    genre_deletes = [{"name": "Action"}]
    for filter_kwargs in genre_deletes:
        Genre.objects.filter(**filter_kwargs).delete()

    actor_deletes = [{"first_name": "Scarlett"}]
    for filter_kwargs in actor_deletes:
        Actor.objects.filter(**filter_kwargs).delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
