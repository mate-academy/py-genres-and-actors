# Cinema Hall

Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before starting.

In `db/models.py` create table `Genre` with such fields:
- char field `name`, name of the genre with the maximum length of 255 
characters.

Also, create table `Actor` with such fields:
- char field `first_name`, name of the actor with the maximum length of 255 
characters;
- char field `last_name`, surname of the actor with the maximum length of 255 
characters.

Inside `main.py`, create `main` function.
This function should perform these actions:
1. Create:
   - genre Western
   - genre Action
   - genre Dramma
   - actor George Klooney
   - actor Kianu Reaves
   - actress Scarlett Keegan
   - actor Will Smith
   - actor Jaden Smith
   - actress Scarlett Johansson
2. Update:
   - genre Dramma, set `name` to "Drama"
   - actor George Klooney, set `last_name` to "Clooney"
   - actor Kianu Reaves, set `first_name` to "Keanu" and `last_name` to "Reeves"
3. Delete:
   - genre Action
   - all actresses with the `first_name` "Scarlett"
4. Return:
   - QuerySet of actors with `last_name` "Smith" and ordered by `first_name`
   
**Note**: if you need to sort the QuerySet, you can use 
[.order_by()](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#order-by) 
method

Example:
```python
print(main())
# <QuerySet [<Actor: Jaden Smith>, <Actor: Will Smith>]>

print(Genre.objects.all())
# <QuerySet [<Genre: Western>, <Genre: Drama>]>

print(Actor.objects.all())
# <QuerySet [<Actor: George Clooney>, <Actor: Keanu Reeves>, <Actor: Will Smith>, <Actor: Jaden Smith>]>
```

### Note: Check your code using this [checklist](checklist.md) before pushing your solution.
