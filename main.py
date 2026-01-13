import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genre_list = ["Western", "Action", "Dramma"]

    actor_dict = {"George": "Klooney",
                  "Kianu": "Reaves",
                  "Scarlett": "Keegan",
                  "Will": "Smith",
                  "Jaden": "Smith",
                  }
    for i in genre_list:
        Genre.objects.create(name=i,)

    for key, value in actor_dict.items():
        Actor.objects.create(first_name=key, last_name=value,)
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George",).update(last_name="Clooney")
    (Actor.objects.filter(first_name="Kianu", last_name="Reaves")
     .update(first_name="Keanu", last_name="Reeves"))
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett", ).delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    main()
