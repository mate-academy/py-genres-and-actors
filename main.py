from db.models import Genre, Actor
from django.db.models import QuerySet

def main() -> QuerySet[Actor]:
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

    actor_george = Actor.objects.get(first_name="George", last_name="Klooney")
    actor_george.last_name = "Clooney"
    actor_george.save()

    actor_kianu = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    actor_kianu.first_name = "Keanu"
    actor_kianu.last_name = "Reeves"
    actor_kianu.save()

    Genre.objects.filter(name="Action").delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    smith_actors = Actor.objects.filter(last_name="Smith").order_by("first_name")

    return smith_actors


if __name__ == "__main__":
    print(main())
    print(Genre.objects.all())
    print(Actor.objects.all())