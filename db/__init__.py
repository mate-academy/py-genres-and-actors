from db.models import Genre, Actor
from django.db.models import QuerySet


def main() -> QuerySet:
    western = Genre.objects.create(name="Western")
    action = Genre.objects.create(name="Action")
    drama = Genre.objects.create(name="Dramma")

    george_clooney = Actor.objects.create(first_name="George", last_name="Klooney")
    keanu_reeves = Actor.objects.create(first_name="Kianu", last_name="Reaves")
    scarlett_keegan = Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    will_smith = Actor.objects.create(first_name="Will", last_name="Smith")
    jaden_smith = Actor.objects.create(first_name="Jaden", last_name="Smith")
    scarlett_johanson = Actor.objects.create(first_name="Scarlett", last_name="Johanson")

    drama.objects.update(name="Drama")
    drama.save()

    george_clooney.objects.update(last_name="Clooney")
    george_clooney.save()

    keanu_reeves.objects.update(first_name="Keanu", last_name="Reeves")
    keanu_reeves.save()

    action.delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("last_name")
