import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
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

    updates = [
        ("Dramma", "Drama", "Genre"),
        ("Klooney", "Clooney", "Actor"),
        ("Kianu", "Keanu", "Actor"),
        ("Reaves", "Reeves", "Actor"),
    ]
    for old_value, new_value, model in updates:
        if model == "Genre":
            Genre.objects.filter(name=old_value).update(name=new_value)
        else:
            Actor.objects.filter(first_name=old_value).update(
                first_name=new_value
            )
            Actor.objects.filter(last_name=old_value).update(
                last_name=new_value
            )

    deletions = [
        ("Action", "Genre"),
        ("Scarlett", "Actor"),
    ]
    for value, model in deletions:
        if model == "Genre":
            Genre.objects.filter(name=value).delete()
        else:
            Actor.objects.filter(first_name=value).delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
