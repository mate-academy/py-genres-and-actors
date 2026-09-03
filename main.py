import init_django_orm  # noqa: F401


from django.db.models import QuerySet


def main() -> QuerySet:

    genres = ["Western", "Action", "Dramma"]

    cast = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
        ]

    for genre in genres:
        Genre.objects.create(name=genre)

    for name, last_name in cast:
        Actor.objects.create(
            first_name=name,
            last_name=last_name
            )
