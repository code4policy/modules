# Data 3-3: Python - JSON

Run this before any of the below snippets.

```bash
wget https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json
```

### Opening a JSON file

This snippet reads `test.json` and loads the contents as a dict into the variable `data`.

```python
import json

with open('superheroes.json', 'r') as f:
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

1. Read `vegetables.csv` (see previous section) into a variable called `vegetables`.
2. Print the variable `vegetables`.
2. Write `vegetables` as a JSON file called `vegetables.json`. It should look like this:

    ```
    [
        {"name": ..., "length": ...},
        {"name": ..., "length": ...},
    ]
    ```

### ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example

Write a python program that outputs a list of superhero powers
1. Reads `superheroes.json` (in this folder)
2. Creates an empty array called `powers`
3. Loop thorough the members of the squad, and append the powers of each to the `powers` array.
4. Prints those powers to the terminal
5. **Bonus**: make the list of powers unique and print it again

hint: To get the unique elements in a list use the `set` method. For example, try running `list(set([1, 1, 2, 3]))` in your python console. Alternatively you can use an if statement to only add the powers to the list if they are not already in there.

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

Lets Read `superheroes.json` (in this folder) and output a flat CSV of members. The columns should be: `name, age, secretIdentity, powers, squadName, homeTown, formed, secretBase, active`. Any column that is top level, such as `squadName` should just be repeated for every row.

Here is an example set of steps:
1. Read `superheroes.json`
2. Write a header to the CSV file
3. Loop over the members, and for each member write a row to the csv file

<!--
TODO
The output should look like this:

```
name, age, secretIdentity, powers, squadName, homeTown, formed, secretBase, active
"Molecule Man",29,"Dan Jukes",
"Madame Uppercut",39,"Jane Wilson",
"Eternal Flame",1000000,"Unknown"
```

```python
import json

with open('superheroes.json', 'r') as f:
    data = json.load(f)

for row in data['members']:
    print(row[])
```

-->

HINT: Powers will need to be transformed from a list to a string. You could use `str(powers)` to do this.
