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
	git commit -m "add day 1 class work"
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
