import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genrs = ["Western", "Action", "Dramma"]
    for gen in genrs:
        Genre.objects.create(name=gen)

    actore_nam = [["George", "Klooney"], ["Kianu", "Reaves"],
                  ["Scarlett", "Keegan"], ["Will", "Smith"],
                  ["Jaden", "Smith"]]
    for act in actore_nam:
        Actor.objects.create(first_name=act[0], last_name=act[1])

    Genre.objects.filter(name="Dramma").update(name="Drama")
    (Actor.objects.filter(first_name="George", last_name="Klooney")
     .update(last_name="Clooney"))
    (Actor.objects.filter(first_name="Kianu", last_name="Reaves")
     .update(first_name="Keanu", last_name="Reeves"))
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    get_actor = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return get_actor
