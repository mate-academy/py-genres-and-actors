from db.models import Actor, Genre

def create_genre(genre):
    for name in genre:
        Genre.objects.create(name=name)

def create_actor(actor):
    for first_name, last_name in actor:
        Actor.objects.create(first_name=first_name, last_name=last_name)

def update_genre():
    return Genre.objects.filter(name= 'Dramma').update(name="Drama")

def update_clooney():
    return Actor.objects.filter(first_name = 'George', last_name= 'Klooney').update(last_name="Clooney")

def update_reeves():
    return Actor.objects.filter(first_name= 'Kianu', last_name= 'Reaves').update(first_name="Keanu", last_name='Reeves')


def delete_genre():
    return Genre.objects.filter(name= 'Action').delete()

def delete_actress():
    return Actor.objects.filter(first_name= 'Scarlett').delete()

def main():
    genres = ["Western", "Action", "Dramma"]
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    create_genre(genres)
    create_actor(actors)
    update_genre()
    update_clooney()
    update_reeves()
    delete_genre()
    delete_actress()
    return Actor.objects.filter(last_name= "Smith").order_by("first_name")
