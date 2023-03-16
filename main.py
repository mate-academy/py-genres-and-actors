import init_django_orm  # noqa: F401


from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genre1 = Genre(name="Western")
    genre1.save()

    genre2 = Genre(name="Action")
    genre2.save()

    genre3 = Genre(name="Dramma")
    genre3.save()

    actor1 = Actor(first_name="George", last_name="Klooney")
    actor1.save()

    actor2 = Actor(first_name="Kianu", last_name="Reaves")
    actor2.save()

    actress1 = Actor(first_name="Scarlett", last_name="Keegan")
    actress1.save()

    actor3 = Actor(first_name="Will", last_name="Smith")
    actor3.save()

    actor4 = Actor(first_name="Jaden", last_name="Smith")
    actor4.save()

    actress2 = Actor(first_name="Scarlett", last_name="Johansson")
    actress2.save()

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu", last_name="Reeves"
    )

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    queryset = Actor.objects.filter(last_name="Smith").order_by(
        "first_name"
    )
    return queryset


if __name__ == "__main__":
    print(main())
