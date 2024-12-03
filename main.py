import init_django_orm # noqa:F401

from db.models import Genre, Actor


def main():
    # Greate genres
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Drama")

    # Create actors and actresses
    Actor.objects.create(first_name="George",
                         last_name="Klooney")
    Actor.objects.create(first_name="Kianu",
                         last_name="Reaves")
    Actor.objects.create(first_name="Scarlett",
                         last_name="Keegan")
    Actor.objects.create(first_name="Will",
                         last_name="Smith")
    Actor.objects.create(first_name="Jaden",
                         last_name="Smith")
    Actor.objects.create(first_name="Scarlett",
                         last_name="Johansson")

    # Update operations
    (Genre.objects.filter(name="Drama")
     .update(name="Drama"))
    (Actor.objects.filter(last_name="Klooney")
     .update(last_name="Clooney"))
    (Actor.objects.filter(first_name="Kianu", last_name="Reaves")
     .update(first_name="Keanu", last_name="Reeves"))


    # Delete operations
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett",
                         last_name="Keegan").delete()


    # Return operations
    smith_actors = (Actor.objects.filter(last_name="Smith")
                    .order_by("first_name"))

    print(Genre.objects.all())
    print(Actor.objects.all())

    return smith_actors

if __name__ == '__main__':
    main()
