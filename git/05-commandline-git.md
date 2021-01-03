# Git from the Command Line

Let's practice using Git from the command line.


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
3. run `pwd` and `ls` to remind yourself where you are and what is there.
4. Change to the folder with day 1 homework (https://classroom.github.com/a/ciZOS9c2). Your shell prompt (`PS1`) should show that we are now in a git repository.

	```
	git status
	git log
	```


## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example: universe

1. cd into your directory `~/Development/universe`
2. run `pwd` and `ls` to remind yourself where you are and what is there.
3. Change to the folder with day 1 assignment on folder structure (https://classroom.github.com/a/wtsFvR6p). Your shell prompt (`PS1`) should show that we are now in a git repository.

	```
	git status
	git log
	```

4.  Create `visitors/oumuamua.txt` and add it

	```
	git add visitors/oumuamua.txt
	git status
	git log
	```

5. commit

	```
	git commit -m "add visitors"
	git status
	git log
	```

6. push your commit

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
