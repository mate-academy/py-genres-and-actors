<!-- @format -->

# Migrations

python manage.py makemigrations db

python manage.py migrate

# Start

python -m main

# Run

print(main())

# <QuerySet [<Actor: Jaden Smith>, <Actor: Will Smith>]>

print(Genre.objects.all())

# <QuerySet [<Genre: Western>, <Genre: Drama>]>

print(Actor.objects.all())

# <QuerySet [<Actor: George Clooney>, <Actor: Keanu Reeves>, <Actor: Will Smith>, <Actor: Jaden Smith>]>
