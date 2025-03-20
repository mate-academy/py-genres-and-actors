import init_django_orm  # noqa: F401
from db.models import Genre, Actor
from django.db.models import QuerySet


def main() -> QuerySet:
    western = Genre.objects.create(name="Western")
    action = Genre.objects.create(name="Action")
    drama = Genre.objects.create(name="Dramma")
    actor1 = Actor.objects.create(first_name="George", last_name="Klooney")
    actor2 = Actor.objects.create(first_name="Kianu", last_name="Reaves")
    actor3 = Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    actor4 = Actor.objects.create(first_name="Will", last_name="Smith")
    actor5 = Actor.objects.create(first_name="Jaden", last_name="Smith")
    actor6 = Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    update_genre = Genre.objects.filter(name="Dramma").update(name="Drama")
    update_actor1 = Actor.objects.filter(first_name="George").update(last_name="Clooney")
    update_actor2 = Actor.objects.filter(first_name="Kianu").update(first_name="Keanu", last_name="Reeves")

    delete_genre = Genre.objects.filter(name="Action").delete()
    delete_actors = Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")

if __name__ == "__main__":
    print(main())