# Git 9: Reference

# Getting Started

1. Create a new repository on GitHub
2. **Clone** that repository locally onto your computer

	```
	git clone git@github.com:dmil/mehta-simple-website.git
	```

# Linear Workflow


1. `cd` into the folder containing your project.

	```
	cd ~/path/to/project
	```
2. Check the **status** of your **local repository** to make sure you didn't forget to commit any work.

	```
	git status
	```

3. Then **pull** the latest changes from the **remote repository** on GitHub.

	```
	git pull
	```

4. Do a discrete chunk of work on your project (lets say you added a basic FAQ page"

5. Check the status again, then **add** the files you'd like to commit to the **staging area**.

	```
	git status
	git add faq.html
	git status
	```
6. Commit with a descriptive summary of exactly what you did

	```
	git commit -m "add a basic FAQ page"
	```

7. Push that change back to GitHub

	```
	git push
	```

# Non-linear branching workflow

1. `cd` into the folder containing your project.

	```
	cd ~/path/to/project
	```
2. Check the **status** of your **local repository** to make sure you didn't forget to commit any work. Run `git branch` to see which **branch** you're on. You should ideally be on the `master` branch.

	```
	git status
	git branch
	```

3. Then **pull** the latest changes from the **master** branch of the **remote repository** on GitHub.

	```
	git pull
	```

4. Create a new branch with a descriptive name (remember the `-b` option will create a new branch, you can check out an existing branch by not using that option)

	```
	git checkout -b faq-page
	```

5. Do your work in discrete chunks. at the end of each chunk, add the file to the staging area, then commit it. Its usually a good idea to also push the latest to GitHub, although some people prefer to do that at the end.

	Do some work

	```
	git status
	git add faq.html
	git commit -m "add blank FAQ page"
	git push
	git status
	```

	Do more work

	```
	git status
	git add faq.html
	git commit -m "add information to FAQ page"
	git push
	git status
	```

	Do more work

	```
	git status
	git add faq.html
	git commit -m "fix bug"
	git push
	git status
	```

	Do more work - lets imagine this work took place across two files, an html file and a stylesheet file.

	```
	git status
	git add faq.html
	git add style.css
	git commit -m "make it look pretty"
	git push
	git status
	```

6. Once everything has been pushed to GitHub, issue a **pull request** from your branch back to the master branch.

	![](https://www.evernote.com/shard/s150/sh/271da921-4f35-4fca-ab35-7ced2b9e1faa/8364bd49b4ad8f8e/res/765ea1c4-9759-4f0f-bc5f-ba44987a4e6c/skitch.png?resizeSmall&width=832)

7. You can have a discussion on this **pull request** using GitHub's social features, and then **merge** it into the master branch when everyone agrees its a good idea to do so.

8. Finally, once the pull request has been merged into the master branch in the **remote repository** on GitHub, you'll want to get the latest version of the master branch on your local machine. Checkout the master branch locally and then pull.

	```
	git checkout master
	git pull
	```

## Additional Resources

1. If you're stuck, ask (or come to office hours). Ihsaan and I should also be on Slack.
2. Here is a video I made last year that might be of some use: https://www.youtube.com/watch?v=O4Zc8DJ9MdQ
3. Here the diagram from class ![](https://www.evernote.com/shard/s150/sh/3a1357b6-6250-432c-b5be-6bc0a895b97f/0a90b7cfc659e426/res/930e27c8-7194-484b-84f5-d411e15c2bc5/skitch.jpg?resizeSmall&width=832)