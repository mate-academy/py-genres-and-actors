import init_django_orm  # noqa: F401

# from django.db import connection
from django.db.models import QuerySet
from db.models import Genre, Actor


# def reset_table(table_name: str) -> None:
#     with connection.cursor() as cursor:
#         cursor.execute(f"DELETE FROM '{table_name}';")
#         cursor.execute(
#             f"DELETE FROM sqlite_sequence WHERE name='{table_name}';"
#         )


def main() -> QuerySet:
    # reset_table("db_genre")
    # reset_table("db_actor")

    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")
    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu")
    Actor.objects.filter(last_name="Reaves").update(last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
