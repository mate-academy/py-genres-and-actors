import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre
from db.models import Actor


def main() -> QuerySet:
    genre_western =\
        Genre.objects.create(name="Western")
    genre_action =\
        Genre.objects.create(name="Action")
    genre_dramma =\
        Genre.objects.create(name="Dramma")
    actor_george_klooney =\
        Actor.objects.create(first_name="George", last_name= "Klooney")
    actor_kianu_reaves =\
        Actor.objects.create(first_name="Kianu", last_name="Reaves")
    actress_scarlett_keegan =\
        Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    actor_will_smith =\
        Actor.objects.create(first_name="Will", last_name="Smith")
    actor_jaden_smith =\
        Actor.objects.create(first_name="Jaden", last_name="Smith")
    actress_scarlett_johansson =\
        Actor.objects.create(first_name="Scarlett", last_name="Johansson")
    genre_dramma.name = "Drama"
    genre_dramma.save()
    actor_george_klooney.last_name = "Clooney"
    actor_george_klooney.save()
    actor_kianu_reaves.first_name = "Keanu"
    actor_kianu_reaves.last_name = "Reeves"
    actor_kianu_reaves.save()
    Actor.objects.filter(first_name="Scarlett").delete()
    Genre.objects.filter(name="Action").delete()
    result = Actor.objects.filter(last_name="Smith").order_by('first_name')
    return result


if __name__ == "__main__":
    print(main())
