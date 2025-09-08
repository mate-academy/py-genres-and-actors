from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    Genre.objects.all().delete()
    Actor.objects.all().delete()

    genres = ["Western", "Action", "Dramma"]
    for gen in genres:
        Genre.objects.create(name=gen)

    actors = [("George", "Klooney"), ("Kianu", "Reaves"),
              ("Scarlett", "Keegan"), ("Will", "Smith"),
              ("Jaden", "Smith"), ("Scarlett", "Johansson")]
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    dramma = Genre.objects.get(name="Dramma")
    dramma.name = "Drama"
    dramma.save()


    george = Actor.objects.get(last_name="Klooney")
    george.last_name = "Clooney"
    george.save()

    kianu = Actor.objects.get(first_name="Kianu")
    kianu.first_name = "Keanu"
    kianu.last_name = "Reeves"
    kianu.save()

    Genre.objects.get(name="Action").delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
