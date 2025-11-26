import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
django.setup()

from db.models import Genre, Actor

def main():
    # Create genres
    western = Genre.objects.create(name="Western")
    action = Genre.objects.create(name="Action")
    dramma = Genre.objects.create(name="Dramma")

    # Create actors/actresses
    george = Actor.objects.create(first_name="George", last_name="Klooney")
    keanu = Actor.objects.create(first_name="Kianu", last_name="Reaves")
    scarlett1 = Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    will = Actor.objects.create(first_name="Will", last_name="Smith")
    jaden = Actor.objects.create(first_name="Jaden", last_name="Smith")
    scarlett2 = Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # Update operations
    dramma.name = "Drama"
    dramma.save()

    george.last_name = "Clooney"
    george.save()

    keanu.first_name = "Keanu"
    keanu.last_name = "Reeves"
    keanu.save()

    # Delete operations
    action.delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # Return queryset of actors with last_name "Smith" ordered by first_name
    result = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return result

if __name__ == "__main__":
    qs = main()
    print(qs)
    print(Genre.objects.all())
    print(Actor.objects.all())
