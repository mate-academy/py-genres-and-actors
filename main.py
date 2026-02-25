import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor

genres = ["Western", "Action", "Dramma"]
actors = [("George", "Klooney"),
          ("Kianu", "Reaves"),
          ("Scarlett", "Keegan"),
          ("Will", "Smith"),
          ("Jaden", "Smith"),
          ("Scarlett", "Johansson")
          ]


def main() -> QuerySet:
    # Create
    for genre in genres:
        Genre.objects.create(name=genre)
    for firstname, lastname in actors:
        Actor.objects.create(first_name=firstname, last_name=lastname)

    # Update
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu").update(first_name="Keanu", last_name="Reeves")

    # Delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # Return
    result = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return result
