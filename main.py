import init_django_orm  # noqa: F401


from django.db.models import QuerySet
from db.models import Genre, Actor


actors = [
    ("George", "Klooney"), ("Kianu", "Reaves"), ("Scarlett", "Keegan"),
    ("Scarlett", "Keegan"), ("Will", "Smith"), ("Jaden", "Smith"),
    ("Scarlett", "Johansson")
]

genre = ["Western", "Action", "Dramma"]


def main() -> QuerySet:
    for genre_name in genre:
        Genre.objects.create(name=genre_name)

    for f_name, l_name in actors:
        Actor.objects.create(first_name=f_name, last_name=l_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu", last_name="Reeves"
    )

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    queryset = Actor.objects.filter(last_name="Smith").order_by(
        "first_name"
    )
    return queryset
