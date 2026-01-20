from db.models import Genre, Actor


def main() -> Actor.objects.all().__class__:
    # 1. Create gêneros usando for loop + lista
    genres = [
        "Western", "Action", "Dramma"
    ]  # "Dramma" com dois "m" de propósito
    for name in genres:
        Genre.objects.create(name=name)

    # 1. Create atores usando for loop + lista de tuplas
    actors_data = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in actors_data:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    # 2. Update
    Genre.objects.filter(name="Dramma").update(name="Drama")

    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves",
    )

    # 3. Delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # 4. Return QuerySet ordenado
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
