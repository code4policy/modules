# Data 3-5: Python - Filtering

We can use `for` loops and `if` statements to filter through data.

```python
rows = [
    {"name": "Rachel", "age": 34},
    {"name": "Monica", "age": 34},
    {"name": "Phoebe", "age": 37}
]

# filter to age < 37

for row in rows:
    if row['age'] < 37:
        print(row)
```

```python
# filter whitelist names

whitelist_names = ['Rachel', 'Phoebe']
for row in rows:
    if row['name'] in whitelist_names:
        print(row)
```

```python
# blacklist names

blacklist_names = ['Rachel']
for row in rows:
    if row['name'] not in blacklist_names:
        print(row)
```

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

1. Read vegetables.csv into a variable called `vegetables`.
2. Loop through `vegetables` and filter down to only green vegtables using a whitelist.
3. Output another csv called `green_vegetables.csv`.
