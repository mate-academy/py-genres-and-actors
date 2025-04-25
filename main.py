import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    """Main function to perform CRUD operations on Genre and Actor models."""
    # 1. Create objects
    # Create genres
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    drama_genre = Genre.objects.create(name="Dramma")  # For later update

    # Create actors
    george = Actor.objects.create(first_name="George", last_name="Klooney")
    kianu = Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    scarlett_j = Actor.objects.create(
        first_name="Scarlett",
        last_name="Johansson"
    )

    # 2. Update objects
    # Update genre
    drama_genre.name = "Drama"
    drama_genre.save()

    # Update actors
    george.last_name = "Clooney"
    george.save()

    kianu.first_name = "Keanu"
    kianu.last_name = "Reeves"
    kianu.save()

    # 3. Delete objects
    # Delete genre
    Genre.objects.filter(name="Action").delete()

    # Delete actresses named "Scarlett"
    Actor.objects.filter(first_name="Scarlett").delete()

    # 4. Return QuerySet of Smith actors ordered by first_name
    return Actor.objects.filter(last_name="Smith").order_by('first_name')


if __name__ == "__main__":
    # Print results
    print("Actors with last name 'Smith':")
    print(main())

    print("\nAll genres:")
    print(Genre.objects.all())

    print("\nAll actors:")
    print(Actor.objects.all())
