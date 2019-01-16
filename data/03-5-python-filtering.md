# Data 3-5: Python - Filtering

We can use `for` loops and `if` statements to filter through data.

```python
rows = [
    {"name": "Rachel", "age": 34},
    {"name": "Monica", "age": 34},
    {"name": "Phoebe", "age": 37}
]

# filter to age < 37
millenials = []
for row in rows:
    if row['age'] < 37:
        millenials.append(row)

print(millenials)
```

```python
# filter whitelist names

cool_people = []
whitelist = ['Rachel', 'Phoebe']
for row in rows:
    if row['name'] in whitelist:
        cool_people.append(row)

print(cool_people)
```

```python
# filter blacklist names

cool_people = []
blacklist = ['Monica']
for row in rows:
    if row['name'] not in blacklist:
        cool_people.append(row)

print(cool_people)
```

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

1. Read vegetables.csv into a variable called `vegetables`.
2. Loop through `vegetables` and filter down to only green vegtables using a whitelist.
3. Print veggies to the terminal
4. Bonus: Output another csv called `green_vegetables.csv`.
