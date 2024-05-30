import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Genre
from db.models import Actor

def main() -> QuerySet:
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")
    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    genre_dramma = Genre.objects.get(name="Dramma")
    genre_dramma.name = "Drama"
    genre_dramma.save()

    actor_klooney = Actor.objects.get(first_name="George", last_name="Klooney")
    actor_klooney.last_name = "Clooney"
    actor_klooney.save()

    actor_reaves = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    actor_reaves.first_name = "Keanu"
    actor_reaves.last_name = "Reeves"
    actor_reaves.save()

    Genre.objects.get(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    set_of_actors = Actor.objects.filter(last_name="Smith").order_by('first_name')
    return set_of_actors


if __name__ == "__main__":
    print(main())





