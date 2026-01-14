import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def create(info: list[str | tuple[str, str]]) -> None:
    if isinstance(info[0], str):
        for name in info:
            Genre.objects.create(name=name)
    elif isinstance(info[0], tuple):
        for first_name, last_name in info:
            Actor.objects.create(first_name=first_name, last_name=last_name)


def update(**kwargs) -> None:
    if "name" in kwargs:
        (
            Genre.objects
            .filter(name=kwargs["name"])
            .update(name=kwargs["new_name"])
        )
    elif "first_name" in kwargs:
        update_fields = {}
        if "new_first_name" in kwargs:
            update_fields["first_name"] = kwargs["new_first_name"]
        if "new_last_name" in kwargs:
            update_fields["last_name"] = kwargs["new_last_name"]
        Actor.objects.filter(
            first_name=kwargs["first_name"],
            last_name=kwargs["last_name"]
        ).update(**update_fields)


def delete(**kwargs) -> None:
    if "name" in kwargs:
        Genre.objects.filter(**kwargs).delete()
    if "first_name" in kwargs:
        Actor.objects.filter(**kwargs).delete()


def main() -> QuerySet:
    list_of_genres = ["Western", "Action", "Dramma"]
    list_of_actor = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    create(list_of_genres)
    create(list_of_actor)
    update(name="Dramma", new_name="Drama")

    update(
        first_name="George",
        last_name="Klooney",
        new_last_name="Clooney"
    )
    update(first_name="Kianu",
           last_name="Reaves",
           new_first_name="Keanu",
           new_last_name="Reeves"
           )

    delete(name="Action")
    delete(first_name="Scarlett")

    result_set = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return result_set
