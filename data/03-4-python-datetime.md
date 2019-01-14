# Data 3-4: Python - Datetime

We can use the `datetime` module to parse dates and convert them from one format to another. We will primarily be using the `datetime.datetime.strptime` and `datetime.datetime.strftime` methods. Check http://strftime.org/ for the format string codes.

```python
import datetime

raw_date = "2017-01-11"
date_format = "%Y-%m-%d"

parsed_date = datetime.datetime.strptime(raw_date, date_format)

print(parsed_date.strftime("%x")) # 01/11/17
```

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

1. Set a variable birthday = "1-May-12".
2. Parse the date using datetime.datetime.strptime.
3. Use strftime to output a date that looks like "5/1/2012".
