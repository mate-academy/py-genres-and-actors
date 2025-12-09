import os
import django
from db.models import Genre, Actor

from django.urls import path

urlpatterns = []


def main():
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Dramma")
    Genre.objects.create(name="Action")

    Actor.objects.create(first_name="George", last_name="Klooney", is_actress=False)
    Actor.objects.create(first_name="Kianu", last_name="Reaves", is_actress=False)
    Actor.objects.create(first_name="Scarlett", last_name="Keegan", is_actress=True)
    Actor.objects.create(first_name="Will", last_name="Smith", is_actress=False)
    Actor.objects.create(first_name="Jaden", last_name="Smith", is_actress=False)
    Actor.objects.create(first_name="Scarlett", last_name="Johansson", is_actress=True)

    Genre.objects.filter(name="Dramma").update(name="Drama")

    Actor.objects.filter(first_name="George", last_name="Klooney").update(last_name="Clooney")

    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu",
        last_name="Reeves"
    )

    Genre.objects.filter(name="Action").delete()

    Actor.objects.filter(is_actress=True, first_name="Scarlett").delete()

    smith_actors = Actor.objects.filter(last_name="Smith").order_by('first_name')

    return smith_actors


if __name__ == "__main__":

    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
        django.setup()
    except Exception as e:
        print(f"Błąd konfiguracji Django. Upewnij się, że masz skonfigurowany projekt i settings.py. Szczegóły: {e}")

    print(main())

    print(Genre.objects.all())

    print(Actor.objects.all())