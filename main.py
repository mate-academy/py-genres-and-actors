import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


# Genre
def create_genre(name: str) -> None:
    Genre.objects.create(name=name)


def update_genre(genre_id: int, genre_name: str) -> None:
    Genre.objects.filter(id=genre_id).update(name=genre_name)


def all_genres() -> QuerySet:
    return Genre.objects.all()


def delete_genre(genre_id: int) -> None:
    Genre.objects.filter(id=genre_id).delete()


# Actor
def create_actor(first_name: str, last_name: str) -> None:
    Actor.objects.create(first_name=first_name, last_name=last_name)


def update_actor(actor_id: int, first_name: str, last_name: str) -> None:
    data = {}
    if first_name:
        data["first_name"] = first_name
    if last_name:
        data["last_name"] = last_name
    if data:
        Actor.objects.filter(id=actor_id).update(**data)


def all_actors() -> QuerySet:
    return Actor.objects.all()


def delete_actor(actor_id: int) -> None:
    Actor.objects.filter(id=actor_id).delete()


def main() -> QuerySet:

    # Create genres
    for genre in ["Western", "Action", "Dramma"]:
        create_genre(genre)

    # Create actors
    actore = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Keegan"),
        ("Scarlett", "Johansson")
    ]
    for first_name, last_name in actore:
        create_actor(first_name, last_name)

    # Update genre Dramma -> Drama
    dramma = Genre.objects.get(name="Dramma")
    update_genre(dramma.id, "Drama")

    # Update actors
    george = Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).first()
    update_actor(
        george.id,
        first_name="George",
        last_name="Clooney"
    )

    kianu = Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).first()
    update_actor(kianu.id, first_name="Keanu", last_name="Reeves")

    # Delete genre Action
    action = Genre.objects.filter(name="Action").first()
    delete_genre(action.id)

    # Delete all Scarletts
    Actor.objects.filter(first_name="Scarlett").delete()

    # Повертаємо QuerySet акторів із прізвищем "Smith"
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
