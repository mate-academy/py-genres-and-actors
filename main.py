import init_django_orm  # noqa: F401

from models import Genre, Actor


def main():
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Drama")

    Actor.objects.create(first_name="George", last_name="Clooney")
    Actor.objects.create(first_name="Keanu", last_name="Reeves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    Actor.objects.filter(first_name="Keanu").update(last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    actors = Actor.objects.filter(last_name="Smith").order_by("first_name")
    for actor in actors:
        print(actor)

if __name__ == "__main__":
    main()
