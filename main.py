import init_django_orm  # noqa: F401

from db.models import Genre, Actor


def main():
    genres = ["Western", "Action", "Dramma"]
    actors = ["George Klooney", "Kianu Reaves",
              "Scarlett Keegan", "Will Smith",
              "Jaden Smith", "Scarlett Johansson"]
    for genre in genres:
        new_genre = Genre.objects.create(
            name=genre,
        )
    for actor in actors:
        new_actor = Actor.objects.create(
            first_name=actor.split()[0],
            last_name=actor.split()[1]
        )
    changed_genre = Genre.objects.filter(
        name="Dramma",).update(name="Drama")
    changed_actor_1 = Actor.objects.filter(
        last_name="Klooney", ).update(last_name="Clooney")
    changed_actor_2 = Actor.objects.filter(
        first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves")
    Genre.objects.filter(name="Action",).delete()
    Actor.objects.filter(first_name="Scarlett",).delete()
    return Actor.objects.filter(
        last_name="Smith",).order_by('first_name')


if __name__ == '__main__':
    print(main())
    print(Genre.objects.all())
    print(Actor.objects.all())
