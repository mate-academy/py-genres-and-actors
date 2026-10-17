from db.models import Genre, Actor


def main():
    western = Genre.objects.create(name="Western")
    action = Genre.objects.create(name="Action")
    drama = Genre.objects.create(name="Dramma")

    george = Actor.objects.create(
        first_name="George", last_name="Klooney"
    )
    keanu = Actor.objects.create(
        first_name="Kianu", last_name="Reaves"
    )
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    drama.name = "Drama"
    drama.save()

    george.last_name = "Clooney"
    george.save()

    keanu.first_name = "Keanu"
    keanu.last_name = "Reeves"
    keanu.save()

    action.delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
