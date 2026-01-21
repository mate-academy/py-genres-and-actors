import init_django_orm  # Standard for these environments to initialize Django

from db.models import Genre, Actor


def main():
    # --- CREATE ---
    # Genres
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")

    # Actors/Actresses
    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # --- UPDATE ---
    # Update Dramma to Drama
    Genre.objects.filter(name="Dramma").update(name="Drama")

    # Update George Klooney
    Actor.objects.filter(first_name="George", last_name="Klooney").update(
        last_name="Clooney"
    )

    # Update Kianu Reaves
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu",
        last_name="Reeves"
    )

    # --- DELETE ---
    # Delete Genre Action
    Genre.objects.filter(name="Action").delete()

    # Delete all actors/actresses with first_name "Scarlett"
    Actor.objects.filter(first_name="Scarlett").delete()

    # --- RETURN ---
    # Return QuerySet of actors with last_name "Smith" ordered by first_name
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
