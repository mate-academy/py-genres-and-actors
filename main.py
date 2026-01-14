from db.models import Genre, Actor


def main():
    # Criar gêneros
    genres = ["Western", "Ação", "Drama"]
    for g in genres:
        Genre.objects.create(name=g)

    # Criar atores
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first, last in actors:
        Actor.objects.create(first_name=first, last_name=last)

    # Atualizar gênero "Drama" (já está escrito corretamente, mas mantendo a operação)
    Genre.objects.filter(name="Drama").update(name="Drama")

    # Atualizar atores
    Actor.objects.filter(first_name="George", last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(first_name="Keanu", last_name="Reeves")

    # Excluir gênero "Ação"
    Genre.objects.filter(name="Ação").delete()

    # Excluir todas as atrizes Scarlett
    Actor.objects.filter(first_name="Scarlett").delete()

    # Retornar atores de sobrenome "Smith", ordenados por first_name
    return Actor.objects.filter(last_name="Smith").order_by("first_name")

