# Data 2: CLI

The command line is a powerful tool for data transformations. We've discussed some CLI tools already such as `grep` that can be used to transform data. Let's delve into a few more.

## `csvlook`

`csvlook` is part of `csvkit` that we installed earlier. It allows to "pretty print" a csv file in the command line.

Here is an example from an old FiveThirtyEight [article on Alcohol Consumption](https://fivethirtyeight.com/features/dear-mona-followup-where-do-people-drink-the-most-beer-wine-and-spirits/).

```bash
curl -s 'https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv' | csvlook
```

For very long or very wide CSV files, you can pipe the output of `csvlook` into `less`.

```bash
curl -s 'https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv' | csvlook | less
```

## `csvgrep`

Note how `grep` leaves out the header of the CSV. As part of csvkit, there's a version of grep specific to csvs: `csvgrep`. This allows 1) to grep the contents of a single column and 2) to view the header after grepping.

```bash
curl -s 'https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv' | csvgrep -c 'country' -m France
```

## `in2csv`

`in2csv` is a data conversion tool built into CSVKit. 
https://csvkit.readthedocs.io/en/1.0.2/scripts/in2csv.html

```
curl -s "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json" | in2csv -f json -k members
```

Note how you have to specify a toplevel key.

## `jq`

`jq` is a Command-line JSON processor. Here are a few examples using the [superheroes.json](https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json) dataset.

If you don't have jq installed, run `brew install jq` on macOS and `sudo apt-get install jq` on Ubuntu.

### Pretty Print JSON

```bash
curl -s "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json" | jq
```

### Extract just 'members' from JSON

```bash
curl -s "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json" | jq '.members'
```

### Get Member Names

```bash
curl -s "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json" | jq -r '.members[].name'
```

### Get List of Powers

```
curl -s "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json" | jq -r '.members[].powers[]'
```

### Create CSV of Members

```bash
curl -s "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json" | jq -r '.members[] | [.name, .secretIdentity, .age] | @csv'
```
