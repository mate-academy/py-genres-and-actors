import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for genre in genres:
        Genre.objects.create(name=genre)
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Genre.objects.filter(name="Action").delete()

    for first_name_, last_name_ in actors:
        Actor.objects.create(first_name=first_name_, last_name=last_name_)
    upd_name_ls = [("George", "Clooney"), ("Kianu", "Reeves")]
    for filter_, new_ in upd_name_ls:
        Actor.objects.filter(first_name=filter_).update(last_name=new_)
    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu")
    Actor.objects.filter(first_name="Scarlett").delete()
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
