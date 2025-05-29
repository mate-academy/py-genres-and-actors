HEAD
# Сheck Your Code Against the Following Points

### 1. Don't add this fragment:
```python
if __name__ == "__main__":
    main()
```
### 2. Put values in the list of tuples for better iterating.

Good example (list of tuples):
```python
for item_first, item_second in items:
       Model.objects.create(
           first=item_first,
           second=item_second
       )
```

Bad example (list of strings):
```python
for item in items:
       Model.objects.create(
           first=item.split()[0],
           second=item.split()[1]
       )
```

### 3. Use the `for` loop in order not to repeat yourself:

Good example:
```python
items = ["a", "b", "c"]


for item in items:
    Model.objects.create(first=item)
# Check Your Code Against the Following Points

## Code Style

1. If you have some long math, you can split it onto additional variables, 
or break after binary operations (not before - it cause the W504 errors)

Good example:

```python
fuel_consumption = max_fuel_consumption * height_fuel_consumption_coeficient
estimated_speed = plan_max_speed - wind_awerage_speed * wind_angle_coefisient
estimated_time = distance_to_the_destinatoin / estimated_speed
how_much_fuel_needed = fuel_consumption * estimated_time * overlap_coeficient
```

Good example:

```python
how_much_fuel_needed = (max_fuel_consumption
                        * height_fuel_consumption_coeficient
                        * distance_to_the_destinatoin
                        / (plan_max_speed
                           - wind_awerage_speed
                           * wind_angle_coefisient)
                        * overlap_coeficient)
```

Bad example:

```python
how_much_fuel_needed = max_fuel_consumption \
                       * height_fuel_consumption_coeficient \
                       * distance_to_the_destinatoin / (
                               plan_max_speed 
                               - wind_awerage_speed 
                               * wind_angle_coefisient
                       ) * overlap_coeficient
```

2. Use descriptive and correct variable names.

Good example:

```python
def get_full_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}"
c457ee4aba3e022c80daa6a7433bb20aead96023
```

Bad example:
```python
HEAD
Model.objects.create(first="a")
Model.objects.create(first="b")
Model.objects.create(first="c")
```

### 4. Don't forget to add migrations to your PR.

def get_full_name(x: str, y: str) -> str:
    return f"{x} {y}"
```

## Clean Code

1. You can avoid else when have return statement.

Good example:

```python
def is_adult(age: int) -> str:
    if age >= 18:
        return "adult"
    return "not an adult"
```

Bad example:

```python
def is_adult(age: int) -> str:
    if age >= 18:
        return "adult"
    else:
        return "not an adult"
```

2. Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.
3. c457ee4aba3e022c80daa6a7433bb20aead96023
