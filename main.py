from django.db.models.query import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet[Actor]:
    """Create, update, delete records and return actors
    with last name 'Smith'."""

    # CREATE genres
    genres = ["Western", "Action", "Dramma"]
    created_genres = [Genre.objects.create(name=name) for name in genres]

    # CREATE actors
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    created_actors = [Actor.objects.create(first_name=f, last_name=l) for f, l in actors]

    # UPDATE records
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Klooney").update(
        last_name="Clooney"
    )
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )

    # DELETE records
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # RETURN QuerySet
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
