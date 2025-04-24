import init_django_orm  # noqa: F401
from db.models import Genre, Actor
from django.db.models import QuerySet


def main() -> QuerySet:
    # Gêneros
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")  # erro intencional para corrigir depois

    # Atores
    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # Atualizações
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    # Deletar especificamente "Scarlett Keegan"
    Actor.objects.filter(first_name="Scarlett").delete()
    Genre.objects.filter(name="Action").delete()

    # Consultar atores com o sobrenome "Smith" e ordená-los pelo primeiro nome
    smith_actors = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
    return smith_actors


if __name__ == "__main__":
    print(main())
