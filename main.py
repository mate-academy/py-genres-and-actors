import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


genre_names = ["Western", "Action", "Dramma"]
actor_names = [
    ("George", "Klooney"),
    ("Kianu", "Reaves"),
    ("Scarlett", "Keegan"),
    ("Will", "Smith"),
    ("Jaden", "Smith"),
    ("Scarlett", "Johansson")
]


def main() -> QuerySet:
    for genre_name in genre_names:
        Genre.objects.create(name=genre_name)
    for actor_f_name, actor_l_name in actor_names:
        (Actor.objects.create
         (first_name=actor_f_name, last_name=actor_l_name))
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    (Actor.objects.filter(first_name="Kianu", last_name="Reaves").update
     (first_name="Keanu", last_name="Reeves"))
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
