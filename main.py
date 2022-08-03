import init_django_orm  # noqa: F401

from db.models import Genre, Actor


genres = ["Western", "Action", "Dramma"]
actors = [
    {"first_name": "George", "last_name": "Klooney"},
    {"first_name": "Kianu", "last_name": "Reaves"},
    {"first_name": "Scarlett", "last_name": "Keegan"},
    {"first_name": "Will", "last_name": "Smith"},
    {"first_name": "Jaden", "last_name": "Smith"},
    {"first_name": "Scarlett", "last_name": "Johansson"}
]


def main():
    for genre in genres:
        Genre.objects.create(name=genre)
    for actor in actors:
        Actor.objects.create(
            first_name=actor["first_name"],
            last_name=actor["last_name"]
        )

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(last_name="Reaves").update(
        first_name="Keanu",
        last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name='Scarlett').delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
