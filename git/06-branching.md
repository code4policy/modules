# Git: Branching

## Why branches?

When using Git, branches are a part of your everyday development process. Git branches are effectively a pointer to a snapshot of your changes. When you want to add a new feature or fix a bug—no matter how big or how small—you spawn a new branch to encapsulate your changes. This makes it harder for unstable code to get merged into the main code base, and it gives you the chance to clean up your future's history before merging it into the main branch.

There are many different use cases for branches ranging from the aforementioned "feature branches", "release branches", dev/test/qa branches, and more.

## How do branches work?

When creating a new repository, git by default starts with a `master` branch which is what we have been using until now. When we create branches, we are branching *off of* the most recent commit on the master branch.

![](https://wac-cdn.atlassian.com/dam/jcr:746be214-eb99-462c-9319-04a4d2eeebfa/01.svg)

The diagram above visualizes a repository with two isolated lines of development, one for a little feature, and one for a longer-running feature. By developing them in branches, it’s not only possible to work on both of them in parallel, but it also keeps the main master branch free from questionable code.

After developing a feature, it needs to be merged back into the master branch. We will do this using a [Pull Request](https://help.github.com/articles/about-pull-requests/).

## How does merging work?

![](https://wac-cdn.atlassian.com/dam/jcr:86eba9ec-9391-45ea-800a-948cec1f2ed7/Branch-2.png)

When creating a branch, the head of the branch splits off of a common base as seen in the picture above. This is why we refer to Git as a *non-linear workflow*. There are three new commits on the feature branch and 2 new commits directly on the master branch.

![](https://wac-cdn.atlassian.com/dam/jcr:83323200-3c57-4c29-9b7e-e67e98745427/Branch-1.png)

When come time to merge, the difference between the 2 new commits on the master branch and the new code in the feature branch is resolved in what is referred to as a **merge commit**. Git tries to be as smart as possible when merging code but occasionally there are changes that cannot automatically be merged. This is when we run into a **merge conflict**. We will talk more about this in detail.

Sources:

- https://www.atlassian.com/git/tutorials/using-branches
- https://www.atlassian.com/git/tutorials/using-branches/git-merge

## Pull Requests

While there are other ways to merge branches, we will be using pull requests. When using the [shared repository model](https://help.github.com/articles/about-collaborative-development-models/) (one repository, multiple collaborators), 

- **base**: almost always the `main` branch. this is where you are merging on to
- **compare**: this is your feature branch. this is where you are merging from

<img width="2372" height="1635" alt="image" src="https://github.com/user-attachments/assets/34074b43-1604-4b01-8ca2-5a115d965d25" />

In this screenshot, I am creating a Pull Request from the `instructor-config-file` branch (compare) to the `main` branch (base). Note that this pull request has 1 commit.

## Commands

#### List Branches

```
git branch
```

#### Create (and switch to) a new branch

The `-b` flag creates a new branch.

```
git checkout -b <branchname>
```

#### Switch branch

```
git checkout <branchname>
```

## ➡️ Try It

1. Get into your teams.

2. The product owner should:
	1. create a repository under the `code4policy` account named `demo-website` (or use your project website!)
	2. add the remaining team members (and the prof and the TA) as collaborators to the repo. this is done under the repo settings
	3. enable github pages on this repo with the `master` branch as the source

3. The product owner should create an `index.html` and a page called `our-team/index.html`. Commit and push this change directly to the `master` branch. 

	Here is a sample `index.html`:
	```html
	<!DOCTYPE html>
	<html>
	    <head>
	        <title>Demo Website</title>
	    </head>
	    <body>
	        <h1>Our Demonstration Website</h1>
	        <a href='our-team/index.html'>Learn more about our team</a>
	    </body>
	</html>
	```


	Here is a sample `our-team/index.html`:
	
	```html
	<!DOCTYPE html>
	<html>
	    <head>
	        <title>Demo Website</title>
	    </head>
	    <body>
	        <h1>About Us!</h1>
	    </body>
	</html>
	```

4. Everyone should clone the repository.

    ```
    git clone git@github.com:XXXXX/demo-website.git
    ```

5. All team members, should create branches titled `add-member-<name>`. For example, I would do:

  ```
  git checkout -b add-member-dhrumil
  ```

6. In this branch, each team member should edit `our-team/index.html` and add some basic information about yourself to this page. Be sure to only create this one file - there should be no other changes to the repository. It's important to keep your code changes isolated when working with git to avoid unecessary merge conflicts.
	1. Each member should:
		1. commit this change to the branch
		2. push it
		3. create a pull request
	2. Product owner should review and merge all of the PRs. There should be no conflicts.


8. All team members should checkout the master branch and pull the latest code.

#### Deleting a branch locally

```
git branch -d <branchname>
```


