from db.models import Genre, Actor

def main():
    western = Genre.objects.create(name="Western")
    action = Genre.objects.create(name="Action")
    dramma = Genre.objects.create(name="Dramma")

    george = Actor.objects.create(first_name="George", last_name="Klooney")
    kianu = Actor.objects.create(first_name="Kianu", last_name="Reaves")
    scarlett = Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    will = Actor.objects.create(first_name="Will", last_name="Smith")
    jaden = Actor.objects.create(first_name="Jaden", last_name="Smith")
    second_scarlett = Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    dramma.name = "Drama"
    dramma.save()

    george.last_name = "Clooney"
    george.save()

    kianu.first_name = "Keanu"
    kianu.save()

    action.delete()

    scarlets = Actor.objects.get(first_name="Scarlett")
    scarlets.delete()

    actors_smith = Actor.objects.filter(first_name="Smith").order_by("first_name")
    return actors_smith
