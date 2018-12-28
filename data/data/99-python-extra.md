# Data ?: Python Extra

While stringing together command line tools can be a quick and efficient way to transform data, it is not as flexible as just writing code.

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example: CSV to JSON

Let's first look at this CSV using `csvlook`.

```
curl -s 'https://bl.ocks.org/mbostock/raw/4063318/dji.csv' | head | csvlook
```

Not to convert this CSV into a JSON, let's run the `csv2json.py` python script in this directory.

```
curl -s 'https://bl.ocks.org/mbostock/raw/4063318/dji.csv' | head | ./csv2json.py
```

Source: https://bl.ocks.org/mbostock/4063318

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example: JSON to CSV

<!--

TODO: find a better flat JSON examples!!!
-->

Let's first take a look at this JSON using `jq`.

```
curl -s 'http://elections.huffingtonpost.com/pollster/api/v2/polls' | jq
```

Let's convert this into a flat JSON array for the purposes of this example.

```
curl -s 'http://elections.huffingtonpost.com/pollster/api/v2/polls' | jq -r '.items[] | {slug, start_date, end_date, survey_house, mode, url, partisanship, partisan_affiliation}' | jq --slurp '.'
```

**Dependency**: the following script depends on the python package `unicodecsv`. Run `pip2 install unicodecsv`

Now let's pipe this into `json2csv.py`.

```
curl -s 'http://elections.huffingtonpost.com/pollster/api/v2/polls' | jq -r '.items[] | {slug, start_date, end_date, survey_house, mode, url, partisanship, partisan_affiliation}' | jq --slurp '.' | ./json2csv.py
```

## ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It: JSON to CSV, current legislators

Take a look at this JSON using `jq`.

```
curl -s 'https://theunitedstates.io/congress-legislators/legislators-current.json' | jq
```

The command below returns a flat JSON of current legislators. Pipe the output of this command into `./json2csv.py`.

```
curl -s 'https://theunitedstates.io/congress-legislators/legislators-current.json' | jq '.[] | {bioguide: .id.bioguide, first: .name.first, last: .name.last, full: .name.official_full, birthday: .bio.birthday, gender: .bio.gender, religion: .bio.religion, party: .terms[-1].party, state: .terms[-1].state}' | jq --slurp '.'
```

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example: JSON to CSV, current legislators 2

Let's do the same example as before but flatten the JSON using `python` instead of `jq`.

```
curl -s 'https://theunitedstates.io/congress-legislators/legislators-current.json' | ./flatten-legislators.py | jq
```

Now we can further pipe this into `json2csv.py` like before.

```
curl -s 'https://theunitedstates.io/congress-legislators/legislators-current.json' | ./flatten-legislators.py | ./json2csv.py
```

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example: JSON to CSV, current legislators 3

To be a bit less verbose, we can also combine all three of these steps into a single script.

**Dependency**: the following script depends on the python package `requests`. Run `pip2 install requests`

```
./download-flatten-and-convert-legislators.py
```
