import init_django_orm  # noqa: F401

from db.models import Genre
from db.models import Actor

def main():
#Create
    Genre.objects.create("Western")
    Genre.objects.create("Action")
    Genre.objects.create("Dramma")
    Genre.objects.create("Dramma")
    Genre.objects.create("Dramma")
    Actor.objects.create("George", "Klooney")
    Actor.objects.create("Kianu", "Reaves")
    Actor.objects.create("Scarlett", "Keegan")
    Actor.objects.create("Will", "Smith")
    Actor.objects.create("Jaden", "Smith")
    Actor.objects.create("Scarlett", "Johansson")
#Update
    Genre.objects.filter("Dramma").update("Drama")
    Actor.objects.filter(first_name="George", last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(first_name="Keanu", last_name="Reeves")
#Delete
    Genre.objects.filter("Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
#Read
    return Actor.objects.filter(last_name="Smith").all().order_by("first_name")
