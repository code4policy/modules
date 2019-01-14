# Data 3-2: Python - CSV/TSV

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
