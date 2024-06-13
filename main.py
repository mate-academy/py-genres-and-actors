import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    names = ["Western", "Action", "Dramma"]
    for name in names:
        Genre.objects.create(name=name)
    first_names = ["George", "Kianu", "Scarlett",
                   "Will", "Jaden", "Scarlett"]
    last_names = ["Klooney", "Reaves", "Keegan",
                  "Smith", "Smith", "Johansson"]
    for first_name, last_name in zip(first_names, last_names):
        Actor.objects.create(first_name=first_name, last_name=last_name)
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu")
    Actor.objects.filter(last_name="Reaves").update(last_name="Reeves")
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    return Actor.objects.all().filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    main()
