import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    def create() -> None:
        genres = ["Western", "Action", "Dramma"]
        for genre in genres:
            Genre.objects.create(name=genre)

        actors = [
            ("George", "Klooney"),
            ("Kianu", "Reaves"),
            ("Scarlett", "Keegan"),
            ("Will", "Smith"),
            ("Jaden", "Smith"),
            ("Scarlett", "Smith"),
        ]
        for name, surname in actors:
            Actor.objects.create(first_name=name, last_name=surname)

    def update() -> None:
        genres_to_update = [("Dramma", "Drama")]
        for old_name, new_name in genres_to_update:
            Genre.objects.filter(
                name=old_name,
            ).update(name=new_name)

        actors_to_update = [
            (["George", "Klooney"], ["George", "Clooney"]),
            (["Kianu", "Reaves"], ["Keanu", "Reeves"]),
        ]
        for old_name, new_name in actors_to_update:
            Actor.objects.filter(
                first_name=old_name[0],
                last_name=old_name[1],
            ).update(
                first_name=new_name[0],
                last_name=new_name[1],
            )

    def delete() -> None:
        Genre.objects.filter(
            name="Action",
        ).delete()
        Actor.objects.filter(
            first_name="Scarlett",
        ).delete()

    def read() -> QuerySet:
        return Actor.objects.filter(
            last_name="Smith",
        ).order_by("first_name")

    create()
    update()
    delete()
    return read()
