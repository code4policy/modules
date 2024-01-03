# Git from the Command Line

Let's practice using Git from the command line.


## ❇️ Example: fruit-basket

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

## ❇️ Example: universe

1. cd into your directory `~/Development/universe`
2. run `pwd` and `ls` to remind yourself where you are and what is there
3. double check to make sure there are no untracked changes, or tracked changes in the "staging area" that haven't been committed yet. Take a look at the commit log. Build a mental model of what your repository looks like. Then, run a git pull just in case, to grab any new changes from GitHub that you're missing.

	```
	git status
	git log
	git pull
	```
4.  open `mars.txt` in sublime text and add a new fact to it about mars and save the file

5.  add that change to the staging area. But first, glance at your staging area (`git status`) and your commit log (`git log`) to update your mental model

	```
	git status
	git log
	git add solar_system/planets/mars.txt
	```

5. Glance at your staging area (`git status`) and your commit log (`git log`) again to update your mental model. Now commit those changes.

	```
	git status
	git log
	git commit -m "add mars"
	```

6. push your commit

	```
	git push
	```

	and check your repository online by refereshing the page in github
	
## ➡️ Try It

<!-- OLD INSTRUCTIONS
1. Add `venus.txt` and commit it with the message "add venus".
2. Add `jupiter.txt` and `uranus.txt` and commit it with the message "add jupiter and venus".
3. Add the rest of the `planets` folder and commit it with the message "add remaining planets".
4. Add the rest of the `stars` folder and commit it with the message "add stars".
5. Run `git status` to check for any more "untracked files". Add the remaining files and commit them.
5. Push these commits to github.
-->

Repeat the steps above 3 times, each time for a different planet

**bonus** 

Try making a commit that involves changing multiple files (do two planets in the same commit)

