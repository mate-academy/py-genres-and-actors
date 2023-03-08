import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [("George", "Klooney"),
              ("Kianu", "Reaves"),
              ("Scarlett", "Keegan"),
              ("Will", "Smith"),
              ("Jaden", "Smith"),
              ("Scarlett", "Johansson")]

    for genre in genres:
        Genre.objects.create(name=genre)

    for name, surname in actors:
        Actor.objects.create(first_name=name, last_name=surname)

    drama = Genre.objects.get(name="Dramma")
    drama.name = "Drama"
    drama.save()

    clooney = Actor.objects.get(last_name="Klooney")
    clooney.last_name = "Clooney"
    clooney.save()

    keanu = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    keanu.first_name = "Keanu"
    keanu.last_name = "Reeves"
    keanu.save()

    Genre.objects.get(name="Action").delete()

    scarlett_ls = Actor.objects.filter(first_name="Scarlett")
    for person in scarlett_ls:
        person.delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
