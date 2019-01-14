# Data 3-6: Python - Filtering and Grouping

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

### Read/Write JSON from STDIN/STDOUT

Read From STDIN
```python
#!/usr/bin/env python3

import sys
import json

# read data from STDIN
input_str = sys.stdin.read()

# parse data as a json
data = json.loads(input_str)
```

Transform data...

Write `data` to stdout.
```
json.dump(data, sys.stdout, indent=4)
```
