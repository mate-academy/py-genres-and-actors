import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet[Actor, Genre]:
    # Criar gêneros
    western = Genre.objects.create(name="Western")
    action = Genre.objects.create(name="Action")
    dramma = Genre.objects.create(name="Dramma")

    # Criar atores e atrizes
    george_klooney = Actor.objects.create(first_name="George", last_name="Klooney")
    kianu_reeves = Actor.objects.create(first_name="Kianu", last_name="Reaves")
    scarlett_keegan = Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    will_smith = Actor.objects.create(first_name="Will", last_name="Smith")
    jaden_smith = Actor.objects.create(first_name="Jaden", last_name="Smith")
    scarlett_johansson = Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # Atualizando o nome do gênero sobrenome de um usuário
    dramma = Genre.objects.get(name="Dramma")
    dramma.name = "Drama"
    dramma.save()
    george_klooney = Actor.objects.get(first_name="George", last_name="Klooney")
    george_klooney.last_name = "Clooney"   
    george_klooney.save()
    kianu_reeves = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    kianu_reeves.last_name = "Reeves"
    kianu_reeves.save() 

    # Deletando um ator
    scarlett_keegan = Actor.objects.get(first_name="Scarlett", last_name="Keegan")
    scarlett_keegan.delete()

    # Retornar todos os atores
    last_name = "Smith"
    actors_with_last_name_smith = Actor.objects.filter(last_name=last_name)
    actors_Ordered_by_first_name = Actor.objects.order_by("first_name")        
    for actor in actors_with_last_name_smith:
        print(actor.first_name, actor.last_name) 
    for actor in actors_Ordered_by_first_name:
        print(actor.first_name, actor.last_name)    


