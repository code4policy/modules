# The `.DS_Store` file in MacOS

If you are a Mac user, you may have noticed that your computer sometimes creates files called `.DS_Store` which are visible when you run `ls -a` or `git status`.

## What are these files?

Mac creates the `.DS_Store` files in each folder to store information about how the icons in that folder should be displayed. It is a hidden folder (becuase it starts with a `.`) which means that it doesn't appear in the finder, or when you run an `ls`, but it is there. You can see it by running `ls -a`.

## Why do i care?

The `.DS_Store` file can cause conflicts if they end up in your git repository, especially when you're working on a project with other mac users.

## What should I do?

Try not to commit `.DS_Store` files to your GitHub repos.

Here is one way to make sure git always ignores the `.DS_Store` file so that you remove the possibility of accidentally committing it to a repo. 

**One member** of your team can create a file called `.gitignore`, which tells git to ignore certain files or file types. 



1. `cd` into the folder containing your project (the folder must be a git repository). Make sure you're on the master branch and that all changse so far have been committed. `git status` should show the staging area is empty.

2. Add the `.gitignore` file

	```
	touch .gitignore
	echo ".DS_Store" > .gitignore
	git add .gitignore
	git commit -m "make git ignore .DS_Store files"
	```
	
That's it. Git will now always ignore the `.DS_Store` file in that repository.