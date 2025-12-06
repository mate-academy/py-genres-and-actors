from django.db.models import QuerySet

import init_django_orm  # noqa: F401
from db.models import Genre, Actor


def create_genres(genre_names: tuple) -> None:
    for name in genre_names:
        Genre.objects.create(
            name=name
        )


def create_actors(actor_items: tuple) -> None:
    for first_name, last_name in actor_items:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name
        )


def update_genre(old_name: str, new_name: str) -> None:
    Genre.objects.filter(
        name=old_name
    ).update(
        name=new_name
    )


def update_actor(
        first_name: str = None,
        last_name: str = None,
        new_first_name: str = None,
        new_last_name: str = None
) -> None:
    if first_name:
        if not last_name:
            Actor.objects.filter(
                first_name=first_name
            ).update(
                first_name=new_first_name
            )
        else:
            Actor.objects.filter(
                first_name=first_name,
                last_name=last_name
            ).update(
                first_name=new_first_name,
                last_name=new_last_name
            )
    elif last_name:
        Actor.objects.filter(
            last_name=last_name
        ).update(
            last_name=new_last_name
        )


def delete_genre(name_to_delete: str) -> None:
    Genre.objects.filter(
        name=name_to_delete
    ).delete()


def delete_actor(
        first_name: str = None,
        last_name: str = None
) -> None:
    if first_name:
        if last_name:
            Actor.objects.filter(
                first_name=first_name,
                last_name=last_name
            ).delete()
        else:
            Actor.objects.filter(
                first_name=first_name
            ).delete()
    elif last_name:
        Actor.objects.filter(
            last_name=last_name
        ).delete()


def search_actors(
        first_name: str = None,
        last_name: str = None,
        ordering: str = None
) -> QuerySet:
    queryset = Actor.objects.all()
    if first_name:
        if last_name:
            queryset = queryset.filter(
                first_name=first_name,
                last_name=last_name
            )
        else:
            queryset = queryset.filter(
                first_name=first_name
            )
    elif last_name:
        queryset = queryset.filter(
            last_name=last_name
        )
    if ordering:
        queryset = queryset.order_by(ordering)
    return queryset


def main() -> QuerySet:
    create_genres(genre_names=(
        "Western",
        "Action",
        "Dramma"
    ))
    create_actors(actor_items=(
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ))
    update_genre("Dramma", "Drama")
    update_actor(
        last_name="Klooney",
        new_last_name="Clooney"
    )
    update_actor(
        first_name="Kianu",
        last_name="Reaves",
        new_first_name="Keanu",
        new_last_name="Reeves"
    )
    delete_genre(
        name_to_delete="Action"
    )
    delete_actor(
        first_name="Scarlett"
    )
    queryset = search_actors(
        last_name="Smith",
        ordering="first_name"
    )
    return queryset
