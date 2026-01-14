import init_django_orm  # noqa: F401

from django.db.models import QuerySet


from db.models import Actor, Genre


def main() -> QuerySet:
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    genres = ["Western", "Action", "Dramma"]
    for actor_name, actor_surname in actors:
        Actor.objects.create(first_name=actor_name, last_name=actor_surname)
    for genre in genres:
        Genre.objects.create(name=genre)
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu"
    ).update(
        first_name="Keanu", last_name="Reeves"
    )
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
