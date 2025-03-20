import init_django_orm  # noqa: F401

from django.db.models import QuerySet
import db.models as models


def main() -> QuerySet:
    models.Genre.objects.create(name="Western")
    models.Genre.objects.create(name="Action")
    models.Genre.objects.create(name="Dramma")
    models.Actor.objects.create(first_name="George", last_name="Klooney")
    models.Actor.objects.create(first_name="Kianu", last_name="Reaves")
    models.Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    models.Actor.objects.create(first_name="Will", last_name="Smith")
    models.Actor.objects.create(first_name="Jaden", last_name="Smith")
    models.Actor.objects.create(first_name="Scarlett", last_name="Johansson")
    models.Genre.objects.filter(name="Dramma").update(name="Drama")
    models.Actor.objects.filter(last_name="Klooney").update(
        last_name="Clooney"
    )
    models.Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves").update(
        first_name="Keanu",
        last_name="Reeves")
    models.Genre.objects.filter(name="Action").delete()
    models.Actor.objects.filter(first_name="Scarlett").delete()
    return models.Actor.objects.filter(
        last_name="Smith"
    ).all().order_by("first_name")


if __name__ == "__main__":
    print(main())
    print(models.Genre.objects.all())
    print(models.Actor.objects.all())
