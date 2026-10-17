import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor

list_of_data = ["genre Western",
                "genre Action",
                "genre Dramma",
                "actor George Klooney",
                "actor Kianu Reaves",
                "actress Scarlett Keegan",
                "actor Will Smith",
                "actor Jaden Smith",
                "actress Scarlett Johansson"
                ]


def main() -> QuerySet:
    actors = []
    genres = []
    for elem in list_of_data:
        words = elem.split()
        if "actor" in words or "actress" in words:
            actors.append((tuple(words)))
        if "genre" in words:
            genres.append((tuple(words)))

    for s_h, f_name, l_name in actors:
        Actor.objects.create(first_name=f_name, last_name=l_name)

    for genre, movie in genres:
        Genre.objects.create(name=movie)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    Actor.objects.filter(last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves")

    action = Genre.objects.get(name="Action")
    action.delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
