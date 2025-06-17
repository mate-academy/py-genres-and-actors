import init_django_orm  # noqa: F401
from .db.models import Genre, Actor
from django.db.models import QuerySet


def main() -> QuerySet:
    western = Genre()
    western.name = "Western"
    western.save()

    action = Genre()
    action.name = "Action"
    action.save()

    dramma = Genre()
    dramma.name = "Dramma"
    dramma.save()

    george_klooney = Actor()
    george_klooney.first_name = "George"
    george_klooney.last_name = "Klooney"
    george_klooney.save()

    kianu_reaves = Actor()
    kianu_reaves.first_name = "Kianu"
    kianu_reaves.last_name = "Reaves"
    kianu_reaves.save()

    scarlett_keegan = Actor()
    scarlett_keegan.first_name = "Scarlett"
    scarlett_keegan.last_name = "Keegan"
    scarlett_keegan.save()

    will_smith = Actor()
    will_smith.first_name = "Will"
    will_smith.last_name = "Smith"
    will_smith.save()

    jaden_smith = Actor()
    jaden_smith.first_name = "Jaden"
    jaden_smith.last_name = "Smith"
    jaden_smith.save()

    scarlett_johansson = Actor()
    scarlett_johansson.first_name = "Scarlett"
    scarlett_johansson.last_name = "Johansson"
    scarlett_johansson.save()

    dramma.name = "Drama"
    dramma.save()

    george_klooney.last_name = "Clooney"
    george_klooney.save()

    kianu_reaves.first_name = "Keanu"
    kianu_reaves.last_name = "Reeves"
    kianu_reaves.save()

    action.delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
