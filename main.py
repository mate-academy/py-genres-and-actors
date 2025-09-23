import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre


def main() -> QuerySet:
    # Create
    iter_genre = ["Western", "Action", "Dramma"]
    iter_actor = ["George Klooney", "Kianu Reaves", "Scarlett Keegan", "Will Smith", "Jaden Smith", "Scarlett Johansson"]

    for _iter in iter_genre:
        Genge.objects.create(
            name=_iter,
        )

    for _iter in iter_actor:
        name = _iter.split()
        Actor.objects.create(
            first_name=name[0],
            last_name=name[1],
        )

    # Update
    Genre.objects.filter(
        name="Dramma",
    ).update(
        name="Drama",
    )

    Actor.objects.filter(
        last_name="Klooney",
    ).update(
       last_name="Clooney",
    )

    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )

    # Delete
    Genre.objects.filter(
        name="Action",
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett",
    )

    # Retrieve
    return Actor.objects.filter(
        last_name="Smith",
    ).all()