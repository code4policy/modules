# Command Line 5

## CSVKit, Sed, Awk, Data Manipulation

For the future, there is CSVKit: [https://csvkit.readthedocs.io/en/1.0.1/](https://csvkit.readthedocs.io/en/1.0.1/). This program is its both a command line interface (CLI) and a python package. It helps parse CSVs cleanly.

```
pip2 install csvkit
```

#### Example using in2csv and csvstat

```
in2csv roster.xlsx | csvstat
```

#### Example using in2csv and sed and awk

```
in2csv roster.xlsx | csvcut -c 9 | tail -n +2 | awk '{gsub("\"", "")}1' | cut -d'|' -f 1 | sed 's/^[ \t]*//;s/[ \t]*$//' | sort | uniq -c
```

#### csvkit example with house expenditure data

```
curl "https://projects.propublica.org/congress/assets/staffers/2017Q1-house-disburse-detail.csv" | egrep -i "water|bioguide" | csvstat
```

```
cd ~/Development/house-expenditure
cat 2017Q1-house-disburse-detail.csv | grep "BIOGUIDE\|WATER" | csvstat
cat 2017Q1-house-disburse-detail.csv | grep "BIOGUIDE\|,HON" | grep "40333.33"
```

#### Why would you ever do this?

* Reproducability
* Portability
* Transparancy
* To be obnioxious
* Simplicity and ease of use. Once you're comfortable with this, its easier sometimes to use the command line for simple cleaning operations before piping to file and starting the real analysis.
