# Git: Basics

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
  - `git init` creates a git repo inside current working directory. This means that this command can turn a regular folder into a git repository by generating a hidden `.git` folder that starts to keep track of changes.
  - `git clone` takes a git repo from somewhere else and makes a copy of that repo into your current working directory. We will frequently be cloning repos from GitHub.

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

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example: simple-website

Let's give it a try! We're going to **clone** a repository for a simple website fro GitHub down to our computer where we can work with it **locally**. We will make some edits to the code, **commit** those changes and then **push** the changes back up to the **remote** repository in GitHub.

https://classroom.github.com/a/IcLXBRpw
