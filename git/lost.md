# What the Git?

Help! I'm randomly typing git commands into the terminal.

Ok Ok...lets chill and take a systematic approach to this.


## Where Am I?

`pwd` **p**rint **w**orking **d**irectory

## Is this a git repository?

`ls -a` **l**i**s**ts all files and folders in this directory. `-a` sands for all (to display hidden folders too). 

You should see a folder called `.git`. If you don't, you may need to 

- Go to a differnt folder
- Clone (download) the repository you're looking to work in from GitHub
- Init - turn the folder you're in into a new git repository

## What has hapened here?
- `git branch` will show you which **branch** you're on
- `git log` will show your your **commit log** in that branch. 
 
 You can use the ↑ and ↓ arrows to look through your commit log. 
 
 Press q to quit.

## What's is happening now?

- `git status` will show you your **staging area**

	Read all the output messages thoroughly.

## Breathe

Take a few breaths and make a mental picture of what's going on.  

- What was your last commit? 
- Is your staging area empty?
- Is your local repository in sync with GitHub?

## Figure out what's next

Tell yourself what needs to be done next before typing any commands:

- Do I need to add things to the staging area? 
- Do I need to commit staged changes to the commit log? 
- Do I need to push to github? 
- Do I need to reach out for help?