import init_django_orm # noqa: F401

from django.db.models import QuerySet, IntegerField, Case, When
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Drama"]
    for genre in genres:
        Genre.objects.create(name=genre)

    actors = [
        ("George", "Clooney"),
        ("Keanu", "Reeves"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
    ]

    for first_name, last_name in actors:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name
        )


    return Actor.objects.filter(
        first_name__in=["Jaden", "Will"],
        last_name="Smith"
    ).order_by(
        Case(
            When(first_name="Jaden", then=0),
            When(first_name="Will", then=1),
            output_field=IntegerField(),
        )
    )

