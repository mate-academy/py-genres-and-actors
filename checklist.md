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
```

Bad example:
```python
Model.objects.create(first="a")
Model.objects.create(first="b")
Model.objects.create(first="c")
```

### 4. Don't forget to add migrations to your PR.

