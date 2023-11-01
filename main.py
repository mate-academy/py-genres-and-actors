import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    with open("data.txt", "r") as f:
        lines = f.read().splitlines()

    for line in lines:
        data = line.split(" ")

        kind_of_data = data[0]

        if kind_of_data == "genre":
            genre = data[1]
            Genre.objects.create(name=genre)
        else:
            first_name, last_name = data[1], data[2]
            Actor.objects.create(first_name=first_name, last_name=last_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
