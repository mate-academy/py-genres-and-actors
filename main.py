import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    genre = ["Western", "Action", "Dramma"]

    names = ["George", "Kianu", "Scarlett", "Will", "Jaden", "Scarlett"]
    surnames = ["Klooney", "Reaves", "Keegan", "Smith", "Smith", "Johansson"]

    for i in genre:
        Genre.objects.create(name=i)

    for name, surname in zip(names, surnames):
        Actor.objects.create(first_name=name, last_name=surname)

    Actor.objects.filter(first_name="George",
                         last_name="Klooney").update(last_name="Clooney")

    Actor.objects.filter(first_name="Kianu",
                         last_name="Reaves").update(first_name="Keanu",
                                                    last_name="Reeves")

    Genre.objects.filter(name="Dramma").update(name="Drama")

    Genre.objects.filter(name="Action").delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    result = Actor.objects.filter(last_name="Smith").order_by("first_name")

    return result
