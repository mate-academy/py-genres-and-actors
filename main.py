import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        Genre.objects.create(name=genre)
    Genre.objects.all()

    actors = [("George", "Klooney"), ("Kianu", "Reaves"),
              ("Scarlett", "Keegan"), ("Will", "Smith"),
              ("Jaden", "Smith"), ("Scarlett", "Johansson")]
    for first, second in actors:
        act = Actor(first_name=first, last_name=second)
        act.save()

    Genre.objects.filter(name="Dramma").update(name="Drama")
    (Actor.objects.filter(first_name="George", last_name="Klooney")
     .update(last_name="Clooney"))
    actor_update = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    actor_update.first_name = "Keanu"
    actor_update.last_name = "Reeves"
    actor_update.save()

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
