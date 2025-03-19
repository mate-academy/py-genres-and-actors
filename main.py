import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


class ManagerGenre:
    @staticmethod
    def create_genre(name: str) -> None:
        Genre.objects.create(name=name)

    @staticmethod
    def update_genre(old_name: str, new_name: str) -> None:
        Genre.objects.filter(name=old_name).update(name=new_name)

    @staticmethod
    def delete_genre(name: str) -> None:
        Genre.objects.filter(name=name).delete()


class ManagerActor:
    @staticmethod
    def create_actor(first_name: str, last_name: str) -> None:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    @staticmethod
    def update_actor(
            old_first_name: str,
            old_last_name: str,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        Actor.objects.filter(first_name=old_first_name, last_name=old_last_name
                             ).update(
            first_name=new_first_name, last_name=new_last_name
        )

    @staticmethod
    def delete_actor(first_name: str,
                     last_name: str
                     ) -> None:
        Actor.objects.filter(first_name=first_name,
                             last_name=last_name).delete()


def main() -> QuerySet:
    Genre.objects.all().delete()
    Actor.objects.all().delete()

    genre_list = ["Western", "Action", "Dramma"]
    for genre in genre_list:
        ManagerGenre.create_genre(genre)

    ManagerGenre.update_genre("Dramma", "Drama")
    ManagerGenre.delete_genre("Action")

    actor_list = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for actor in actor_list:
        first, last = actor
        ManagerActor.create_actor(first, last)

    ManagerActor.update_actor("George",
                              "Klooney",
                              "George",
                              "Clooney"
                              )
    ManagerActor.update_actor("Kianu",
                              "Reaves",
                              "Keanu",
                              "Reeves"
                              )

    ManagerActor.delete_actor("Scarlett",
                              "Johansson"
                              )
    ManagerActor.delete_actor("Scarlett",
                              "Keegan"
                              )  # Добавляем удаление Scarlett Keegan

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
