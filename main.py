import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    # creating
    ls_1 = ["Western", "Action", "Dramma"]
    for element in ls_1:
        Genre.objects.create(name=element)
    ls_2 = [["George", "Klooney"], ["Kianu", "Reaves"], ["Scarlett", "Keegan"],
            ["Will", "Smith"], ["Jaden", "Smith"], ["Scarlett", "Johansson"]]
    for element in ls_2:
        Actor.objects.create(first_name=element[0], last_name=element[1])
    # updating
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )
    # deleting
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
