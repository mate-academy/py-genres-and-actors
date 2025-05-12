import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.model import Genre, Actor


def main() -> QuerySet:
    # create
    Genre.objects.create("Western")
    Genre.objects.create("Action")
    Genre.objects.create("Dramma")
    Actor.objects.create("George", "Klooney")
    Actor.objects.create("Kianu", "Reaves")
    Actor.objects.create("Scarlett", "Keegan")
    Actor.objects.create("Will", "Smith")
    Actor.objects.create("Jaden", "Smith")
    Actor.objects.create("Scarlett", "Johansson")
    # update
    Genre.objects.filter(name="Dramma").update("Drama")
    Actor.objects.filter(first_name="George", last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(last_name="Reeves")
    # delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by(first_name)
