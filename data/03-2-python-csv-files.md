# Data 3-2: Python - CSV Files

### Writing a CSV file

We will be using the [`csv.writer`](https://docs.python.org/3/library/csv.html#csv.writer) to write csv files.

```python
import csv

with open('testwrite.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['col1', 'col2'])
    writer.writerow(['val1', 'val2'])
    writer.writerow(['val1', 'val2'])
    writer.writerow(['val1', 'val2'])
```

You can read more about the csv module here: https://docs.python.org/3/library/csv.html


## Opening a CSV file

This snippet opens a file in read only mode and uses the csv module to instantiate a [`csv.DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader). 

The DictReader will parse the CSV and return a dictionary for each record where the keys of the dictionary are the header of the csv. 

Then we take all of those dictionaries and put them into a list with `rows = list(reader)`. `reader` is what is referred to as an `iterable` in python. Running the `list` function exhausts the iterator and just gives us the contents of the reader as a list.)


```python
import csv

with open('testwrite.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(rows)
```

Note that since we have loaded the entire CSV into memory in the variable `rows` we can now put our `for` loop outside of the context manager since we no longer need access to the file, `f`.


### ➡️ Try It

Write a python script called `veggies.py` that defines a list of dicts named vegetables like so:

```python
vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]
```

Write a python program that

1. Loops through each vegetable
2. In the loop, write the name of each vegetable and the color into a CSV called `vegetables.csv`

	The CSV should look like this:
	
	name | color
	-----|-------
	eggplant | purple
	tomato | red
	corn | yellow
	okra | green
	arugula | green
	broccoli | green
	
3. **Bonus**: add the length of the name of the vegtable as separate column

hints:

* Don't forget to first write a header row to the CSV
* To get the length of any string use the builtin `len` method. For example, `len('dhrumil')` is 7.
