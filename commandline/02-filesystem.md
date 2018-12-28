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
.
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
