# Git 13: FAQ

So you're lost in a sea of git.

### What should you do when you open up your terminal?

Check to see what branch you're on: <br/>
  `git branch -v`

Check to see what files have changed in your repo: <br/>
  `git status`

  * Files that have changed since your last commit will appear in red
  * Files that have changed that are staged for your next commit will appear in green

### So you're ready to push up your local changes to your remote (GitHub), what should you do?

Make sure you've staged all of your changes:
  `git status`

Add any untracked changes you'd like to include in your commit: <br/>
  `git add <file>` or `git add *` to stage all of changed files.

Commit those changes: <br/>
  `git commit -m <your wonderful commit message>`

Pull down any recent changes from your remote that may not be in your local repo: <br/>
  `git pull` or `git pull origin <branch name>`

If necessary, resolve any merge conflicts and commit those changes. Merge conflicts will appear in your files surrounded by `<<<<` and `====`. Go through and remove those brackets keep only the changes you want in your commit.

```
<<<<<<<<<<<<<<<< HEAD
This line comes from head
===================
This line comes from cool-branch
>>>>>>>>>>>>>>>>>> cool-branch
```

If you need to resolve conflicts and merge in changes from the remote you'll want to stage and commit those changes: <br/>
`git add <file>` <br/>
`git commit -m <COMMIT MESSAGE>`

Now you can push up your changes: <br/>
`git push` or `git push origin <branch name>`

### What happens when you can't push up your changes?

  ```
  MacBook-Pro-94:wiki_trust oripleban$ git push
  ERROR: Permission to xxxxxxxxx/wiki_trust.git denied to opleban.
  fatal: Could not read from remote repository.

  Please make sure you have the correct access rights
  and the repository exists.
  ```
  It could be that you don't have the right permission on the remote (GitHub)
  Make sure you are a collaborator on the GitHub repo.
  <br/>
  ```
  git push origin testbranch
  Permission denied (publickey).
  fatal: Could not read from remote repository.
  ```
  Make sure your SSH keys are [set up correctly](https://help.github.com/articles/connecting-to-github-with-ssh/).

It could be your local branch isn't tracking a remote





## Other Useful Resources
* [Github GIT Cheatsheet](https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf)
* [Oh Shit, Git!](https://github.com/AlJohri/DAT-DC-12/blob/master/notebooks/intro-git.ipynb)
* [GIT FAQ](http://gitfaq.org/)

