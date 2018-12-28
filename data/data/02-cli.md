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

## `grep`

`grep` can be used to filter any text document. It is most useful for data formats where each line of text is a single record (like a csv).

This example looks filters down the Alcohol Consumption to just Germany.

```bash
curl -s 'https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv' | grep 'Germany'
```

## `csvgrep`

Note how `grep` leaves out the header of the CSV. As part of csvkit, there's a version of grep specific to csvs: `csvgrep`. This allows 1) to grep the contents of a single column and 2) to view the header after grepping.

```bash
curl -s 'https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv' | csvgrep -c 'country' -m France
```

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
