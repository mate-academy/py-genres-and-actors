import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Genre, Actor


class ManagerGenre:

    @staticmethod
    def genre_create(name: str) -> None:
        Genre.objects.create(name=name)

    @staticmethod
    def genre_update(id_to_update: int, new_name: str) -> None:
        Genre.objects.filter(id=id_to_update).update(name=new_name)

    @staticmethod
    def genre_delete(delete_name: str) -> None:
        Genre.objects.filter(name=delete_name).delete()


class ManagerActor:

    @staticmethod
    def actor_create(first_name: str, last_name: str) -> None:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    @staticmethod
    def actor_update(id_to_update: int,
               new_first_name: str,# noqa E128
               new_last_name: str) -> None:# noqa E128
        Actor.objects.filter(id=id_to_update).update(
            first_name=new_first_name,
            last_name=new_last_name)

    @staticmethod
    def actor_delete(first_name_to_delete: str,
                     last_name_to_delete: str) -> None:
        Actor.objects.filter(first_name=first_name_to_delete,
                             last_name=last_name_to_delete).delete()


def main() -> QuerySet:

    genre_list = ["Western", "Action", "Dramma"]
    for char in genre_list:
        ManagerGenre.genre_create(char)

    actor_list = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for char in actor_list:
        first, last = char
        ManagerActor.actor_create(first, last)

    ManagerGenre.genre_update(3, "Drama")
    ManagerActor.actor_update(1, "George", "Clooney")
    ManagerActor.actor_update(2, "Keanu", "Reeves")
    ManagerGenre.genre_delete("Action")
    ManagerActor.actor_delete("Scarlett", "Johansson")
    ManagerActor.actor_delete("Scarlett", "Keegan")
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
