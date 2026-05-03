import init_django_orm  # noqa: F401
from db.models import Genre, Actor
from django.db.models import QuerySet


def main() -> QuerySet:
    Genre.objects.create(name="Western")
    genre_action = Genre.objects.create(name="Action")
    genre_dramma = Genre.objects.create(name="Dramma")
    actor_george = Actor.objects.create(
        first_name="George",
        last_name="Klooney"
    )
    actor_kianu = Actor.objects.create(
        first_name="Kianu",
        last_name="Reaves"
    )
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    genre_dramma.name = "Drama"
    genre_dramma.save()
    actor_george.last_name = "Clooney"
    actor_george.save()
    actor_kianu.first_name = "Keanu"
    actor_kianu.last_name = "Reeves"
    actor_kianu.save()

    genre_action.delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
