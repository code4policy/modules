# Data 3-4: Python - Datetime

We can use the `datetime` module to parse dates and convert them from one format to another. We will primarily be using the `datetime.datetime.strptime` and `datetime.datetime.strftime` methods. Check http://strftime.org/ for the format string codes.

```python
from datetime import datetime

raw_date = "2017-01-11"
date_format = "%Y-%m-%d"

parsed_date = datetime.strptime(raw_date, date_format)
date_str = parsed_date.strftime("%m/%d/%y") # 01/11/17
print(date_str)

```

Its often a good idea to put this conversion into a function if you plan to use it again.

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

1. Set a variable birthday = "1-May-12".
2. Parse the date using datetime.datetime.strptime.
3. Use strftime to output a date that looks like "5/1/2012".

Warning! Excel can make dates really weird. Beware: https://github.com/Quartz/bad-data-guide#spreadsheet-has-dates-in-1900-1904-1969-or-1970

Excel has has other weird quirks like having a maximum number of characters per cell or maximum number of rows etc. If you open a CSV in excel and save it, make sure you open it in a text editor once to make sure you didn't lose any data or it didn't do anything unexpected.
