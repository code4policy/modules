# Data 3-7: Python - Filtering and Grouping

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

# filter to red cars

red_cars = []
for car in cars:
    if car['color'] == 'red':
        red_cars.append(car)

# group by make

red_cars_by_make = {}
for car in red_cars:
    make = car['make']
    if make in red_cars_by_make:
        red_cars_by_make[make].append(car)
    else:
        red_cars_by_make[make] = [car]

pprint(red_cars_by_make)
```

Output:

```python
{'Honda': [{'color': 'red', 'make': 'Honda', 'model': 'Civic'}],
 'Tesla': [{'color': 'red', 'make': 'Tesla', 'model': 'Model 3'}],
 'Toyota': [{'color': 'red', 'make': 'Toyota', 'model': 'Yaris'},
            {'color': 'red', 'make': 'Toyota', 'model': 'Auris'}]}
```

## Piping smaller files together

If you're overwhelmed by large python files, you can split up the work into steps and pipe them together. To do this, you'll need to read from STDIN and write to STDOUT in each step.

```python
#!/usr/bin/env python3

import sys
import json

# read data from STDIN
input_str = sys.stdin.read()

# parse data as a json
data = json.loads(input_str)

##########################
# DO SOME TRANSFORMATION #
##########################

# Write data to stdout.
json.dump(data, sys.stdout, indent=4)
```
