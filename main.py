import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")  # Replace "your_project_name"
django.setup()

from db.models import Genre, Actor

def main():
    western_genre = Genre.objects.create(name="Western")
    action_genre = Genre.objects.create(name="Action")
    drama_genre = Genre.objects.create(name="Dramma")

    george_klooney = Actor.objects.create(first_name="George", last_name="Klooney")
    keanu_reaves = Actor.objects.create(first_name="Kianu", last_name="Reaves")
    scarlett_keegan = Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    will_smith = Actor.objects.create(first_name="Will", last_name="Smith")
    jaden_smith = Actor.objects.create(first_name="Jaden", last_name="Smith")
    scarlett_johansson = Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    drama_genre.name = "Drama"
    drama_genre.save()

    george_klooney.last_name = "Clooney"
    george_klooney.save()

    keanu_reaves.first_name = "Keanu"
    keanu_reaves.last_name = "Reeves"
    keanu_reaves.save()

    action_genre.delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    smith_actors = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return smith_actors

if __name__ == "__main__":
    actors = main()
    print(actors)
    print(Genre.objects.all())
    print(Actor.objects.all())
