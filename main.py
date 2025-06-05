from db.models import Genre, Actor
from django.db.models import QuerySet


def main() -> QuerySet:
    # CREATE genres
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Drammma")

    # CREATE actors
    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # UPDATE genre "Dramma" → "Drama"
    Genre.objects.filter(name="Dramma").update(name="Drama")

    # UPDATE George Klooney → George Clooney
    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(last_name="Clooney")

    # UPDATE Kianu Reaves → Keanu Reeves
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    # DELETE genre "Action"
    Genre.objects.filter(name="Action").delete()

    # DELETE actresses with first_name = "Scarlett"
    Actor.objects.filter(first_name="Scarlett").delete()

    # RETURN queryset of actors with last_name "Smith", ordered by first_name
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
