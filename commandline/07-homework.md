# Command Line 7

## Setup

On macOS, run `brew install python`. On Ubuntu, run `sudo apt-get install python3 python3-pip`.

Please note that if you don't have csvkit, you'll need to install it.

```
pip3 install csvkit
```

## Homework

The following program reads data from STDIN that is in a csv format and filters rows where someone has made a purchase for water that is over $1000. It writes this data back to STDOUT.

```python
#!/usr/bin/env python3
import csv
import sys

# read data from STDIN and split on each newline
data = sys.stdin.read().splitlines()

# use python's csv library to create a csv reader and a writer
reader = csv.DictReader(data)
writer = csv.DictWriter(sys.stdout, fieldnames=reader.fieldnames)

# write the header (first line of the csv)
writer.writeheader()

# loop through the rows in the original csv
for row in reader:
	# filter rows
    if row['PURPOSE'] == 'WATER' and float(row['AMOUNT']) > 1000:
    	# write rows that match above filter
        writer.writerow(row)
```

### Part 1

1. Read the script above and try and understand what it's doing.
2. cd into your assignments directory
3. save this program as `filter.py`
4. make the script executable (`chmod +x filter.py`)
5. `curl` the 2017 quarter 1 expenditure file from https://projects.propublica.org/congress/assets/staffers/2017Q1-house-disburse-detail.csv and pipe it into `./filter.py`

	note: you have to use the `-N` flag on `curl`
	```
	curl -N "https://projects.propublica.org/congress/assets/staffers/2017Q1-house-disburse-detail.csv" | ./filter.py
	```

6. redirect the output into a file `expensive_water.csv`
7. pipe `expensive_water.csv` into `csvstat` and redirect that into a file called `expensive_water_summary.txt`
8. open `expensive_water.csv` in Excel and take a look
9. open a file called `expensive_water_description.txt`. In your own words, in a few sentences, explain what you've just done.

### Part 2

1. cd into your assignments directory
2. Save this program again, but this time as `filter_modified.py`
3. Modify the above program to get a different subset of the data that is interesting to you.
4. Redirect the output to a file called `output.csv`.
5. Pipe `output.csv` into `csvstat` and redirect that into a file called `summary.txt`.
6. Look at `output.csv` and `summary.txt`
7. Write a short description of what you've found out about this subset of data and put it in a file called `description.txt`.
8. You will learn how to submit summary.txt and output.csv via github during the next class.

### Hints

- in order to pipe an existing file into csvstat, use `cat` to send the contents of the file to stdout first
- use `./filter.py` to run the program
	- remember the `.` refers to the current directory, so `./filter.py` means run the `filter.py` script that is located in the current directory
- make sure filter.py has a shebang on top. the shebang is `#!/usr/bin/env python3`. without the shebang, the shell won't know how to execute your script
- use the 2017 quarter 1 file, quarter 2 might have some issues


### Final Thoughts

Try your best to not just complete the assignment, but also understand what you're doing each step of the way.
