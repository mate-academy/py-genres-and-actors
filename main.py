import init_django_orm  # noqa: F401

from db.models import Genre, Actor


def main():
    genres_arr = ["Western", "Action", "Dramma"]

    for genre in genres_arr:
        Genre.objects.create(name=genre)

    actors_arr = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    for first_name, last_name in actors_arr:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")

    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu",
                                                    last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.all().filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    print(main())
