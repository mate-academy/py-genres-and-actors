import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    for name in ["Western", "Action", "Dramma"]:
        Genre.objects.create(name=name)

    for first_name, last_name in [("George", "Klooney"),
                                  ("Kianu", "Reaves"),
                                  ("Scarlett", "Keegan"),
                                  ("Will", "Smith"),
                                  ("Jaden", "Smith"),
                                  ("Scarlett", "Johansson")]:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(last_name="Reeves", first_name="Keanu")
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    print(main())
