from db.models import Genre, Actor


def main():
    genre_action = Genre.objects.create(name="Action")
    genre_drama = Genre.objects.create(name="Drama")

    # Create actors and actresses
    actor_george_clooney = Actor.objects.create(first_name="George", last_name="Klooney")
    actor_kianu_reeves = Actor.objects.create(first_name="Kianu", last_name="Reaves")

    # Update records
    genre_drama.name = "Drama"
    genre_drama.save()

    actor_george_clooney.last_name = "Clooney"
    actor_george_clooney.save()

    actor_kianu_reeves.first_name = "Keanu"
    actor_kianu_reeves.last_name = "Reeves"
    actor_kianu_reeves.save()

    # Delete records
    genre_action.delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # Return the QuerySet of actors with last_name "Smith" ordered by first_name
    actors_with_last_name_smith = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return actors_with_last_name_smith


if __name__ == "__main__":
    result = main()
    print(result)
