import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    data = [("genre", "Western"),
            ("genre", "Action"),
            ("genre", "Dramma"),
            ("actor", "George", "Klooney"),
            ("actor", "Kianu", "Reaves"),
            ("actress", "Scarlett", "Keegan"),
            ("actor", "Will", "Smith"),
            ("actor", "Jaden", "Smith"),
            ("actress", "Scarlett", "Johansson")]
    for item in data:
        if item[0] == "genre":
            Genre.objects.create(name=item[1])
        if item[0] == "actor" or item[0] == "actress":
            Actor.objects.create(first_name=item[1],
                                 last_name=item[2])

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")

    (Actor.objects.filter(
        first_name="Kianu", last_name="Reaves")
     .update(
        first_name="Keanu", last_name="Reeves"))

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    result = Actor.objects.filter(last_name="Smith").order_by("first_name")

    return result


if __name__ == "__main__":
    main()
