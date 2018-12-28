# Data 5: Regex

## Part 1: Learning  Regular Expressions

### Intro to Regular Expressions

Regular Expressions (Regexes) can be useful for:

* Extracting Data
* Cleaning Dirty Data
* Reformatting Data
* Lots of other programming tasks...

They are supported in most programming languages and text editors. They are used extensively in the command line as well.

**A tutorial we will follow together.**

* https://regexone.com/

**Tutorial Recap**

* Lets recap the lesson by reviewing the "cheat sheet"
	* http://web.mit.edu/hackl/www/lab/turkshop/slides/regex-cheatsheet.pdf

**Concepts Recap**

* Special characters have to be escaped with a `\`
* Using `^` at the start and `$` at the end matches the start and end of a line
* You can capture parts of a pattern in a group using parentheses `()`
* The `|` character is used to indicate "OR"
* Inside square brackets the `^` means "NOT" for example `[^b]` matches any character that is not "b"
* Quantifiers like `*`, `+`, `{4}`, or `{1,4}` can help capture repeated patterns
* `a|b|c|d|e|f` is equivalent to `[abcdef]` which is equivalent to `[a-f]`. All three of these patterns will capture one letter that is a,b,c,d,e, or f.
* `?` can be used to make part of a pattern optional to match

One additional concept we may need

* `^(?!http).*` will match all lines that don't begin with `http`. Just know this pattern and know that its called a "negative lookahead". I'm not going to explain it, but you'll see what it does in the exercises below.

### Regex Exercises

Make sure to press "fork regex" to get your own copy before you mess around with it.
![](https://www.evernote.com/shard/s150/sh/edc138cf-1a64-4771-9da6-d38479aa3c8e/21836d6ddc04aba8/res/684b1904-c2f3-48c4-ab8d-c6bc45a7297e/skitch.png?resizeSmall&width=832)

#### Exercise 1: Words
Pre-Loaded Data: https://regex101.com/r/4jkeQ9/4

1. Match words that start with "a" and end with "d" (will match 5 words)
2. Match words that start with "A" or "a" and end with "d" (will match 7 words)
3. Match words that end with "an" (will match 13 words)
4. Match all words containing "ll"
5. Match all words like "yo-yo" that are split with a hyphen (will match 3 words)
6. Match words that are split with a hypthen, but capture everything to the left of the hyphen in one group and everything to the right of the hyphen in another.

Bonus:

1. Match all words that are split with a hyphen where the contents of the left side are the same as the contents of the right side. (*hint*: you'll have to use a backreference, these are listed in the "cheat sheet").

#### Exercise 2: URLS
Pre-Loaded Data: https://regex101.com/r/2qQTvP/3

1. Match only URLs that start with `http://`or `https://`
2. Match incomplete urls (the opposite of number 1) 
	* hint: Try this regex first `^(?!www).*`
3. Match URLs that begin with `www`
4. Match URLs that don't begin with either `http://`, `https://`, or `www`
5. **Together:** Lets clean these URLS using find and replace in sublime text

#### Exercise 3: People
Pre-Loaded Data: https://regex101.com/r/RWujRv/3

1. Match just the state name
2. Match only the digits in the phone number
3. Match the first and last names in two separate groups
4. Match each column in a separate group
5. Match the phone number in three groups
	* Together: standardize phone numbers into the following format `(XXX)-XXX-XXXX` in sublime text
	* Together: switch first and last name columns and make the first letter of each upper case in sublime text


### Concepts we did not cover
* non-capturing groups
* named groups
* lookahead and lookbehind
* backreference


## Part 2: Cleaning & Extracting Data with Regex

### Sublime Text

#### Multi-line Cursor
- Creating Multi-line cursor
	- `option`+ click and drag
	- Alternatively select all with `Cmd ⌘`+`a`, then `Cmd ⌘`+`Shift`+`l` to create a multiline cursor at the end of each line
- Navigate with multiline cursor
	- ← and → arrow keys
	- `Cmd ⌘`+`←` and `Cmd ⌘`+`→` to go to start or end of each line
	- `option`+`←` and `option`+`→` to go to previous or next delimiter

#### Regular Expressions in Sublime Text

