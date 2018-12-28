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

