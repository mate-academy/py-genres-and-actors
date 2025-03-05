import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from models import Genre, Actor


def main() -> QuerySet:
    western = Genre.objects.create(name="Western")
    drama = Genre.objects.create(name="Drama")
    action = Genre.objects.create(name="Action")

    george_clooney = Actor.objects.create(first_name="George", last_name="Clooney")
    keanu_reeves = Actor.objects.create(first_name="Keanu", last_name="Reeves")
    scarlett_keegan = Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    will_smith = Actor.objects.create(first_name="Will", last_name="Smith")
    jaden_smith = Actor.objects.create(first_name="Jaden", last_name="Smith")
    scarlett_johansson = Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Clooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Keanu", last_name="Reeves").update(first_name="Keanu", last_name="Reeves")
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    smith_actors = Actor.objects.filter(last_name="Smith").order_by('first_name')
    return smith_actors

    actors = Actor.objects.filter(last_name="Smith").order_by("first_name")
    for actor in actors:
        print(actor)
