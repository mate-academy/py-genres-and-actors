import init_django_orm  # noqa: F401
from db.models import Genre, Actor


def main():
    genres = ["Western", "Action", "Dramma"]
    actors = ["George Klooney", "Kianu Reaves", "Scarlett Keegan",
              "Will Smith", "Jaden Smith", "Scarlett Johansson"]

    for genre in genres:
        # try:
        #     Genre.objects.get(name=genre)
        # except Genre.DoesNotExist:
        Genre.objects.create(name=genre)

    for actor in actors:
        first_name, last_name = actor.split()
        # try:
        #     Actor.objects.get(first_name=first_name, last_name=last_name)
        # except Actor.DoesNotExist:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    Genre.objects.filter(name=genres[-1]).update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Klooney").update(
        last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu",
        last_name="Reeves")

    Genre.objects.filter(name=genres[1]).delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").all().order_by("first_name")


if __name__ == "__main__":
    main()
