import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    create_genre = [
        "Western",
        "Action",
        "Dramma"
    ]

    for name in create_genre:
        Genre.objects.create(
            name=name
        )

    create_actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    checklist = [
        {"field": "first_name", "index": 0},
        {"field": "last_name", "index": 1}
    ]

    for data in create_actors:
        actor_data = {item["field"]: data[item["index"]] for item in checklist}
        Actor.objects.create(**actor_data)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(
        first_name="Keanu", last_name="Reeves"
    )

    Genre.objects.filter(
        name="Action"
    ).delete()
    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
