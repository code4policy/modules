# Command Line 7

## Setup

On macOS, run `brew install python`. On Ubuntu, run `sudo apt-get install python python-pip`.

Please note that if you don't have csvkit, you'll need to install it.

```
pip2 install csvkit
```

## Homework

The following program reads data from STDIN that is in a csv format and filters rows where someone has made a purchase for water that is over $1000. It writes this data back to STDOUT.

```python
#!/usr/bin/env python2
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

1. cd into your assignments directory
2. save this program as `filter.py`
3. make the script executable (hint: chmod)
4. `curl` the 2017 quarter 1 expenditure file from https://projects.propublica.org/congress/assets/staffers/2017Q1-house-disburse-detail.csv and pipe it into `./filter.py`
	
	note: you have to use the `-N` flag on `curl`
	```
	curl -N "https://projects.propublica.org/congress/assets/staffers/2017Q1-house-disburse-detail.csv" | ./filter.py
	```

5. redirect the output into a file `expensive_water.csv`
6. pipe `expensive_water.csv` into `csvstat` and redirect that into a file called `expensive_water_summary.txt`

### Part 2

1. Modify the above program to get another subset of the data that is interesting to you.
2. Redirect the output to a file called `output.csv`.
3. Write a short description. It can be as short as two sentences.
4. Put it in a file called `description.txt`.
5. Slackcat the contents of `descrption.txt` to the `#assignments` slack channel:

	```
	cat description.txt | slackcat -s -c assignments
	```
6. Pipe `output.csv` into `csvstat` and redirect that into a file called `summary.txt`.
7. You will learn how to submit summary.txt and output.csv via github tomorrow.

### Hints

- in order to pipe an existing file into csvstat, use `cat` to send the contents of the file to stdout first
- use `./filter.py` to run the program
	- remember the `.` refers to the current directory, so `./filter.py` means run the `filter.py` script that is located in the current directory
- make sure filter.py has a shebang on top. the shebang is `#!/usr/bin/env python2`. without the shebang, the shell won't know how to execute your script
- use the 2017 quarter 1 file, quarter 2 might have some issues
