import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor

def main() -> QuerySet:
    # Criar Gêneros
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")

    #Criar Atores
    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # Updates
    genre = Genre.objects.filter(name="Dramma").first()
    if genre:
        genre.name = "Drama"
        genre.save()

    actor = Actor.objects.get(first_name="George", last_name="Klooney")
    actor.last_name = "Clooney"
    actor.save()

    actor = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    actor.first_name = "Keanu"
    actor.last_name = "Reeves"
    actor.save()

    # Deletes
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
    # O return tem que ficar por último, se não tudo acima será ignorado.


if __name__ == "__main__":
    result = main()
    print(result)
