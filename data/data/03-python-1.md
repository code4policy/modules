# Data 3: Python 1

While command line tools allows for several quick out of the box data transformations, we resort to Python to doing anything a bit more custom.

## Text Files

### Opening a text file

This snippet opens a file in read only mode (default), loads the entire contents of the file as a string in `full_text` and prints it out.

```python
with open('myfile.txt') as f:
    full_text = f.read()

print full_text
```

`with open(...) as f` is called a "context manager". After opening a file, we generally want to close it to prevent memory leaks. The context manager will do this for us.

### Writing a text file

This snippet opens a file in write mode and writes the word 'hello' with a newline character at the end.

```python
with open('testwrite.txt', 'w') as f:
    f.write('hello')
    f.write('\n')
```

You can append to the end of a file by opening it in the mode `a` like `with open('testwrite.txt', 'a') as f:`.

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

Create a file called `name.txt` with your full name in it.

Write a python script that:

1. reads `name.txt` into a variable `my_name` and then
2. writes a new file named `hello.txt` with the contents `Hello, my name is <my_name>.`

## CSV/TSV

## Opening a CSV file or TSV file

This snippet opens a file in read only mode and uses the csv module to instantiate a [`csv.DictReader`](https://docs.python.org/2/library/csv.html#csv.DictReader). The DictReader will parse the CSV and return a dictionary for each record where the keys of the dictionary are the header of the csv. Then we take all of those dictionaries and put them into a list with `rows = list(reader)`. If we wanted to get all of the rows into a single variable, we can run `rows = list(reader)`. `reader` is what is referred to as an `iterable` in python. Running the `list` function exhausts the iterator and just gives us the contents of the reader as a list.

```python
import csv

with open('myfile.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

for row in rows:
    print(row)
```

Note that since we have loaded the entire CSV into memory in the variable `rows` we can now put our `for` loop outside of the context manager since we no longer need access to the file, `f`.

You can also open a TSV file in the same manner by passing the `delimeter` argument to `csv.DictReader`.

```python
import csv

with open('myfile.tsv') as f:
    reader = csv.DictReader(f, delimeter='\t')
    rows = list(reader)

for row in rows:
    print(row)
```

### Writing a CSV file

We will be using the [`csv.writer`](https://docs.python.org/2/library/csv.html#csv.writer) to write csv files. [`csv.DictWriter`](https://docs.python.org/2/library/csv.html#csv.DictWriter) is a higher level abstraction you can also use but we will be using `csv.writer` in the examples below.

```python
import csv

with open('testwrite.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['col1', 'col2'])
    writer.writerow(['val1', 'val2'])
    writer.writerow(['val1', 'val2'])
    writer.writerow(['val1', 'val2'])
```

You can read more about the csv module here: https://docs.python.org/2/library/csv.html

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

Write a python script that defines a list of dicts named vegetables like so:

```python
vegetables = [
 {"name": "eggplant"},
 {"name": "tomato"},
 {"name": "corn"},
 ...
]
```

Write a python program that 

1. Loops through each vegetable
2. In the loop, writes the name of each vegetable and the length of its name into a CSV

hints: 

* Don't forget to first write a header row to the CSV
* To get the length of any string use the builtin `len` method. For example, `len('dhrumil')` is 7.

## JSON

### Opening a JSON file

This snippet reads `test.json` and loads the contents as a dict into the variable `data`.

```python
import json

with open('test.json') as f:
    data = json.load(f)
```

### Writing a JSON file

```python
import json

rows = [
    {"name": "Rachel", "age": 34},
    {"name": "Monica", "age": 34},
    {"name": "Phoebe", "age": 37}
]

with open('testwrite.json', 'w') as f:
    json.dump(rows, f)
```

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

1. Read `vegetables.csv` into a variable called `vegetables`.
2. Write `vegtables` as a JSON file called `vegetables.json`. It should look like this:

    ```
    [
        {"name": ..., "length": ...},
        {"name": ..., "length": ...},
    ]
    ```

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

Write a python program that outputs a unique list of superhero powers
1. Reads `superheroes.json` (in this folder) 
2. Creates an empty array called `powers`
3. Loops thorough the members of the squad, and appends the powers of each to the `powers` array.
4. Prints those powers to the terminal

hint: To get the unique elements in a list use the `set` method. For example, try running `list(set([1, 1, 2, 3]))` in your python console. Alternatively you can  use an if statement to only add the powers to the list if they are not already in there.

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

Lets Read `superheroes.json` (in this folder) and output a flat CSV of members. The columns should be: `name, age, secretIdentity, powers, squadName, homeTown, formed, secretBase, active`. Any column that is top level, such as `squadName` should just be repeated for every row.

Here is an example set of steps:
1. Read `superheroes.json`
2. Write a header to the CSV file
3. Loop over the members, and for each member write a row to the csv file

HINT: Powers will need to be transformed from a list to a string. You could use `str(powers)` to do this, or you could use `', '.join(['str1', 'str2', 'str3'])` to make it a comma separated list.

## Datetime

We can use the `datetime` module to parse dates and convert them from one format to another. We will primarily be using the `datetime.datetime.strptime` and `datetime.datetime.strftime` methods. Check http://strftime.org/ for the format string codes.

```python
import datetime

raw_date = "2017-01-11"
date_format = "%Y-%m-%d"

parsed_date = datetime.datetime.strptime(raw_date, date_format)

print parsed_date.strftime("%x") # 01/11/17
```

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

1. Set a variable birthday = "1-May-12".
2. Parse the date using datetime.datetime.strptime.
3. Use strftime to output a date that looks like "5/1/2012".

## Filtering

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

# filter whitelist names

whitelist_names = ['Rachel', 'Phoebe']
for row in rows:
    if row['name'] in whitelist_names:
        print(row)

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

## Grouping

We can use `for` loops, `if` statements, and `dicts` to group data.

```python
from pprint import pprint

cars = [
    {"model": "Yaris", "make": "Toyota"},
    {"model": "Auris", "make": "Toyota"},
    {"model": "Camry", "make": "Toyota"},
    {"model": "Prius", "make": "Toyota"},
    {"model": "Civic", "make": "Honda"},
    {"model": "Model 3", "make": "Tesla"},
]

cars_by_make = {}
for car in cars:
    make = car['make']
    if make in cars_by_make:
        cars_by_make[make].append(car)
    else:
        cars_by_make[make] = [car]

pprint(cars_by_make)

# {'Honda': [{'make': 'Honda', 'model': 'Civic'}],
#  'Tesla': [{'make': 'Tesla', 'model': 'Model 3'}],
#  'Toyota': [{'make': 'Toyota', 'model': 'Yaris'},
#             {'make': 'Toyota', 'model': 'Auris'},
#             {'make': 'Toyota', 'model': 'Camry'},
#             {'make': 'Toyota', 'model': 'Prius'}]}

number_of_cars_by_make = {}
for car in cars:
    make = car['make']
    if make in number_of_cars_by_make:
        number_of_cars_by_make[make] += 1
    else:
        number_of_cars_by_make[make] = 1

pprint(number_of_cars_by_make)

# {'Honda': 1, 'Tesla': 1, 'Toyota': 4}
```

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

1. Use excel to add a column `color` to `vegtables.csv`.
2. Read `vegtables.csv` into a variable called `vegtables`.
3. Group `vegtables` by `color` as a variable `vegtables_by_color`.
4. Output `vegtables_by_color` into a json called `vegtables_by_color.json`.
