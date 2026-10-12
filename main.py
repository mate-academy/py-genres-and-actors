import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet[Actor]:
    # Criar gêneros
    Genre.objects.create(name="Western")
    action = Genre.objects.create(name="Action")
    dramma = Genre.objects.create(name="Dramma")

    # Criar atores e atrizes
    george_klooney = Actor.objects.create(
        first_name="George",
        last_name="Klooney"
    )
    kianu_reeves = Actor.objects.create(
        first_name="Kianu",
        last_name="Reaves"
    )
    Actor.objects.create(
        first_name="Scarlett",
        last_name="Keegan"
    )
    Actor.objects.create(
        first_name="Will",
        last_name="Smith"
    )
    Actor.objects.create(
        first_name="Jaden",
        last_name="Smith"
    )
    Actor.objects.create(
        first_name="Scarlett",
        last_name="Johansson"
    )

    # Atualizando o nome do gênero sobrenome de um usuário
    dramma = Genre.objects.get(name="Dramma")
    dramma.name = "Drama"
    dramma.save()
    george_klooney = Actor.objects.get(
        first_name="George",
        last_name="Klooney"
    )

    george_klooney.last_name = "Clooney"
    george_klooney.save()
    kianu_reeves = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    kianu_reeves.last_name = "Reeves"
    kianu_reeves.first_name = "Keanu"
    kianu_reeves.save()

    # Deletando um ator
    Actor.objects.filter(first_name="Scarlett").delete()

    # Deletando gênero de ação
    action = Genre.objects.get(name="Action")
    action.delete()

    # Retornar todos os atores
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
