# Command Line 3

## Redirection & Piping

##### Redirecting output to file: `>`

```
command > filename
```

Takes the output of `command` and saves it in `filename`. This will overwrite the file if it already exists.

##### Redirecting output and appending to file: `>>`

```
command >> filename
```

Takes the output of `command` and appends it to the end of the content of `filename`. This will create the file if it does not yet exist.

##### Piping: `|`

```
command1 | command2
```

Pipes the results from `command1` as input to `command2`, and then the results of `command2` are printed to the console.

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example: Redirection

1. Redirect a fact about planet mars into the mars.txt.

```
echo "Mars is dusty." > ~/Development/universe/solar_system/planets/mars.txt
```

2. Add another mars fact to mars.txt.

```
echo "Mars has an 687 day year." >> ~/Development/universe/solar_system/planets/mars.txt
```

3. Cat the contents of mars.txt.

```
cat ~/Development/universe/solar_system/planets/mars.txt
```

4. Make sure there is at least one newline at the end of `mars.txt`.

  You can check if there is a newline at the end of the file if there is no `%` sign that appears at the end of the file.

  ![](https://i.imgur.com/k8XBUQF.png)

  In this screenshot, the first example with the `%` at the end has no newline. The latter example does.

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example: piping

Count the number of characters in the string "hello world" using `wc`.

```
echo "hello world" | wc -c
```

Count the number of lines in the file `mars.txt`

```
cat ~/Development/universe/solar_system/planets/mars.txt | wc -l
```

Count the number of characters in the first line of `mars.txt`

```
cat ~/Development/universe/solar_system/planets/mars.txt | head -n 1 | wc -c
```

## ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

Count the number of characters in `mars.txt`
Count the number of characters in the last line of `mars.txt`


## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example: piping

Count number of **folders** in the `universe` folder.

```
cd ~/Development/universe
find . -type d | wc -l
```

## ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

Count number of **files** in the `universe` folder.

## Slackcat

Lets install a new command-line tool. On macOS use `brew install slackcat`. For linux, see the bottom of this page https://github.com/vektorlab/slackcat for instructions.

Configure slackcat by running this command and following the instructions in your web browser:

```
slackcat --configure
```

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example

Let's use slackchat to send a simple message to the `#scratchwork` channel.

```
echo "hello world" | slackcat -c scratchwork
```

## ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

Notice how the message is being sent as a snippet. Figure out how to send a normal, non-snippet, message using slackcat.

<!--
echo "hello" | slackcat -t -s -c scratchwork
-->

## ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

1. Count the total number of files and folders in the `~/Development/universe/` directory and send this to the person sitting next to you using slackcat. Use only one line and piping. You can use the `--noop` flag to first test it out without sending the message, then you can remove it to send the message. (hint: start with `tree`)

<!--
cd ~/Development/universe/solar_system/planets
tree | wc -l | slackcat -s -c scratchwork
-->

2. In the `~/Development/universe` directory, run `ls`, pipe the output of that into slackcat and send it to the `#scratchwork` channel. This time, make sure to send it as a snippet.

<!--
cd ~/Development/universe/solar_system
tree | slackcat -c scratchwork
-->

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example: piping and redirection

House Office Expenditure Data: https://projects.propublica.org/represent/expenditures

1. Let's start a new directory for the house expenditure data.

    ```
    cd ~/Development
    mkdir house-expenditure
    cd house-expenditure
    ```

4. Download the Q2 2017 expenditure detail data and pipe it into a file.

    ```
    curl "https://projects.propublica.org/congress/assets/staffers/2017Q2-house-disburse-detail.csv" > 2017Q2-house-disburse-detail.csv
    ```

5. Print the header (first line) of this file.

    ```
    head -n 1 2017Q2-house-disburse-detail.csv
    ```

6. Print the last 12 lines of this file.

    ```
    tail -n 12 2017Q2-house-disburse-detail.csv
    ```

7. Count the number of lines in this file.

    ```
    cat 2017Q2-house-disburse-detail.csv | wc -l
    ```

8. Count the number of rows in this file that contains the word "technology" (case insensitive)

    ```
    cat 2017Q2-house-disburse-detail.csv | grep -i technology | wc -l
    ```

9. Return only the rows containing the word "technology" and redirect the output into a file. Keep the header.

    ```
    head -1 2017Q2-house-disburse-detail.csv > technology.csv
    cat 2017Q2-house-disburse-detail.csv | grep -i technology >> technology.csv
    ```

10. Grep a word of your choice and send the first 5 lines to #scratchwork channel on slack.

    ```
    cat 2017Q2-house-disburse-detail.csv | grep -i technology | head -n 5 | slackcat --filename technology.csv -c scratchwork
    ```
