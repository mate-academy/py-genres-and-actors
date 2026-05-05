import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = [("Western",), ("Action",), ("Dramma",)]
    actor_list = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")]
    for (name,) in genres:
        Genre.objects.create(name=name)

    for first_name, last_name in actor_list:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    updates = [
        ({"first_name": "George", "last_name": "Klooney"},
         {"last_name": "Clooney"}),
        ({"first_name": "Kianu", "last_name": "Reaves"},
         {"first_name": "Keanu", "last_name": "Reeves"}),
    ]
    for filters, new_value in updates:
        Actor.objects.filter(**filters).update(**new_value)

    Genre.objects.filter(name="Dramma").update(name="Drama")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
