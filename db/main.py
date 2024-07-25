import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    [
        Genre.objects.create(name=genre) for genre in
        [
            "Western",
            "Action",
            "Dramma",
        ]
    ]

    [
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name
        )
        for first_name, last_name in
        [
            ("George", "Clooney"),
            ("Keanu", "Reeves"),
            ("Scarlett", "Keegan"),
            ("Will", "Smith"),
            ("Jaden", "Smith"),
            ("Scarlett", "Johansson"),
        ]
    ]
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu").update(last_name="Reeves", first_name="Keanu"
                                   )
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    return Actor.objects.filter(last_name="Smith").all().order_by("first_name")


if __name__ == "__main__":
    main()
