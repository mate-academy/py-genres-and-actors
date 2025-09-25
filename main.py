from db.models import Genre, Actor

def main():
    # Criar gêneros usando lista e loop
    genres = ["Western", "Action", "Dramma"]
    for g in genres:
        Genre.objects.create(name=g)

    # Criar atores/atrizes usando lista de tuplas (first_name, last_name)
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for first, last in actors:
        Actor.objects.create(first_name=first, last_name=last)

    # Atualizações
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(first_name="Keanu", last_name="Reeves")

    # Exclusões
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # Retornar atores com last_name "Smith" ordenados por first_name
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
