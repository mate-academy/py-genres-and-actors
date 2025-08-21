# main.py
from db.models import Genre, Actor
from django.db.models.query import QuerySet


def main() -> QuerySet[Actor]:
    """Create, update, delete records and return actors
    with last name 'Smith'."""
    # CREATE genres
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    dramma = Genre.objects.create(name="Dramma")

    # CREATE actors
    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # UPDATE records
    dramma.name = "Drama"
    dramma.save()

    george = Actor.objects.get(first_name="George", last_name="Klooney")
    george.last_name = "Clooney"
    george.save()

    kianu = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    kianu.first_name = "Keanu"
    kianu.last_name = "Reeves"
    kianu.save()

    # DELETE records
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # RETURN QuerySet
    smith_actors = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
    return smith_actors


if __name__ == "__main__":
    actors = main()
    print("Actors with last name 'Smith':")
    for actor in actors:
        print(
            f"{actor.first_name} "
            f"{actor.last_name}"
        )
