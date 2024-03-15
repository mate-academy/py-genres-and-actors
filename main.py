import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    Genre.objects.create(name="Western")
    action_genre = Genre.objects.create(name="Action")
    drama_genre = Genre.objects.create(name="Drama")

    george_clooney = Actor.objects.create(
        first_name="George",
        last_name="Clooney"
    )
    keanu_reeves = Actor.objects.create(
        first_name="Kianu",
        last_name="Reeves"
    )
    scarlett_keegan = Actor.objects.create(
        first_name="Scarlett",
        last_name="Keegan"
    )
    Actor.objects.create(
        first_name="Will",
        last_name="Smith"
    )
    Actor.objects.create(
        first_name="Jaden",
        last_name="Smith"
    )
    scarlett_johansson = Actor.objects.create(
        first_name="Scarlett",
        last_name="Johansson"
    )

    drama_genre.name = "Drama"
    drama_genre.save()

    george_clooney.last_name = "Clooney"
    george_clooney.save()

    keanu_reeves.first_name = "Keanu"
    keanu_reeves.last_name = "Reeves"
    keanu_reeves.save()

    action_genre.delete()
    scarlett_keegan.delete()
    scarlett_johansson.delete()

    smith_actors = (Actor.objects.
                    filter(last_name="Smith").
                    order_by("first_name"))
    return smith_actors
