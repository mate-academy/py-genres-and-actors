import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    western_genre = Genre.objects.create(
        name="Western",
    )
    print(western_genre)

    action_genre = Genre.objects.create(
        name="Action",
    )
    print(action_genre)

    drama_genre = Genre.objects.create(
        name="Dramma",
    )
    print(drama_genre)

    george_actor = Actor.objects.create(
        first_name="George",
        last_name="Klooney",
    )
    print(george_actor)

    kianu_actor = Actor.objects.create(
        first_name="Kianu",
        last_name="Reaves",
    )
    print(kianu_actor)

    scarlet_actress = Actor.objects.create(
        first_name="Scarlett",
        last_name="Keegan",
    )
    print(scarlet_actress)

    will_actor = Actor.objects.create(
        first_name="Will",
        last_name="Smith",
    )
    print(will_actor)

    jaden_actress = Actor.objects.create(
        first_name="Jaden",
        last_name="Smith",
    )
    print(jaden_actress)

    johansson_actress = Actor.objects.create(
        first_name="Scarlett",
        last_name="Johansson",
    )
    print(johansson_actress)

    update_drama_genre = Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")
    print(update_drama_genre)

    update_george = Actor.objects.filter(
        last_name="Klooney",
    ).update(last_name="Clooney")
    print(update_george)

    kianu_update = Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves",
    ).update(first_name="Keanu", last_name="Reeves")
    print(kianu_update)

    delete_genre = Genre.objects.filter(
        name="Action",
    ).delete()
    print(delete_genre)

    delete_all_scarletts = Actor.objects.filter(
        first_name="Scarlett",
    ).delete()
    print(delete_all_scarletts)

    to_return = Actor.objects.filter(
        last_name="Smith",
    ).order_by("first_name")
    return to_return
