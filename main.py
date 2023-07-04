import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [("George", "Klooney"), ("Kianu", "Reaves"),
              ("Scarlett", "Keegan"), ("Will", "Smith"),
              ("Jaden", "Smith"), ("Scarlett", "Johansson")]
    actors_to_update = [(("George", "Klooney"), ("George", "Clooney")),
                        (("Kianu", "Reaves"), ("Keanu", "Reeves"))]
    for genre in genres:
        Genre.objects.create(name=genre)
    for first_item, second_item in actors:
        Actor.objects.create(
            first_name=first_item,
            last_name=second_item
        )
    Genre.objects.filter(name="Dramma").update(name="Drama")
    for (
            (invalid_first, invalid_last),
            (valid_first, valid_last)
    ) in actors_to_update:
        Actor.objects.filter(
            first_name=invalid_first,
            last_name=invalid_last
        ).update(first_name=valid_first, last_name=valid_last)
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
