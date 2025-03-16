import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genre_western = Genre("Western")
    genre_action = Genre("Action")
    genre_dramma = Genre("Dramma")

    actor_george_klooney = Actor(first_name = "George", last_name =  "Klooney")
    actor_kianu_reaves = Actor(first_name = "Kianu", last_name =  "Reaves")
    actor_scarlett_keegan = Actor(first_name = "Scarlett", last_name =  "Keegan")
    actor_will_smith = Actor(first_name = "Will", last_name =  "Smith")
    actor_jaden_smith = Actor(first_name = "Jaden", last_name =  "Smith")
    actor_scarlett_johansson = Actor(first_name = "Scarlett", last_name =  "Johansson")


