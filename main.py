import init_django_orm  # noqa: F401
from db.models import Actor, Genre


def main():
    genres = ["Western", "Action", "Dramma"]
    actors = ["George Klooney", "Kianu Reaves",
              "Scarlett Keegan", "Will Smith",
              "Jaden Smith", "Scarlett Johansson"]
    for genre in genres:
        Genre.objects.create(name=genre)

    for actor in actors:
        separated_actor = actor.split()
        name = separated_actor[0]
        last_name = separated_actor[1]
        Actor.objects.create(first_name=name, last_name=last_name)

    Actor.objects.filter(first_name="George", last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(first_name="Keanu", last_name="Reeves")
    Actor.objects.filter(first_name="Scarlett").delete()

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Genre.objects.filter(name="Action").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name").all()


if __name__ == "__main__":
    main()
