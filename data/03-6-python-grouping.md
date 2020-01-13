# Data 3-6: Python - Grouping

We can use `for` loops, `if` statements, and `dicts` to group data.

### Example 1: Grouping

```python
from pprint import pprint

cars = [
    {"model": "Yaris", "make": "Toyota", "color": "red"},
    {"model": "Auris", "make": "Toyota", "color": "red"},
    {"model": "Camry", "make": "Toyota", "color": "green"},
    {"model": "Prius", "make": "Toyota", "color": "yellow"},
    {"model": "Civic", "make": "Honda", "color": "red"},
    {"model": "Model 3", "make": "Tesla", "color": "red"}
]

cars_by_make = {}
for car in cars:
    make = car['make']
    if make in cars_by_make:
        cars_by_make[make].append(car)
    else:
        cars_by_make[make] = [car]

pprint(cars_by_make)
```

This should output:

```python
{'Honda': [{'make': 'Honda', 'model': 'Civic'}],
 'Tesla': [{'make': 'Tesla', 'model': 'Model 3'}],
 'Toyota': [{'make': 'Toyota', 'model': 'Yaris'},
            {'make': 'Toyota', 'model': 'Auris'},
            {'make': 'Toyota', 'model': 'Camry'},
            {'make': 'Toyota', 'model': 'Prius'}]}
```

### Example 2: Grouping and Counting

```python
number_of_cars_by_make = {}
for car in cars:
    make = car['make']
    if make in number_of_cars_by_make:
        number_of_cars_by_make[make] += 1
    else:
        number_of_cars_by_make[make] = 1

pprint(number_of_cars_by_make)
```

This should output:

```python
{'Honda': 1, 'Tesla': 1, 'Toyota': 4}
```

If you use Python's [Pandas](https://pandas.pydata.org/) library for data manipulation and analysis instead, the code would look like this: https://gist.github.com/AlJohri/59c9762845519f999eb28fe45276f4c1

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

1. Read `vegtables.csv` into a variable called `vegtables`.
2. Group `vegtables` by `color` as a variable `vegtables_by_color`.
3. Output `vegtables_by_color` into a json called `vegtables_by_color.json`.
