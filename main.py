import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genre_western = Genre.objects.create("Western")
    genre_action = Genre.objects.create("Action")
    genre_drama = Genre.objects.create("Dramma")

    actor_george_klooney = Actor.objects.create(first_name="George", last_name="Klooney")
    actor_kianu_reaves = Actor.objects.create(first_name="Kianu", last_name="Reaves")
    actor_scarlett_keegan = Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    actor_will_smith = Actor.objects.create(first_name="Will", last_name="Smith")
    actor_jaden_smith = Actor.objects.create(first_name="Jaden", last_name="Smith")
    actor_scarlett_johansson = Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    genre_update_drama = Genre.objects.filter(name="Dramma").update(name="Drama")
    actor_update_george_clooney = Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    actor_update_keanu_reeves = (Actor.objects.filter(first_name="", last_name="Reaves")
                                 .update(first_name="Keanu", last_name="Reeves"))

    genre_delete_action = Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()


