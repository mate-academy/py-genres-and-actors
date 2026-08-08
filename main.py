import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    western_genre = Genre.objects.create(name="Western")
    action_genre = Genre.objects.create(name="Action")
    dramma_genre = Genre.objects.create(name="Dramma")

    first_actor = Actor.objects.create(first_name="George", last_name="Klooney")
    second_actor = Actor.objects.create(first_name="Kianu", last_name="Reaves")
    first_actress = Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    third_actor = Actor.objects.create(first_name="Will", last_name="Smith")
    fourth_actor = Actor.objects.create(first_name="Jaden", last_name="Smith")
    second_actress = Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    drama_genre = Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")
    first_genre = Actor.objects.filter(
        last_name="Klooney",
    ).update(last_name="Clooney")
    second_actor = Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    delete_action_genre = Genre.objects.filter(
        name="Action",
    ).delete()
    delete_actresses = Actor.objects.filter(
        first_name="Scarlett",
    ).delete()

    return Actor.objects.filter(last_name="Smith").order_by(
        "first_name",
    )
