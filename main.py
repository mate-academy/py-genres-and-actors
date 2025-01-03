import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import *


def main() -> QuerySet:
    genre_create_western = Genre.objects.create(name="Western")
    genre_create_action = Genre.objects.create(name="Action")
    genre_create_dramma = Genre.objects.create(name="Dramma")
    actore_create_george = Actor.objects.create(first_name="George", last_name="Klooney")
    actore_create_kianu = Actor.objects.create(first_name="Kianu", last_name="Reaves")
    actore_create_scarlett = Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    actore_create_will = Actor.objects.create(first_name="Will", last_name="Smith")
    actore_create_jaden = Actor.objects.create(first_name="Jaden", last_name="Smith")
    genre_update_dramma = Genre.objects.filter(name="Dramma").update(name="Drama")
    actor_update_george = Actor.objects.filter(first_name="George", last_name="Klooney").update(last_name="Clooney")
    actor_update_kianu = Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(first_name="Keanu", last_name="Reeves")
    del_genre = Genre.objects.filter(name="Action").delete()
    del_actor = Actor.objects.filter(first_name="Scarlett").delete()
    get_actor = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return get_actor
