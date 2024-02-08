import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:

    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        Genre.objects.create(name=genre, )

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_item, second_item in actors:
        Actor.objects.create(first_name=first_item, last_name=second_item, )

    Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama",)

    updates = [
        {"filter_criteria": {"last_name": "Klooney"}, "update_values": {"last_name": "Clooney"}},
        {"filter_criteria": {"first_name": "Kianu", "last_name": "Reaves"},
         "update_values": {"first_name": "Keanu", "last_name": "Reeves"}},
    ]
    for update in updates:
        filter_criteria = update["filter_criteria"]
        update_values = update["update_values"]
        Actor.objects.filter(**filter_criteria).update(**update_values)

    Genre.objects.filter(
        name="Action",
    ).delete()
    Actor.objects.filter(
        first_name="Scarlett",
    ).delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name").values()
