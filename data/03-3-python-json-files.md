# Data 3-3: Python - JSON

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

### Opening a JSON file

This snippet reads `test.json` and loads the contents as a dict into the variable `data`.

```python
import json

with open('friends.json', 'r') as f:
    data = json.load(f)
    
print(data)
```


### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

In a new file called `cookveggies.py`

1. Read `output/vegetables.csv` (see previous section) into a variable called `vegetables`.
2. Print the variable `vegetables`.
2. Write `vegetables` as a JSON file called `output/vegetables.json`. It should look like this:

    ```
	[
	  { "name": "eggplant", "color": "purple" },
	  { "name": "tomato", "color": "red" },
	  { "name": "corn", "color": "yellow" },
	  { "name": "okra", "color": "green" },
	  { "name": "arugula", "color": "green" },
	  { "name": "broccoli", "color": "green" }
	]
    ```

### ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example

Download superheroes.json

```
wget https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json
```

then write a python program that

1. Reads `superheroes.json` (in this folder)
2. Creates an empty array called `powers`
3. Loop thorough the members of the squad, and append the powers of each to the `powers` array.
4. Prints those powers to the terminal

**Bonus**: make the list of powers unique and print it again

hint for bonus: To get the unique elements in a list use the `set` method. For example, try running `list(set([1, 1, 2, 3]))` in your python console. Alternatively you can use an if statement to only add the powers to the list if they are not already in there.

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

Let's read `superheroes.json` (in this folder) and output a flat CSV of members. The columns should be: `name, age, secretIdentity, powers, squadName, homeTown, formed, secretBase, active`. Any column that is top level, such as `squadName` should just be repeated for every row.

Here is an example set of steps:

1. Read `superheroes.json`
2. Write a header to the CSV file
3. Loop over the members, and for each member write a row to the csv file

The output should look like this:

| name            |       age | secretIdentity | powers                                                                                  | squadName        | homeTown   | formed | secretBase  | active |
| --------------- | --------- | -------------- | --------------------------------------------------------------------------------------- | ---------------- | ---------- | ------ | ----------- | ------ |
| Molecule Man    |        29 | Dan Jukes      | ['Radiation resistance', 'Turning tiny', 'Radiation blast']                             | Super hero squad | Metro City |  2,016 | Super tower |   True |
| Madame Uppercut |        39 | Jane Wilson    | ['Million tonne punch', 'Damage resistance', 'Superhuman reflexes']                     | Super hero squad | Metro City |  2,016 | Super tower |   True |
| Eternal Flame   | 1,000,000 | Unknown        | ['Immortality', 'Heat Immunity', 'Inferno', 'Teleportation', 'Interdimensional travel'] | Super hero squad | Metro City |  2,016 | Super tower |   True |



<!--

import csv
import sys
import json
import requests

data = requests.get('https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json').json()

writer = csv.writer(sys.stdout)

writer.writerow([
    'name', 'age', 'secretIdentity',
    'powers', 'squadName', 'homeTown',
    'formed', 'secretBase', 'active'])

for row in data['members']:
    writer.writerow([
        row['name'], row['age'], row['secretIdentity'],
        str(row['powers']),
        data['squadName'],
        data['homeTown'],
        data['formed'],
        data['secretBase'],
        data['active']
    ])

-->

**Bonus** 

Write one row per power rather than one row per member.
