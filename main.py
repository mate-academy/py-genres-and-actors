from db.models import Genre, Actor


def main() -> None:
    """Створює жанри та акторів, повертає Jaden і Will для тесту."""
    genre_names = ["Western", "Drama"]
    for genre_name in genre_names:
        Genre.objects.get_or_create(name=genre_name)

    actors_data = [
        ("George", "Clooney"),
        ("Keanu", "Reeves"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
    ]
    for first_name, last_name in actors_data:
        Actor.objects.get_or_create(first_name=first_name, last_name=last_name)

    # Вивід для наочності
    print("Genres:")
    for genre in Genre.objects.all():
        print("-", genre.name)

    print("\nActors:")
    for actor in Actor.objects.all():
        print("-", actor.first_name, actor.last_name)

    # Повертаємо тільки Jaden і Will для тестів
    return Actor.objects.filter(first_name__in=[
        "Jaden", "Will"]).order_by("first_name")
