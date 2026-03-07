from db.models import Genre, Actor


def main():
    # CREATE
    western = Genre.objects.create(name="Western")
    action = Genre.objects.create(name="Action")
    dramma = Genre.objects.create(name="Dramma")

    george = Actor.objects.create(first_name="George", last_name="Klooney")
    kianu = Actor.objects.create(first_name="Kianu", last_name="Reaves")
    scarlett1 = Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    will_smith = Actor.objects.create(first_name="Will", last_name="Smith")
    jaden_smith = Actor.objects.create(first_name="Jaden", last_name="Smith")
    scarlett2 = Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # UPDATE
    dramma.name = "Drama"
    dramma.save()

    george.last_name = "Clooney"
    george.save()

    kianu.first_name = "Keanu"
    kianu.last_name = "Reeves"
    kianu.save()

    # DELETE
    action.delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # RETURN
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
