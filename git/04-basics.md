# Git 4: Basics

## Some Vocabulary

* **Git** - version control software
* **Repository** - a folder containing your files and also containing a structure that helps keep track of changes in those files. When you intialize a repository, git creates a hidden folder (`.git` folder) that stores the changes to those files.
* **GitHub** - a place to host git repositories and collaborate
* **Local Repository** - the version of a git repository on your local computer
* **Remote Repository** - the version of a git repository stored somewhere else that your local repository is connected to (frequently on GitHub)
* **Commit** - the basic unit of a git repository is a commit. It is a set of changes to a file. A commit usually comes with an id as well as a **commit message** that describes the change.

Within a Repository you have

* **Untracked Changes** - files that are in your folder but that git doesn't pay attention to.
* **Staging Area** - a place where you can put files before you commit them. Once files are in the staging area, git is paying attention to them.
* **Commit Log** (aka Git History) - all of the commits (previous changes) to all of the files in your repository.

## Components of a Git Repository

![](https://www.evernote.com/shard/s150/sh/3a1357b6-6250-432c-b5be-6bc0a895b97f/0a90b7cfc659e426/res/930e27c8-7194-484b-84f5-d411e15c2bc5/skitch.jpg?resizeSmall&width=832)

1. The working directory
  - `git init` creates a git repo inside current working directory

2. The staging area
  - `git add .` adds changes from the working directory to the staging area
  - `git add <filename>` adds changes to filenames specified from the working directory to the staging area

3. The commit
  - `git commit -m "commit message"` adds changes in staging area to the repository
  - `git log` shows

**Protip**: Run `git status` after each command in the beginning because it allows you to visualize what just happaned.

## Github

* Your Github Page
* Social Features

#### Key Terms
* **github** - a service that hosts git remote repositories, and provides a web app to interact / collaborate on them
* **remote** - another repository that can be syncronized with a remote
* **upstream** - the name for a remote read-only repository
* **origin** - the name for a remote read-and-write repository
* **clone**  - download an entire remote repository, to be used as a local repository
* **fetch**  - downloading the set of changes (commits) from a remote repository
* **pull**   - fetching changes and merging them into the current branch

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example: fruit-basket

1. Create 🍒🍎🍌🍇🍑🍉🍍 basket

	```
	cd ~/Development/
	mkdir fruit-basket
	cd fruit-basket

	echo "i am cherry" > cherries.txt
	echo "i am a strawberry" > strawberries.txt
	echo "i am a watermelon" > watermelons.txt
	```

2. Initialize repository

	```
	git init

	git status
	git log
	```

5. Add the fruits to the staging area.

	```
	git add cherries.txt
	git add strawberries.txt
	git add watermelons.txt

	git status
	git log
	```

6. Create a commit.

	```
	git commit -m "add cherries, strawberries, and watermelons"

	git status
	git log
	```

7. Create a [blank github repo](https://github.com/new) called "fruit-basket".

8. Set your remotes (follow the instructions in the new github repository, it should look something like below).
	
	```
	git remote add origin git@github.com:XXXXX/XXXXX.git
	git push --set-upstream origin master
	```

8. Push the commit.

	```
	git push

	git status
	git log
	```

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example: assignments

1. Backup the `assignments` directory.
2. cd into your directory `~/Development/assignments`
3. run `pwd` and `ls` to remind yourself where you are and what is there
4. intitialize a git repository in the folder. Your shell prompt (`PS1`) should also show that we are now in a git repository.

	```
	git init
	git status
	git log
	```

5. Add day 1 homework to the staging area.

	```
	git add sayhello.py
	git add expensive_water.csv
	git add expensive_water_summary.txt
	git add description.txt
	git add output.csv
	git add summary.txt
	git status
	git log
	```

6. commit
	
	```
	git commit -m "add day 1 homework"
	git status
	git log
	```

7. create a [blank github repo](https://github.com/new) called "assignments"
8. set your remotes (follow the instructions in the new github repository, it should look something like below)

	```
	git remote add origin git@github.com:<username>/<repo>.git
	git push --set-upstream origin master
	```

9. push your commits

	```
	git push
	```

10. check if the code is pushed online

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example: universe

1. cd into your directory `~/Development/universe`
2. run `pwd` and `ls` to remind yourself where you are and what is there
3. intitialize a git repository in the folder

	```
	git init
	git status
	git log
	```

4.  add mars.txt

	```
	git add solar_system/planets/mars.txt
	git status
	git log
	```

5. commit

	```
	git commit -m "add mars"
	git status
	git log
	```

6. add earth

	```
	git add solar_system/planets/earth
	git status
	git log
	```

7. commit

	```
	git commit -m "add earth"
	git status
	git log
	```

8. create a [blank github repo](https://github.com/new) called "universe"

9. set your remotes (follow the instructions in the new github repository, it should look something like below)
	
	```
	git remote add origin git@github.com:XXXXX/XXXXX.git
	git push --set-upstream origin master
	```

10. push your 2 commits

	```
	git push
	```

11. check your repository online by refereshing the page in github

## ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

1. Add `venus.txt` and commit it with the message "add venus".
2. Add `jupiter.txt` and `uranus.txt` and commit it with the message "add jupiter and venus".
3. Add the rest of the `planets` folder and commit it with the message "add remaining planets".
4. Add the rest of the `stars` folder and commit it with the message "add stars".
5. Run `git status` to check for any more "untracked files". Add the remaining files and commit them.
5. Push these commits to github.

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example: cloning and pulling

1. Clone code4policy repository.

	```
	git clone git@github.com:dmil/code4policy.git
	```

2. Dhrumil will now push a commit.

3. Run `git pull` followed by `git log` to see the new commits.

## Git vs Github

<!-- TODO: integrate stuff from intro.md - git vs github -->

Git is a _distributed_ version control system (VCS). Distributed means that there is no one central server that stores all of your code- you can have redundancies (copies) of the code wherever you like. There is always one copy of the code (along with its entire history) on your local computer. Other copies of your code are each referred to as "remotes". Github.com is a *very* popular remote used for Git projects such as it is almost synonymous with Git now. There are of course other alternatives such as [BitBucket](https://bitbucket.org/) and [GitLab](https://about.gitlab.com/).
