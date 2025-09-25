from db.models import Genre, Actor
from django.db import transaction

def main():
    with transaction.atomic():
        # Criar gêneros
        Genre.objects.create(name="Western")
        Genre.objects.create(name="Ação")
        Genre.objects.create(name="Drama")

        # Criar atores e atrizes
        Actor.objects.create(first_name="George", last_name="Klooney")
        Actor.objects.create(first_name="Kianu", last_name="Reaves")
        Actor.objects.create(first_name="Scarlett", last_name="Keegan")
        Actor.objects.create(first_name="Will", last_name="Smith")
        Actor.objects.create(first_name="Jaden", last_name="Smith")
        Actor.objects.create(first_name="Scarlett", last_name="Johansson")

        # Atualizar registros
        Genre.objects.filter(name="Drama").update(name="Drama")  # aparentemente não muda nada
        Actor.objects.filter(first_name="George", last_name="Klooney").update(last_name="Clooney")
        Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(first_name="Keanu", last_name="Reeves")

        # Excluir registros
        Genre.objects.filter(name="Ação").delete()
        Actor.objects.filter(first_name="Scarlett").delete()

        # Retornar QuerySet de atores com last_name "Smith" ordenados por first_name
        result = Actor.objects.filter(last_name="Smith").order_by("first_name")

    return result
