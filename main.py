import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    # create
    list_of_genre = ["Western", "Action", "Dramma"]
    list_of_actors = [["George", "Klooney"],
                      ["Kianu", "Reaves"],
                      ["Scarlett", "Keegan"],
                      ["Will", "Smith"],
                      ["Jaden", "Smith"],
                      ["Scarlett", "Johansson"]]
    for genre in list_of_genre:
        Genre.objects.create(name=genre)
    for actor in list_of_actors:
        Actor.objects.create(first_name=actor[0], last_name=actor[1])
    # update
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu")
    Actor.objects.filter(last_name="Reaves").update(last_name="Reeves")
    # delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    # return
    list_of_smith = []
    for smith in Actor.objects.all():
        if smith.last_name == "Smith":
            list_of_smith.append(smith)
    return QuerySet.order_by(list_of_smith[1], list_of_smith[0])
