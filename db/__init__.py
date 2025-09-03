from django.db.models import QuerySet


def main() -> QuerySet:
    from db.models import Genre, Actor

    Genre.objects.create(name="Western")
    action = Genre.objects.create(name="Action")
    drama = Genre.objects.create(name="Dramma")

    clooney = Actor.objects.create(first_name="George", last_name="Klooney")
    reeves = Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johanson")

    drama.objects.update(name="Drama")
    drama.save()

    clooney.objects.update(last_name="Clooney")
    clooney.save()

    reeves.objects.update(first_name="Keanu", last_name="Reeves")
    reeves.save()

    action.delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("last_name")
