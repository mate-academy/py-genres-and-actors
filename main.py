from db.models import Genre, Actor


def main():
    # Create genres
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Drammma")

    # Create actors
    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # Update genre name
    Genre.objects.filter(name="Drammma").update(name="Drama")

    # Update actors
    Actor.objects.filter(first_name="George", last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(first_name="Keanu", last_name="Reeves")

    # Delete genre "Action"
    Genre.objects.filter(name="Action").delete()

    # Delete actresses with first_name "Scarlett"
    Actor.objects.filter(first_name="Scarlett").delete()

    # Return actors with last_name "Smith", ordered by first_name
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
