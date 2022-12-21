import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre

from db.models import Actor


def main() -> QuerySet:
    names = ["Western", "Action", "Dramma"]
    actors = [["George", "Klooney"],
              ["Kianu", "Reaves"],
              ["Scarlett", "Keegan"],
              ["Will", "Smith"],
              ["Jaden", "Smith"],
              ["Scarlett", "Johansson"],
              ]
    for name_ in names:
        Genre.objects.create(
            name=name_,
        )
    for first_name_, last_name_ in actors:
        Actor.objects.create(
            first_name=first_name_,
            last_name=last_name_,
        )
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu",
        last_name="Reeves",
    )
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    return Actor.objects.filter(last_name="Smith").order_by("first_name").all()
