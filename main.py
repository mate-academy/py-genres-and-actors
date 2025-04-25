from db.models import Genre, Actor


def main():
    # Create Genres
    genres = ["Western", "Action", "Dramma"]
    for genre_name in genres:
        Genre.objects.create(name=genre_name)

    # Create Actors
    actor_data = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in actor_data:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    # Update Dramma -> Drama
    Genre.objects.filter(name="Dramma").update(name="Drama")

    # Update actor names
    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    # Delete Action genre
    Genre.objects.filter(name="Action").delete()

    # Delete all actresses with first_name Scarlett
    Actor.objects.filter(first_name="Scarlett").delete()

    # Return actors with last_name "Smith", ordered by first_name
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
