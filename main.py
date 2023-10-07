import init_django_orm  # noqa: F401
from db.models import Genre, Actor
from django.db.models import QuerySet


def main() -> QuerySet:
    create_genres = ["Western", "Action", "Dramma"]
    for genre in create_genres:
        Genre.objects.create(name=genre)

    create_actors = [
        {"first_name": "George", "last_name": "Klooney"},
        {"first_name": "Kianu", "last_name": "Reaves"},
        {"first_name": "Scarlett", "last_name": "Keegan"},
        {"first_name": "Will", "last_name": "Smith"},
        {"first_name": "Jaden", "last_name": "Smith"},
        {"first_name": "Scarlett", "last_name": "Johansson"}
    ]
    for actor_data in create_actors:
        Actor.objects.create(**actor_data)

    update_genres = {"Dramma": "Drama"}
    for old_name, new_name in update_genres.items():
        Genre.objects.filter(name=old_name).update(name=new_name)

    update_actors = [
        {"last_name": "Klooney", "new_last_name": "Clooney"},
        {"first_name": "Kianu", "new_first_name": "Keanu",
         "last_name": "Reaves", "new_last_name": "Reeves"}
    ]
    for actor_data in update_actors:
        filter_fields = {
            key: value for key, value in actor_data.items() if
            not key.startswith("new_")
        }
        update_fields = {
            key.replace("new_", ""): value for key, value in
            actor_data.items() if key.startswith("new_")
        }

        Actor.objects.filter(**filter_fields).update(**update_fields)

    delete_genres = ["Action"]
    for genre_name in delete_genres:
        Genre.objects.filter(name=genre_name).delete()

    delete_actors = {"first_name": "Scarlett"}
    Actor.objects.filter(**delete_actors).delete()

    last_name_is_smith = Actor.objects.filter(
        last_name="Smith").order_by("first_name")

    return last_name_is_smith