* Regular Expressions Find and Replace ( `Cmd ⌘`+`option`+`f`)

	![](https://www.evernote.com/shard/s150/sh/c369c090-ae6e-46ff-80b0-274d5224f9c6/43f5f856c227e7f8/res/f9a6f0dd-bd1e-4292-9f27-f2a8f5588d50/skitch.png?resizeSmall&width=832)

### Data Extraction Exercises

#### ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example 1 

We're going to grab some data from here: http://www.finra.org/industry/disciplinary-actions. Through some simple find and repalce statements using regex, we will be able to extract structured data from this otherwise unstructured format. 

I've already downloaded the pdf and saved it as a text file, so you can skip straight to opening up the `finra.txt` file in Sublime Text.

1. Search for exactly this text (remember to escape all the special characters)

	> Cadaret, Grant & Co., Inc. (CRD #10641, Syracuse, New York)
	
	**Answer:**
	
	Simply searching for "Cadaret, Grant & Co., Inc. (CRD #10641, Syracuse, New York)" won't work unless you have regex search mode (screenshot above) turned off. Why? Becuase you you are looking for literal parentheses, which is a special character in regex. So first turn on regex search, then escape the special characters. If you search for `Cadaret, Grant & Co., Inc. \(CRD #10641, Syracuse, New York\)` with the parentheses escaped, you should find this one entry.
	

2. Modify the search for that pattern above and capture into groups name of the company, the CRD number, the state, and the city in separate groups.

	**Answer:**

	Here is one possible pattern you could end up with (there are others)

	```
	^(.*) \(CRD #(\d+), (.+), (.+)\)
	```
	
	In order to write this regex, I started with the regex search from the previous part, `Cadaret, Grant & Co., Inc. \(CRD #10641, Syracuse, New York\)` and then started replacing each section with wildcards until I got to `^(.*) \(CRD #(\d+), (.+), (.+)\)`. 
	
	Note: this will not capture items that are split accross multiple lines. It is possible to do that but for the sake of simplicity in this lesson we will ignore those datapoints that match this pattern but are split accross two lines. We will also for the sake of time ignore any lines where the pattern is not the first item in the line.

3. Remove all lines that don't match that pattern

	**Answer:**
	
	We start with the regex above `^(.*) \(CRD #(\d+), (.+), (.+)\)`, and we'll add a .* at the end to capture the rest of the line. `^(.*) \(CRD #(\d+), (.+), (.+)\).*` will now capture the whole line containing the data. However we want to match lines that don't match that pattern. For this we have to surround the regex with a "not"
	
	```
	^(?!^(.*) \(CRD #(\d+), (.+), (.+)\)).*
	```
	
	will then capture all lines that do not start with that pattern. Find and replace anything that matches that pattern with a blank. We have now removed all rows that don't contain the data we're looking for.

4. Remove any stray characters that remain

	**Answer:**
	
	Notice sometimes this stray character appears:
	
	![](https://www.evernote.com/shard/s150/sh/6122e840-30b8-4384-b368-d351bbdf4144/312e1624139319a1/res/ad75d816-256a-4830-a7e0-9835d11d976d/skitch.png?resizeSmall&width=832)
	
	I'm going to copy and paste that into the "find" textbox and replace it with a blank.

5. Remove the empty lines using regex. (hint `\n` will match a new line character)

	**Answer:**
	Replace `\n+` (one or more new lines) with `\n` (one new line)

6. Use regexes to turn the remaining lines into comma separated data. You want it to look something like this

	```
	"Cadaret, Grant & Co., Inc.",10641,"Syracuse","New York"
	"Ameritas Investment Corp.",14869,"Lincoln","Nebraska"
	"Cantor Fitzgerald & Co.",134,"New York","New York"
	"Citadel Securities LLC",116797,"Chicago","Illinois"
	"Citizens Securities, Inc.",39550,"Dedham","Massachusetts"
	```
	
	**Answer:**
	
	Lets start with the pattern that matches the data we want `^(.*) \(CRD #(\d+), (.+), (.+)\)`, then add .* to capture all the rest of the junk in that line. 
	
	Find `^(.*) \(CRD #(\d+), (.+), (.+)\).*`
	
	now each piece of "data" we want is in a capturing group. Replace the above with the capturing groups. I'm going to put quotations around the text values but not number values because that is the way excel likes it:
	
	Replace `"\1",\2,"\3","\4"`
	
	Once your data looks like the screenshot above, go to "file > save as" and save the file as "finra.csv" and open it in excel.
	
**Bonus:**

7. How would you do this so that we don't lose the items that are split across two lines?


#### ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example 2

Use regular expressions to extract table S-10 of this PDF 
https://obamawhitehouse.archives.gov/sites/default/files/omb/budget/fy2017/assets/17msr.pdf

![](https://www.evernote.com/shard/s150/sh/42edde77-7abb-499e-983d-991ccb5e6c72/aa95f0faae21feb4/res/0bba0f48-28b6-4881-a9dc-5d22de68470d/skitch.png?resizeSmall&width=832)

We want to conver this data into a CSV file. CSV stands for "Comma Separated Values" and can be opened in excel. These files have two rules, (1) commas separate table items (unless that comma is contained within quotes) (2) new line separates new rows.

1. Copy and paste the table into sublime text
2. Remove un-necessary rows
	
	**Answer:**
	
	National Aeronautics & Space Administration	and Corporation for National & Community Service are split both split into two rows. 
	
	The pattern to match those two rows goes like this:

	`[^�]+` captures one or more items that are not �
	`([^�]+)\n` captures one or more items that are not � followed by a new line
	`^([^�]+)\n` captures the start of a line, then one or more items that are not � followed by a new line.
	
	So the answer is to find

	```
	^([^�]+)\n
	```
	
	and replace it with
	
	```
	\1 
	```
	note that is `\1` followed by a space ` `

3. Remove all the commas that separate digits from one another. (these are the commas within numbers, for example those found in that final subtotal row).

	**Answer:**
	
	Find

	```
	(\d),(\d)
	```
	
	Replace

	```
	\1\2
	```

4. Put the agency name in quotes and remove the junk that separates that from the data

	**Answer:**
	
	Find
	
	```
	(.+) �+
	```
	
	Replace
	
	```
	"\1"
	```

5. Separate the data with commas instead of spaces 

	**Answer:**
	
	Find 
	
	```
	(["\d\.\–]) (["\d\.\–])
	```
	
	Replace
	
	```
	\1,\2
	```
	
	Also put quotes around "Subtotal, Base Discretionary Funding"

6. Save and open in excel!

	**Answer**
	
	Notice the "m dash" `–` in all the negative numbers appears odd in excel, find and replace that with an "n dash" `-` in sublime and reopen in excel to make it appear properly. (or just find and replace it in excel)

#### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

Lets see if you can extract the value of each gift:

* https://www.chronicle.com/article/Major-Private-Gifts-to-Higher/128264

### Command Line Demonstration

This one you can just watch. I'll demonstrate how regexes can be useful in the command line. Lets look at house expenditure data hosted by propublica.

[https://projects.propublica.org/represent/expenditures](https://projects.propublica.org/represent/expenditures)

This will show me that data in the command line

```
curl https://pp-projects-static.s3.amazonaws.com/congress/staffers/2016Q4-house-disburse-detail.csv
```

Here are the first few lines

```
curl https://pp-projects-static.s3.amazonaws.com/congress/staffers/2016Q4-house-disburse-detail.csv | head
```

Here are all the lines that don't start with a comma

```
curl https://pp-projects-static.s3.amazonaws.com/congress/staffers/2016Q4-house-disburse-detail.csv | grep -e "^[^\,]"
```

This command matches two regexes.
(1) All the rows that don't start with a comma and contain "FEDERAL EXPRESS CORPORATION" `^[^\,].*FEDERAL EXPRESS CORPORATION`
(2) The header of the document (contains "BIOGUIDE_ID) `BIOGUIDE_ID`

```
curl https://pp-projects-static.s3.amazonaws.com/congress/staffers/2016Q4-house-disburse-detail.csv | grep -e "^[^\,].*FEDERAL EXPRESS CORPORATION" -e "BIOGUIDE_ID"
```

I can then pipe that whole command to csvstat and get a summary of expenditures to FedEx from congressional offices. (you'll need CSVkit to use the `csvstat` command, [here](https://csvkit.readthedocs.io/en/1.0.1/tutorial/1_getting_started.html#installing-csvkit) are instructions on installing it.

```
curl https://pp-projects-static.s3.amazonaws.com/congress/staffers/2016Q4-house-disburse-detail.csv | grep -e "^[^\,].*FEDERAL EXPRESS CORPORATION" -e "BIOGUIDE_ID" | csvstat
```

Bonus: Here is a summary of Paul Ryan's expenses

```
curl https://pp-projects-static.s3.amazonaws.com/congress/staffers/2016Q4-house-disburse-detail.csv | grep -e "^[^\,].*HON\. PAUL D\. RYAN" -e "BIOGUIDE_ID" | csvstat
```


### Conclusion

There are lots of other uses for regular expressions. If there is a pattern, it can probably be matched! If you don't know how to do it, you may have to use one of the techniques we didn't cover like lookaheads or lookbehinds. Feel free to contact me for regex help, and please let me know if you use what you learned here. Hofully you can now identify situations in your work where regular expressions may be the answer. 

### Additional Resources

* Useful Resources
	* https://regex101.com/ 
	* https://regexper.com/
* Reinforce learning with these exercises
	* http://expressions.wingtiplabs.com/game
	* http://reg-exp.com/tutorial/
* Advaned, but comprehensive tutorial & reference
	* http://www.regular-expressions.info/  
* Regex Reference Sheets
	* http://web.mit.edu/hackl/www/lab/turkshop/slides/regex-cheatsheet.pdf
	* https://www.debuggex.com/cheatsheet/regex/javascript
	* http://www.petefreitag.com/cheatsheets/regex/
	* http://overapi.com/regex
* Regex Puzzles
	* https://regexcrossword.com/
	* https://alf.nu/RegexGolf
	* https://jimbly.github.io/regex-crossword/
* Regex Search Chrome Extension 
	* 	https://chrome.google.com/webstore/detail/regex-search/bcdabfmndggphffkchfdcekcokmbnkjl?hl=en
* Regex Mug 
	* https://www.zazzle.com/regular_expressions_quick_reference_two_tone_coffee_mug-168607272387736153
	![](https://rlv.zcache.com/regular_expressions_quick_reference_two_tone_coffee_mug-rddd03fccd24e4bd6b58d574e49af4844_x7j1t_8byvr_540.jpg)
