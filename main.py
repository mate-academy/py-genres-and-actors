import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")
    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # 2. Update
    # Megkeressük a rekordot, módosítjuk, majd mentjük
    dramma = Genre.objects.get(name="Dramma")
    dramma.name = "Drama"
    dramma.save()

    klooney = Actor.objects.get(last_name="Klooney")
    klooney.last_name = "Clooney"
    klooney.save()

    kianu = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    kianu.first_name = "Keanu"
    kianu.last_name = "Reeves"
    kianu.save()

    # 3. Delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # 4. Return QuerySet (szűrés és rendezés)
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
