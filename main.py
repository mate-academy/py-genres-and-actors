import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor

def main() -> QuerySet:
    #############Creating genres#############
    genres = ["Western", "Action", "Dramma"]

    for genre in genres:
        Genre.objects.create(name=genre)
    #############Creating actors#############
    actors = [("George", "Klooney"),
              ("Kianu", "Reaves"),
              ("Scarlett", "Keegan"),
              ("Will", "Smith"),
              ("Jaden", "Smith"),
              ("Scarlett", "Johansson")]

    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name,
                             last_name=last_name)
    ###################Updating genres######################
    Genre.objects.filter(name="Dramma").update(name="Drama")
    ##################Updating last_name#######################
    Actor.objects.filter(last_name="Klooney").update("Clooney")
    ##################Updating actor###########################
    Actor.objects.filter(last_name="Reaves").update(
        first_name="Keanu",
        last_name="Reeves"
    )
    ##############Deleting a genre##############
    Genre.objects.filter(name="Action").delete()
    ##################Deleting a name###################
    Actor.objects.filter(first_name="Scarlett").delete()
    ###############Return sorted QuerySet###############
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
