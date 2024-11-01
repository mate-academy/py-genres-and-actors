import init_django_orm  # noqa: F401

from db.models import Genre, Actor


def create() -> None:
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")


def create_actors() -> None:
    Actor.objects.create(
        first_name="George",
        last_name="Klooney",)

    Actor.objects.create(
        first_name="Kianu",
        last_name="Reaves", )

    Actor.objects.create(
        first_name="Scarlett",
        last_name="Keegan", )

    Actor.objects.create(
        first_name="Will",
        last_name="Smith", )

    Actor.objects.create(
        first_name="Jaden",
        last_name="Smith", )

    Actor.objects.create(
        first_name="Scarlett",
        last_name="Johansson", )

def update_actors_and_ganre() -> None:
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu",
                                                    last_name="Reeves")


def delete_actors_and_ganres() -> None:
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

def return_query_set() -> None:
    return Actor.objects.filter(last_name="Smith").order_by("first_name")

def main():
    create()
    create_actors()
    update_actors_and_ganre()
    delete_actors_and_ganres()
    return_query_set()
    return return_query_set()
