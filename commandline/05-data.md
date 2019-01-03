# Command Line 5 - Data in the command line


### CSV (Comma Separated Values)

A simple format that can be viewed in excel. Really easy to see in text editor, contains only one table. Lets look at an example CSV file. Here is some data on expenditures in the U.S. House of Representatives:

https://projects.propublica.org/represent/expenditures

### Lets grab one file and take a look

Grab a file
```
wget https://projects.propublica.org/congress/assets/staffers/2017Q1-house-disburse-detail.csv
```

Take a look

```
head 2017Q1-house-disburse-detail.csv
wc -l 2017Q1-house-disburse-detail.csv
```

Find something

```
cat 2017Q1-house-disburse-detail.csv | grep WATER
```

Where did the header go?

```
curl "https://projects.propublica.org/congress/assets/staffers/2017Q1-house-disburse-detail.csv" | egrep -i "water|bioguide" > water.txt

cat water.txt| csvstat
```


### Hmm...this is getting complex, lets use CSVKit

[https://csvkit.readthedocs.io/en/1.0.1/](https://csvkit.readthedocs.io/en/1.0.1/). This program is its both a command line interface (CLI) and a python package. It helps parse CSVs cleanly.

```
pip3 install csvkit
```

#### Examples

Now we can search within a column

```
cat 2017Q1-house-disburse-detail.csv | csvgrep -c OFFICE -m WATER > spending_by_waters_office.csv
cat spending_by_waters_office.csv |csvstat

cat 2017Q1-house-disburse-detail.csv | csvgrep -c PURPOSE -m WATER > spending_on_water.csv
> cat spending_on_water.csv | csvstat
```

Hmm...who is spending so much on water?

```
cat spending_on_water.csv | grep "40333.33"
```

### Sed, Awk, more data manipulation

#### Example using in2csv and csvstat

```
in2csv roster.xlsx | csvstat
```

#### Example using in2csv and sed and awk

```
in2csv roster.xlsx | csvcut -c 9 | tail -n +2 | awk '{gsub("\"", "")}1' | cut -d'|' -f 1 | sed 's/^[ \t]*//;s/[ \t]*$//' | sort | uniq -c
```

#### Why would you ever do this?

* Reproducability
* Portability
* Transparancy
* To be obnioxious
* Simplicity and ease of use. Once you're comfortable with this, its easier sometimes to use the command line for simple cleaning operations before piping to file and starting the real analysis.
