import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [("George", "Klooney"), ("Kianu", "Reaves"),
              ("Scarlett", "Keegan"), ("Will", "Smith"),
              ("Jaden", "Smith"), ("Scarlett", "Johansson")]

    for item in genres:
        Genre.objects.create(
            name=item,
        )
    print(Genre.objects.all())

    for name, surname in actors:
        Actor.objects.create(
            first_name=name,
            last_name=surname
        )
    print(Actor.objects.all())

    filter_genre_drama = (
        Genre.objects.filter(name="Dramma").update(name="Drama"))

    print(filter_genre_drama)

    filter_clooney = (
        Actor.objects.filter(last_name="Klooney").update(last_name="Clooney"))

    print(filter_clooney)

    filter_kianu = (
        Actor.objects.filter(first_name="Kianu").update(first_name="Keanu"))

    print(filter_kianu)

    delete_action = Genre.objects.filter(name="Action").delete()

    print(delete_action)

    delete_scarlett = Actor.objects.filter(first_name="Scarlett").delete()

    print(delete_scarlett)

    actors = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return actors


if __name__ == "__main__":
    print(main())
