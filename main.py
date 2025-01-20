import init_django_orm  # noqa: F401
from db.models import Genre, Actor
from django.db.models import QuerySet


def main() -> QuerySet:
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")

    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Keanu", last_name="Reeves")
    Actress.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actress.objects.create(first_name="Scarlett", last_name="Johansson")

    genre_drama = Genre.objects.get(name="Drama")
    genre_drama.name = "Drama"
    genre_drama.save()

    george = Actor.objects.get(first_name="George", last_name="Klooney")
    george.last_name = "Clooney"
    george.save()

    keanu = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    keanu.first_name = "Keanu"
    keanu.last_name = "Reeves"
    keanu.save()

    Genre.objects.filter(name="Action").delete()
    Actress.objects.filter(first_name="Scarlett").delete()
    actors_with_last_name_smith = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return actors_with_last_name_smith

if __name__ == "__main__":
    actors = main()
    for actor in actors:
        print(actor.first_name, actor.last_name)
