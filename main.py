import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres_list = ["Western", "Action", "Dramma"]
    actors_dict = {
        "George": "Klooney",
        "Kianu": "Reaves",
        "Scarlett": "Keegan",
        "Will": "Smith",
        "Jaden": "Smith",
        "Johanson": "Scarlett",
    }
    for genre in genres_list:
        Genre.objects.create(name=genre)
    for actor in actors_dict.keys():
        if actor != "Johanson":
            Actor.objects.create(first_name=actor,
                                 last_name=actors_dict[actor])
        else:
            Actor.objects.create(first_name=actors_dict[actor],
                                 last_name=actor)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )
    Actor.objects.filter(first_name="Scarlett").delete()
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
