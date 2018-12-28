# Command Line 1

## Introduction

### What is the command line?
The Command Line Interface (CLI) is a way of interacting with your computer using text-based commands. This is also referred to as a Text User Interface (TUI) which is different from the way most people interact with their computers, using their mouse and a Graphical User Interface (GUI).

### Why should I use it?
Once you become comfortable with the basics, it can be a more powerful way to use your computer. You're able to do many things more quickly and *programatically*. It is especially useful if you need to do something repetitively or in bulk.

### Example Use Cases
- find all files in a folder that contain a phrase
- rename several files at the same time
- resize or crop several images or pdfs
- download a list of urls

### Anatomy of a Command
`<command> -<options> <arguments>`

* `<command>` is the action we want the computer to take. This is the program that you are running.
* `<options>` (or "flags") modify the behavior of the command
* `<arguments>` (or positional arguments) are the things we want the command to act on. They are the "inputs" to the program that you are running. You can view the manual for a command by typing `man <command>`. Sometimes, you can view a help page by typing `<command> --help`.

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

## ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

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

## Dangers

The terminal is a powerful tool (especially in linux)
[http://www.howtogeek.com/125157/8-deadly-commands-you-should-never-run-on-linux/](http://www.howtogeek.com/125157/8-deadly-commands-you-should-never-run-on-linux/)
