import init_django_orm  # noqa: F401

from django.db.models import QuerySet


from db.models import Genre, Actor

# import django
# import os
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# django.setup()


def main() -> QuerySet:


    # 1. Create
    # genres
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        Genre.objects.create(name=genre)

    # Genre.objects.create(name="Western")
    # Genre.objects.create(name="Action")
    # Genre.objects.create(name="Dramma")
    #
    # # actor and actress
    actors_data = [
        ("George", "Klooney"),
        ("Kianu", "Reeves"),  # imię specjalnie z literówką, nazwisko już poprawne
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for first_name, last_name in actors_data:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    # Actor.objects.create(first_name="George", last_name="Klooney")
    # Actor.objects.create(first_name="Kianu", last_name="Reeves")
    # Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    # Actor.objects.create(first_name="Will", last_name="Smith")
    # Actor.objects.create(first_name="Jaden", last_name="Smith")
    # Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # 2. Update
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu", last_name="Reeves")

    # 3. Delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()


    # all_actors = Actor.objects.all()
    # for actor in all_actors:
    #     print(actor.first_name, actor.last_name)
    #
    # print("\nGenres")
    # all_genres = Genre.objects.all()
    # for genre in all_genres:
    #     print(genre.name)
    #
    # print("\nSmith:")
    actors_smith = Actor.objects.all().filter(last_name="Smith").order_by("first_name")
    # for actor in actors_smith:
    #     print(actor.first_name, actor.last_name)

    return actors_smith






# if __name__ == "__main__":
#     main()
