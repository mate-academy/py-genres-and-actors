import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet:
    films_name = ["Western", "Action", "Dramma"]
    for item in films_name:
        Genre.objects.create(name=item)
    actors_name = [["George", "Klooney"], ["Kianu", "Reaves"],
                   ["Scarlett", "Keegan"], ["Will", "Smith"],
                   ["Jaden", "Smith"], ["Scarlett", "Johansson"],
                   ]
    for item in actors_name:
        Actor.objects.create(first_name=item[0], last_name=item[1])
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves")
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    return (Actor.objects.filter(
        last_name="Smith").order_by("first_name").all())
