# Git 13: FAQ

So you're lost in a sea of git.

### What should you do when you open up your terminal?

Check to see what branch you're on:
  `git branch -v`

Check to see what files have changed in your repo:
  `git status`

  * Files that have changed since your last commit will appear in red
  * Files that have changed that are staged for your next commit will appear in green

### So your ready to push up your local changes to your remote (GitHub), what should you do?

Pull down the most recent changes from your remote:
  `git pull`

If necessary, resolve any merge conflicts and commit those changes. Merge conflicts will appear in your files surrounded by `<<<<` and `====`. Go through and remove those brackets keep only the changes you want in your commit.

```
<<<<<<<<<<<<<<<< HEAD
This line comes from head
===================
This line comes from cool-branch
>>>>>>>>>>>>>>>>>> cool-branch
```

Once you resolve conflicts and merge in changes from the remote you'll want to commit your changes: <br/> `git commit -m <COMMIT MESSAGE`

### What happens when you can't push up your changes?

Your local branch doesn't have a remoe







## Other Useful Resources
* [Github GIT Cheatsheet](https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf)
* [Oh Shit, Git!](https://github.com/AlJohri/DAT-DC-12/blob/master/notebooks/intro-git.ipynb)
* [GIT FAQ](http://gitfaq.org/)

