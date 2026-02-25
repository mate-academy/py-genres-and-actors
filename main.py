import init_django_orm  # noqa: F401
from django.db import transaction
from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    with transaction.atomic():
        # Clear previous data
        Genre.objects.all().delete()
        Actor.objects.all().delete()

        # ---- Create Genres using a for loop ----
        genres_to_create = ["Western", "Action", "Dramma"]
        for g_name in genres_to_create:
            Genre.objects.create(name=g_name)

        # ---- Update 'Dramma' → 'Drama' and remove 'Action' ----
        Genre.objects.filter(name="Dramma").update(name="Drama")
        Genre.objects.filter(name="Action").delete()

        # ---- Create actors with initial names (typos included) ----
        actors_to_create = [
            ("George", "Klooney"),   # will update
            ("Kianu", "Reaves"),     # will update
            ("Will", "Smith"),
            ("Jaden", "Smith"),
            ("Scarlett", "Keegan"),    # will delete
            ("Scarlett", "Johansson")  # will delete
        ]
        for first, last in actors_to_create:
            Actor.objects.create(first_name=first, last_name=last)

        # ---- Correct names ----
        Actor.objects.filter(first_name="George").update(last_name="Clooney")
        Actor.objects.filter(first_name="Kianu").update(
            first_name="Keanu",
            last_name="Reeves"
        )

        # ---- Delete unnecessary actors ----
        Actor.objects.filter(first_name="Scarlett").delete()

        # ---- Return Smith actors ordered by first name ----
        smith_actors: QuerySet = (
            Actor.objects.filter(last_name="Smith")
            .order_by("first_name")
        )
        return smith_actors
