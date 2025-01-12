from django.db.models import QuerySet
import init_django_orm  # noqa: F401

from db.models import Genre, Actor


def main() -> QuerySet:
    # Ensure data is created only if it doesn't exist
    Genre.objects.get_or_create(name="Western")
    Genre.objects.get_or_create(name="Action")
    Genre.objects.get_or_create(name="Dramma")

    Actor.objects.get_or_create(
        first_name="George", last_name="Klooney")
    Actor.objects.get_or_create(
        first_name="Kianu", last_name="Reaves")
    Actor.objects.get_or_create(
        first_name="Scarlett", last_name="Keegan")
    Actor.objects.get_or_create(
        first_name="Will", last_name="Smith")
    Actor.objects.get_or_create(
        first_name="Jaden", last_name="Smith")
    Actor.objects.get_or_create(
        first_name="Scarlett", last_name="Johansson")

    # Update records
    Genre.objects.filter(name="Dramma").update(
        name="Drama")
    Actor.objects.filter(last_name="Klooney").update(
        last_name="Clooney")
    Actor.objects.filter(first_name="Kianu",
                         last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )

    # Delete records
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # Return QuerySet with last_name "Smith", ordered by name
    return Actor.objects.filter(
        last_name="Smith").order_by("first_name")

# print(Genre.objects.all())
# print(Actor.objects.all())
