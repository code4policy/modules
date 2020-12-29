# Making Your Terminal ✨PrEtTy✨

Making your terminal pretty makes working on the command line much easier, especially when working with git.
The instructions below will get you set up with a terminal that always shows what folder and git branch you are
on so you never get lost.

<p align="center">
  <img src="https://i.imgur.com/g0mvFWa.gif">
</p>

1. Download [starship](https://starship.rs/), a cross-shell prompt.

    - On macOS: `brew install starship`
    - On Linux: `curl -fsSL https://starship.rs/install.sh | bash`

2. Create the starship configuration file at `~/.config/starship.toml`:

    ```bash
    mkdir ~/.config
    touch ~/.config/starship.toml
    subl ~/.config/starship.toml
    ```

3. Copy and paste the following into the blank file that just opened up in Sublime:
    
    ```toml
    [python]
    disabled = true
    
    [directory]
    truncate_to_repo = false
    truncation_length = 8
    
    [git_branch]
    symbol = ""
    
    [git_status]
    disabled = true
    
    [package]
    disabled = true
    
    [aws]
    disabled = true
    ```

4. Edit your shell profile to enable starship.

    <details>
    <summary>On macOS 10.15+ (Catalina):</summary>


    Open `~/.zshrc` using Sublime Text:
    ```bash
    subl ~/.zshrc
    ```
    
    Then, add this to the end of the file:

    ```bash
    export EDITOR="subl --wait"
    eval "$(starship init zsh)"
    ```

    </details>

    <details>
    <summary>On macOS 10.14 and lower:</summary>


    Open `~/.bash_profile` using Sublime Text:
    ```bash
    subl ~/.bash_profile
    ```
    
    Then, add this to the end of the file:

    ```bash
    export EDITOR="subl --wait"
    eval "$(starship init bash)"
    ```

    </details>

    <details>
    <summary>On Linux:</summary>


    Open `~/.bashrc` using Sublime Text:
    ```bash
    subl ~/.bashrc
    ```
    
    Then, add this to the end of the file:

    ```bash
    export EDITOR="subl --wait"
    eval "$(starship init bash)"
    ```

    </details>

5. Open a new tab in your Terminal and navigate (`cd`) to a git repository. See the pretty colors!
# Command Line 1

## Introduction

### What is the command line?
The Command Line Interface (CLI) is a way of interacting with your computer using text-based commands. This is also referred to as a Text User Interface (TUI) which is different from the way most people interact with their computers, using their mouse and a Graphical User Interface (GUI).

### Why should I use it?
Once you become comfortable with the basics, it can be a more powerful way to use your computer. You're able to do many things more quickly and *programatically*. It is especially useful if you need to do something repetitively or in bulk. Even if you never use the command line again after this class, it can help you understand how software works at a more fundamental level.

### Example Use Cases
- find all files in a folder that contain a phrase
- rename several files at the same time
- resize or crop several images or pdfs
- download a list of urls

### Anatomy of a Command
`<command> -<options> <arguments>`

* `<command>` is the action we want the computer to take. This is the program that you are running.
* `<options>` (or "flags") modify the behavior of the command
* `<arguments>` (or positional arguments) are the things we want the command to act on. They are the "inputs" to the program that you are running. 

You can view the manual for a command by typing `man <command>`. Sometimes, you can view a help page by typing `<command> --help`.

#### `df`

As an example, let's take disect the `df` (disk free) command. This command shows how much disk space is used and remaining on your computer.

If you run

```
df
```

by itself, it will show you a result that looks similar to:

```
Filesystem    512-blocks      Used Available Capacity iused               ifree %iused  Mounted on
/dev/disk1s1   488555536 438995376  33577784    93% 3186543 9223372036851589264    0%   /
devfs                411       411         0   100%     712                   0  100%   /dev
/dev/disk1s4   488555536  14681200  33577784    31%       7 9223372036854775800    0%   /private/var/vm
map -hosts             0         0         0   100%       0                   0  100%   /net
map auto_home          0         0         0   100%       0                   0  100%   /home
```

The output isn't all that readable. I don't know how to translate how "512-blocks" to gigabytes in my head.

We can use the `-h` option/flag to make the output human readable text.

```
df -h
```

The output now looks like this:

```
Filesystem      Size   Used  Avail Capacity iused               ifree %iused  Mounted on
/dev/disk1s1   233Gi  209Gi   16Gi    93% 3186562 9223372036851589245    0%   /
devfs          206Ki  206Ki    0Bi   100%     712                   0  100%   /dev
/dev/disk1s4   233Gi  7.0Gi   16Gi    31%       7 9223372036854775800    0%   /private/var/vm
map -hosts       0Bi    0Bi    0Bi   100%       0                   0  100%   /net
map auto_home    0Bi    0Bi    0Bi   100%       0                   0  100%   /home
```

We can see above that I only have 16 gigabytes remaining on my main hard drive. Yikes!

#### `ping`

Let's also disect the `ping` command. You might hear people in normal converation saying "Can you *ping* me when you're back in the office?". The word originates from this old unix command. `ping` sends packets of data to an ip address every few seconds in order to check for a response. One use case for this this command can be used to check if a website is down or not or see how quickly it responds.

In this command, we'll start by using a single position argument.

```
ping google.com
```

You can see a response that looks like:

```
PING google.com (172.217.12.142): 56 data bytes
64 bytes from 172.217.12.142: icmp_seq=0 ttl=55 time=14.140 ms
64 bytes from 172.217.12.142: icmp_seq=1 ttl=55 time=18.354 ms
64 bytes from 172.217.12.142: icmp_seq=2 ttl=55 time=12.728 ms
64 bytes from 172.217.12.142: icmp_seq=3 ttl=55 time=18.537 ms
64 bytes from 172.217.12.142: icmp_seq=4 ttl=55 time=12.509 ms
64 bytes from 172.217.12.142: icmp_seq=5 ttl=55 time=14.982 ms
64 bytes from 172.217.12.142: icmp_seq=6 ttl=55 time=11.185 ms
64 bytes from 172.217.12.142: icmp_seq=7 ttl=55 time=26.755 ms
64 bytes from 172.217.12.142: icmp_seq=8 ttl=55 time=11.612 ms
64 bytes from 172.217.12.142: icmp_seq=9 ttl=55 time=10.857 ms
64 bytes from 172.217.12.142: icmp_seq=10 ttl=55 time=13.876 ms
...
```

This command will keep going on forever sending packets of data to google.com and getting back a response each time. If we want the command to terminate after some number of iterations, we can use the `-c` count option/flag.

```
ping -c 5 google.com
```

Another option on `ping` is `-a` which makes each ping audible.

```
ping -a google.com
```

You can also have multiple options at the same time.

```
ping -a -c 5 google.com
```

This command can also be written as `ping -ac 5 google.com` as a shorthand, but make sure the 5 comes after the `-c`.

Another option that can be used with `ping` is the `-i` (interval) option. This will cause ping to wait some number of seconds between each iteration.

```
ping -ai 2 -c 5 google.com
```

You can use the `man` command to understand all the different options that can be used with `ping`.

```
man ping
```

Use your arrow keys to move up and down and press `q` to exit the man page.

Now that you have an understanding of option/flags vs. positional arguments, let's check out some other basic commands you can use on the command line.

## Basic Commands

### `whoami`
* prints your username to the terminal

### `hostname`
* prints your computer's name to the terminal

### `echo`
* prints a text string (denoted by quotes) to the terminal
* usage: `echo "Hello, World"`

### `man`
* shows you the **man**ual page - get help on how to use any command
* press `q` to quit
* usage: `man <name_of_command>`

### `uname`
* shows you the operating system name
* usage: `uname -a`

### `curl`
* downloads and shows you the source code of a website
* usage 1: `curl 'https://api.ipify.org'`
* usage 2: `curl 'http://example.org'`
* usage 3: `curl 'http://dhrumilmehta.com'`

### `clear`
* **clear**s all output from your console
* on macOS, you can also press `Ctrl+L` to clear your console while retaining history or `Cmd-K` to clear console while deleting the history. `Ctrl+L` should work on Ubuntu as well.

### ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example

1. print your username to the command line using `whoami`
2. print your computer's name to the command line using `hostname`
3. print the name of your operating system using `uname`
4. take a look at the manual page for the `uname` command. Then, use `uname` with options to:
	* print the operating system name
	* print the operating system release
	* print the operating system name and release together
	* print the machine hardware name and the processor architecture together
	* print as much information as you can all at once using `uname`.
5. print 'I did it. I'm so cool.' to the terminal using `echo`

**Bonus** 

1. print "I did it! I'm so cool!" (hint: google "escaping characters in bash")

**Protip**: Use the ↑ and ↓ arrow keys to navigate previously entered commands.

## Figuring out New Commands

### You can always check the manual page for complete documentation
for a given command, its usually either

- `man <command>`
- `<command> --help`
- or `<command> -h`

### if its not easy to figure out from there, try Google
[https://www.google.com/](https://www.google.com/)
### ...StackOverflow is also your friend
[http://stackoverflow.com/](http://stackoverflow.com/)
### also, know when to reach out to someone...
don't go down rabbit holes trying to figure something out if there is someone who knows better nearby and you've already tried the three things above, they might be able to save you a lot of stress. I'm always happy to help out.

## ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

Install the `cowsay` command

Mac: `brew install cowsay`
Ubuntu: `sudo apt-get install cowsay`

1. Make the cow say
```
1) Individuals and interactions over processes and tools 2) Working software over comprehensive documentation 3) Customer collaboration over contract negotiation 4) Responding to change over following a plan
```
2. Make a dead cow say that
3. Customize the eyes to "zz"
4. Customize the tounge to "$$" (hint: is it not displaying properly? google "escaping characters in bash")
5. Say the sentence with "zz" eyes AND "$$ toungue"
5. Make the cow's thought bubble wrap every 4 characters as it says the sentence

**Bonus** 

Make the cow into a moose

**Super Duper Bonus**

Make the cow into a fox

Hint: You'll have to install a new cow - https://raw.githubusercontent.com/paulkaefer/cowsay-files/master/cows/fox.cow

## Dangers

The terminal is a powerful tool (especially in linux)
[http://www.howtogeek.com/125157/8-deadly-commands-you-should-never-run-on-linux/](http://www.howtogeek.com/125157/8-deadly-commands-you-should-never-run-on-linux/)
# Command Line 2 

## Interacting with the Filesystem

### Intro

Just like in Finder (macOS), Explorer (Windows), or Nautilus (Ubuntu), you can navigate and manipulate files and folders in your filesystem using the command line. Each session in your terminal starts in a particular directory and you can traverse the directory structure starting from there. You can use `pwd` (print working directory) to find the current working directory.

```
pwd
```

This command gives the *absolute* path to your current working directory.

### File paths

#### Absolute Path

An **absolute path** specifies the complete path to a file or folder, ignoring your current working directory. For example, if you were to give someone "absolute" directions to your house, you would start by telling them to be on earth, then go to your continent, then go to your country, then go to your region, etc. The root of the filesystem is referred to as `/`.

#### Relative Path

A **relative path** specifies the path to a file or folder, taking into account your current working directory. For example, if you were to give someone "relative" directions to your house, you would give them directions from their current location (the relative path from where they are to where you are).

#### Special Symbols

A few directories have special symbols:

- `/` is the root of the [filesystem](https://www.tutorialspoint.com/unix/unix-file-system.htm)
- `.` current directory
- `..` parent directory
- `~` shortcut to the home directory (for me, the absolute path would be `/Users/mehtad`)

#### Example Directory Structure

Below is an example directory structure from macOS.

```
/
├── Applications
└── Users
    └── mehtad
        ├── Desktop
        ├── Development
        ├── Documents
        ├── Downloads
        ├── Movies
        ├── Music
        └── Pictures
 
```

In the example above, if I was in the Downloads folder and I wanted the relative path to the Documents folder, that would be `../Documents`.

In the same example above, the absolute path to the Documents folder would be `/Users/mehtad/Documents`.

#### ![#1589F0](https://placehold.it/15/1589F0/000000?text=+) Pop Quiz

If you are in the Downloads folder, what folder is:

- `../`
- `../../`
- `../../mehtad/`
- `../../mehtad/./`
- `../../mehtad/./Downloads/../Documents`

Notice that those were **relative** paths, the following are **absolute** paths that both refer to the same location:

- `/Users/mehtad/Downloads`
- `~/Downloads`


### Navigating Directories

##### `pwd`
**p**rints **w**orking **d**irectory (the directory you are currently in)

#### `cd`

To navigate to different directories within your filesystem, you can use the `cd` (**c**hange **d**irectory) command. `cd` takes one positional argument, the absolute or relative path to the destination directory.

```
cd <target_directory>
```

`cd ..` will move you "up" one directory (to the parent directory) and `cd ~` will move you back to the "home" directory.

#### `ls`

In order to **l**i**s**t the contents of the current directory you can use `ls`. 

* `ls -a` lists **a**ll files, including hidden files
* `ls -l` lists the files in a **l**ong format with extra information (permissions, size, last modified date, etc.)
* `ls *` also lists the contents of subdirectories (one level deep) in your working directory
* `ls <path>` lists files in a specific directory (without changing your working directory)

#### `tree`

If you don't have `tree` installed, on macOS run `brew install tree` and on ubuntu run `sudo apt-get install tree`.

* `tree` shows the files and folders in the current working directory
* `tree -L 2` recursively shows the files and directories 2 level deep from the current directory

### Inspecting Files

#### `cat`

You can view the contents of an individual file (or files) by using `cat`. `cat` will print the entire content of a file to the screen.

* usage: `cat <filename>`
* usage: `cat <filename1> <filename2> ...`

#### `head`

When a file is very long, you can use `head` to print he beginning of a file.

* `head <filename>` prints the **head** (the first 10 lines) of the file
* `head -n20 <filename>` prints the first 20 lines of the file
* This is useful for previewing the contents of a large file without opening it.

#### `tail`

In the case of long, constantly changing files, like a log file, you can use `tail`.

* `tail <filename>` prints the **tail** (the last 10 lines) of the file

#### `less`

Last, when reading long files page by page (like when using `man`), you can use `less` to paginate the contents.

* `less <filename>` allows you to page or scroll through the file
* Hit the spacebar to go down a page, use the arrow keys to scroll up and down, and hit `q` to exit.

#### `subl`

If you don't have Sublime Text installed, run `brew cask install sublime-text` on macOS and on ubuntu follow [these](http://tipsonubuntu.com/2017/05/30/install-sublime-text-3-ubuntu-16-04-official-way/) instructions.

* `subl <folder>` **open**s the folder in sublime
* `subl <filepath>` **open**s the file in sublime

#### `open` (mac only)
* `open <folder>` **open**s the Finder in the folder specified
* `open <filepath>` **open**s a url or file in the default mac program

#### `wc`
* count the number of lines and characters in a file
* `wc <path>` **w**ord**c**ount
* `wc -l <path>` only counts lines
* `wc -w <path>` only counts words. A "word" is defined as any set of characters delimited by a space.
* `wc -c <path>` only counts characters

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

1. Take some time to cd around and explore your filesystem. See what is at the root, see if you can find some of the files you use daily.
2. Navigate to `~/Desktop` and run both `ls -a` and `tree` 
3. Navigate to `~/Downloads` and run the `ls -l` command to see information about every item in that folder

**hint!** - are you lost? don't know what to type next?

- first type `pwd` to see "where you are"
- then type `ls` to see what files and folders are there
- then think about your next move, it might be `cd <path>`, where <path> is either an absolute or relative filepath for where you want to navigate to.

### Manipulating Files and Folders

The command line not only lets you navigate the file system but also manipulate it by creating new files (`touch`), creating directories (`mkdir`), deleting files and directories (`rm -i`, `rm -ir`), copying files and directories (`cp -v`, `cp -vR`), move/rename files and directories (`mv`), and more...

#### `touch`
* `touch <filename>` creates an empty file called `<filename>`
* This is useful for creating empty files to be edited at a later time.

#### `mkdir`
* `mkdir <dirname>` **m**a**k**es a new **dir**ectory called `<dirname>`

#### `rm -i`
* `rm -i <filename>` removes files in **i**nteractive mode, in which you are prompted to confirm that you really want to delete the file. It's best to always use `rm -i`
* `rm -ir <dirname>` removes a directory and **r**ecursively deletes all of its contents

#### `cp -v`
* `cp -v <filename> <new_path>` **c**o**p**ies a *file* from its current location to `<newpath>`, leaving the original file unchanged. The `-v` is for verbose mode
* `cp -vR <dirname> <new_path>` copies a *directory* **r**ecursively to `<newpath>`

#### `mv`
* `mv <filename> <new path>` **m**o**v**es a file from its current location to `<new path>`
* `mv <filename> <new filename>` renames a file without changing its location

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

In your home directory, make a folder called `Development`. This is where we will keep all of the code for the class.

1. In the `Development` folder, create a new folder called `universe` and create the following structure of files and folders.

    ```
    .
    └── solar_system
        ├── planets
        │   ├── asteroid_belt.txt
        │   ├── earth
        │   │   └── continents
        │   │       ├── africa.txt
        │   │       ├── antarctica.txt
        │   │       ├── asia.txt
        │   │       ├── australia.txt
        │   │       ├── europe.txt
        │   │       ├── north_america
        │   │       │   └── countries
        │   │       │       ├── canada.txt
        │   │       │       ├── mexico.txt
        │   │       │       └── united_states.txt
        │   │       └── south_america.txt
        │   ├── jupiter.txt
        │   ├── mars.txt
        │   ├── mercury.txt
        │   ├── neptune.txt
        │   ├── pluto.txt
        │   ├── saturn.txt
        │   ├── uranus.txt
        │   └── venus.txt
        └── stars
            └── sun.txt

    7 directories, 19 files
    ```

2. Delete asteroid belt, since that isn't a planet.

3. Move pluto to a folder called "other".

### Finding Files and Folders

#### `find`
* `find <path> -name <name>` will recursively search the specified path (and its subdirectories) and **find** files and directories with a given `<name>`
    * Use `.` for the `<path>` to refer to the working directory.
* For the `<name>`, you can search for an exact match, or use wildcard characters to search for a partial match:
    * `*` specifies any number of any characters, such as `find . -name *.py` or `find . -name *data*.*`
    * `?` specifies one character, such as `find . -name ??_*.*`

#### `grep`
* `grep <pattern> <filename>` searches a file for a **r**egular **e**xpression **p**attern and prints the matching lines
    * The pattern should be in quotation marks to allow for multiple words.
    * The pattern is case-sensitive by default, but you can use the `-i` option to **i**gnore case.
    * You can use wildcards in the filename to search multiple files, but it only searches the working directory (not subdirectories).
* `grep -r <pattern> <path>` does a **r**ecursive search of the path (checks subdirectories) for matches within files
    * Use `.` for the `<path>` to refer to the working directory.
* `grep <pattern>` does a **g**lobal search (of your entire computer) for matches
    * Hit `Ctrl + c` if you want to cancel the search.
* Much more complex string-matching patterns can be used (which we will cover in a future class).

### ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example

`find` all items in the `universe` folder with the `.txt` extension.

```
cd ~/Development/universe
find . -name "*.txt"
```

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

`find` all **folders** in the `universe` folder. use `man find` to figure out how to get folders only.

<!--
cd ~/Development/universe
find . -type d
-->

**hint**: 

The manual for the find command (`man find`) is super long. The answer is in there, but it might take a while to find. You might want to try google instead.
# 2.5 - Running Programs

Lets create and run a very small python program

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example

1. Create and "assignments" folder, navigate to it, and create an empty file called `hello.py`

    ```
    cd ~/Development
    mkdir assignments
    cd assignmets
    touch hello.py
    ```

2. Put this simple python program into hello.py

    ```python
    print("Hello, im a python program")
    ```

3. Run `hello.py`

    ```bash
    pwd
    cd ~/Development/assignments
    python3 hello.py
    ```

## ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

1. In your assignments folder, create a new python program called "aplusb.py"

    ```
    a = 5
    b = 7
    print("The sum of a and b is" + str(a + b))
    ```

2. Run this program
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

## Lets see how it works

First, lets install a new command `fortune`
- mac: `brew install fortune`
- ubuntu: `sudo apt-get install fortune`

1. Redirect: 
  ```
  fortune > wisething.txt
  ```
2. Pipe
  ```
  fortune | cowsay
  ```
3. Pipe then Redirect
  ```
  fortune | cowsay > wisecow.txt
  ```

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
# Command Line 4

## Unix

Unix (/ˈjuː.nɪks/; trademarked as UNIX) is a family of multitasking, multiuser computer operating systems that derive from the original AT&T Unix, developed starting in the 1970s at the Bell Labs research center - [https://en.wikipedia.org/wiki/Unix](https://en.wikipedia.org/wiki/Unix)

Many Unix-like operating systems have arisen over the years, of which Linux is the most popular, having displaced SUS-certified Unix on many server platforms since its inception in the early 1990s. - [https://en.wikipedia.org/wiki/Unix](https://en.wikipedia.org/wiki/Unix)

* [https://en.wikipedia.org/wiki/Unix](https://en.wikipedia.org/wiki/Unix)
* [https://en.wikipedia.org/wiki/Unix_philosophy](https://en.wikipedia.org/wiki/Unix_philosophy)
* [https://en.wikipedia.org/wiki/History_of_Unix](https://en.wikipedia.org/wiki/History_of_Unix)
* [http://www.howtogeek.com/182649/htg-explains-what-is-unix/](http://www.howtogeek.com/182649/htg-explains-what-is-unix/)

## Why learn about this?


> The rise of Linux mirrors the rise of the web, which just happens to have started around the same time. It's hard to pin down exactly how popular Linux is on the web, but according to a study by W3Techs, Unix and Unix-like operating systems power about 67 percent of all web servers. At least half of those run Linux—and probably the vast majority.
> -https://www.wired.com/2016/08/linux-took-web-now-taking-world/

1) Most programmers will be using unix-based systems
2) Many of the same principles apply to all/or the vast majority of software systems you're likely to encounter

## Operating System Concepts

* Files and Processes
	- "[Everything is a file](https://www.youtube.com/watch?v=dDwXnB6XeiA)" (oversimplification, but a useful one)
	- How does the operating system work?
		- Files! [http://www.ee.surrey.ac.uk/Teaching/Unix/unixintro.html](http://www.ee.surrey.ac.uk/Teaching/Unix/unixintro.html)
	- `ps aux` to see the processes that are running, same as opening the "activity monitor"

* Exploring the root directory (in case you're ever wondering what all those files in `/` are)
	* [https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)
	* [http://www.thegeekstuff.com/2010/09/linux-file-system-structure/?utm_source=tuicool](http://www.thegeekstuff.com/2010/09/linux-file-system-structure/?utm_source=tuicool)

## Why?

Q: Isn't this more than I need to know about computers?

A: Probably, but I want to show you that NOTHING is magic. If you ask "why" to anything, you should be able to get a straightforward answer. Learning to ask why and how can be an important management skill when it comes to tech projects in government. 


## Environment Variables and PATH

#### Evnironment Variables
Setting Environment Variables

```
export MY_VAR=1
```

Reading Environment Variables

```
echo $MY_VAR
```

Note how the environment variable is no longer defined once you exit out of the shell and reopen it. The `~/.bash_profile` file is run every time you open a shell. You can store variables that you would like to persist in there.

Check out all of your environment variables: `printenv`

* some basic ones [http://www.ee.surrey.ac.uk/Teaching/Unix/unix8.html](http://www.ee.surrey.ac.uk/Teaching/Unix/unix8.html)

#### $PATH
`$PATH` is an environment variable that specifies where the executable programs are located.

* `which echo` for example, will tell you where the echo command is located, it will be within one of the folders specified in `$PATH` otherwise you would have to call it explicitly every time as `/bin/echo`

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example: permanently setting an environment variable

Lets modify an environment variable in side your your `~/.bash_profile` (macOS) or `~/.bashrc` (Ubuntu).

1. First `touch ~/.bash_profile` (macOS) or `touch ~/.bashrc` (Ubuntu) in the terminal. This will create an empty file in your home folder if one doesn't already exist. If the file does exist, the touch command won't modify it's contents.

2. Then open your `~/.bash_profile` (macOS) or `~/.bashrc` (Ubuntu) file and place the following snippet at the bottom. This exports the environment variable PS1 which controls how your terminal display looks. All of the code inside this file is run every time you open a terminal.

	```bash
	# set EDITOR as sublime text
	export EDITOR="subl --wait"

	# Define a function that returns your current git branch
	parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
	}

	# Display present working directory and git path in bash prompt with colors
	export PS1="\u \[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $ "
	```

3. Close and reopen the terminal to see the change. Modifying the PS1 environment variable as you just did creates this nice prompt that tells you where you are as you move around directories:
	![](https://www.evernote.com/shard/s150/sh/d72e8c94-7e02-4185-b098-d89be0fbbe62/67e7c7d6f27a7790/res/0ba8eb13-4413-4ee0-8f9f-f1d211f5968a/skitch.png?resizeSmall&width=832)

4. Modify PS1 within the existing shell (instead of in the bashrc/bash_profile). Notice that since we didn't add this to the bashrc/bash_profile it doesn't persist when we open a new tab.

## Stdin & Stdout (& Stderr)
Originally I/O happened via a physically connected system console (input via keyboard, output via monitor), but standard streams abstract this. When a command is executed via an interactive shell, the streams are typically connected to the text terminal on which the shell is running, but can be changed with redirection, e.g. via a pipeline. - [https://en.wikipedia.org/wiki/Standard_streams](https://en.wikipedia.org/wiki/Standard_streams)

![](http://www.informit.com/content/images/chap5_9780133927313/elementLinks/05fig02.jpg)

source: [http://www.informit.com/articles/article.aspx?p=2273593&seqNum=5](http://www.informit.com/articles/article.aspx?p=2273593&seqNum=5)

![](http://www.informit.com/content/images/chap5_9780133927313/elementLinks/05fig03.jpg)

Figure 5-3 By default, standard input comes from the keyboard, and standard output goes to the screen

source: [http://www.informit.com/articles/article.aspx?p=2273593&seqNum=5](http://www.informit.com/articles/article.aspx?p=2273593&seqNum=5)

### Redirection
![](http://www.informit.com/content/images/chap5_9780133927313/elementLinks/05fig04.jpg)

Figure 5-4 Redirecting standard output

`command [arguments] > filename`

source: [http://www.informit.com/articles/article.aspx?p=2273593&seqNum=5](http://www.informit.com/articles/article.aspx?p=2273593&seqNum=5)

### Piping

![](https://www.evernote.com/shard/s150/sh/85196657-a9d4-4ae5-a212-225d6c51c14c/9afdbbe4f4da9789/res/57476e92-9833-4887-9e95-3f2644475598/skitch.png?resizeSmall&width=832)

source: [https://en.wikipedia.org/wiki/Pipeline_(Unix)](https://en.wikipedia.org/wiki/Pipeline_(Unix))

### and Exit Codes

Commands return exit codes when they finish running, `0`is success, `1` is fail

Get exit code of the command you just ran with the following

```
echo $?
```

Error Codes other than 1 and 0 are more rare, but here are some examples: [http://www.tldp.org/LDP/abs/html/exitcodes.html](http://www.tldp.org/LDP/abs/html/exitcodes.html])

Additional resource on exit codes:

[http://bencane.com/2014/09/02/understanding-exit-codes-and-how-to-use-them-in-bash-scripts/](http://bencane.com/2014/09/02/understanding-exit-codes-and-how-to-use-them-in-bash-scripts/)


## Permissions and `chmod`

#### Observing a file's permissions

```
ls -l
```

![](https://www.evernote.com/shard/s150/sh/e3167d0f-bb17-48dc-915f-c8fb3bc06e6d/769f5c1706fe6b35/res/2bd19ca1-fada-4833-8932-3835dfaee51c/skitch.png?resizeSmall&width=832)

![](http://linuxcommand.org/images/permissions_diagram.gif)

source: [http://linuxcommand.org/lts0070.php](http://linuxcommand.org/lts0070.php)

1. Look at permissions inside `~/Development/universe/solar_system/planets`
2. Look at permissions inside `/Applications` - notice how those are executable while the planets files are not.

#### Changing a file's permissions

`chmod` stands for "change mode", it is the command that lets you set permissions for a file

- [http://computerplumber.com/2009/01/using-the-chmod-command-effectively/](http://computerplumber.com/2009/01/using-the-chmod-command-effectively/
)
- https://en.wikipedia.org/wiki/Chmod
- https://www.cise.ufl.edu/~shray/

#### sudo (super user do)

Prepend any command with `sudo` in order to run the command as root user. Try to avoid this unless you know what you're doing. But also know that it is often the solution if you get an error telling you that you don't have the permissions to run something.

[http://unix.stackexchange.com/questions/3063/how-do-i-run-a-command-as-the-system-administrator-root](http://unix.stackexchange.com/questions/3063/how-do-i-run-a-command-as-the-system-administrator-root)

![](https://imgs.xkcd.com/comics/sandwich.png)

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example

1. Make a file called `sayhello.py` in your `assignments` folder within `~/Development`.

	```bash
	cd ~/Development/assignments
	touch sayhello.py
	```

2. Open `sayhello.py` and type the following python program:

	```python
	#!/usr/bin/env python3
	import sys
	name = sys.stdin.read()
	print("Hello " + name + "!")
	```

3. Make sayhello.py executable.

	```
	chmod +x sayhello.py
	```

4. Run this program.

	```
	echo -n "John" | ./sayhello.py
	```


## ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

This program below will add 1 to the input on STDIN.

```python
#!/usr/bin/env python3
import sys
input_number = sys.stdin.read()
print(int(input_number) + 1)
```

Save this program as a file called `add1.py`, chmod it, and execute it.

<!--
	subl add1.py
	# paste code
	chmod +x add1.py
	echo -n 10 | python3 add1.py

-->
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
# Command Line 6

## More Resources

Man/Help pages for commands

* http://conqueringthecommandline.com/book/basics
* http://cli.learncodethehardway.org/book/

Command Line Power Tools

- Ag (The Silver Searcher) - Manipulate text in the command line
https://github.com/ggreer/the_silver_searcher
http://conqueringthecommandline.com/book/ack_ag
- Sed and Awk
	- http://www.grymoire.com/Unix/Sed.html
	- http://www.hcs.harvard.edu/~dholland/computers/awk.html
- ​CsvKit - parse CSV data in the command line, transfer to sql database, JSON, and so much more.
	- ​https://csvkit.readthedocs.org/en/0.9.1/install.html​
	- https://source.opennews.org/en-US/articles/eleven-awesome-things-you-can-do-csvkit/
- UnderscoreCLI - Manipulate json data in the command line
https://github.com/ddopson/underscore-cli

* Unix Books [http://www.ee.surrey.ac.uk/Teaching/Unix/books-uk.html](http://www.ee.surrey.ac.uk/Teaching/Unix/books-uk.html)

* Command line data science: [http://datascienceatthecommandline.com](http://datascienceatthecommandline.com/)

## Credits
some information sourced from: [https://github.com/AlJohri/DAT-DC-12/blob/master/notebooks/intro-command-line.ipynb](https://github.com/AlJohri/DAT-DC-12/blob/master/notebooks/intro-command-line.ipynb)

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
# Command Line 8: Review

Review of command line material.

#### General format for commands
`<command> -<options> <arguments>`

* `<command>` is the action we want the computer to take
* `<options>` (or "flags") modify the behavior of the command
* `<arguments>` are the things we want the command to act on
For Linux and Mac users, you can get view the manual for a command by typing man <command>. For Windows users, you can view the help page by typing <command> --help.

### Basic Commands
```
whoami # your username
hostname # my computer's network name
echo "Hello, World!" # print text to terminal

man <name_of_command> # "manual" page - get help on how to use any command
```
### Navigating

```
pwd # print working directory
cd <directory> # change directory
ls # list directory
```

### Files
```
cat <filepath> # display contents of a file
touch <filepath> # create file if it doesn't already exist

mkdir <directory_path> # make directory
rm -ir <directory_path> # remove directory
cp -v <source> <destination> # copy a file or directory
mv <source> <destination> # move a file or directory
```

