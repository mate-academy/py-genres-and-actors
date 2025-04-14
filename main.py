import init_django_orm  # noqa: F401


from db.models import Genre, Actor
from django.db.models import QuerySet


def main() -> QuerySet:
    # Create genres
    Genre.objects.create(mane="Western")
    Genre.objects.create(mane="Action")
    Genre.objects.create(mane="Dramma")
    # Create actors
    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")
    # Update genres and actors
    Genre.objects.filter(name="Dramma").update(name="Drama",)
    Actor.objects.filter(last_name="klooney").update(last_name="Clooney",)
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves",
    )
    # Delete genres and actors
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    main()
