import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    for genre in ("Western", "Action", "Dramma"):
        Genre.objects.create(
            name=genre,
        )

    for name, surname in (("George", "Klooney"),
                          ("Kianu", "Reaves"),
                          ("Scarlett", "Keegan"),
                          ("Will", "Smith"),
                          ("Jaden", "Smith"),
                          ("Scarlett", "Johansson"),):
        Actor.objects.create(
            first_name=name,
            last_name=surname,
        )

    Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")

    for name, surname, new_name, new_surname in (
            ("George", "Klooney", "George", "Clooney"),
            ("Kianu", "Reaves", "Keanu", "Reeves"),):
        Actor.objects.filter(
            first_name=name,
            last_name=surname,
        ).update(first_name=new_name, last_name=new_surname)

    Genre.objects.filter(
        name="Action",
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett",
    )

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    print(main())
    # <QuerySet [<Actor: Jaden Smith>, <Actor: Will Smith>]>

    print(Genre.objects.all())
    # <QuerySet [<Genre: Western>, <Genre: Drama>]>

    print(Actor.objects.all())
    # <QuerySet [<Actor: George Clooney>, <Actor: Keanu Reeves>,
    # <Actor: Will Smith>, <Actor: Jaden Smith>]>
