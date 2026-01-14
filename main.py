import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [("George", "Klooney"), ("Kianu", "Reaves"),
              ("Scarlett", "Keegan"), ("Will", "Smith"),
              ("Jaden", "Smith"), ("Scarlett", "Johansson")]

    # Create items
    for genre in genres:
        Genre.objects.create(name=genre)

    for first, last in actors:
        Actor.objects.create(first_name=first, last_name=last)

    # Update items
    drama = Genre.objects.get(name="Dramma")
    drama.name = "Drama"
    drama.save()

    george = Actor.objects.get(first_name="George", last_name="Klooney")
    george.last_name = "Clooney"
    george.save()

    kianu = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    kianu.first_name = "Keanu"
    kianu.last_name = "Reeves"
    kianu.save()

    # Delete items
    Genre.objects.get(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # Return items
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
