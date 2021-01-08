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

- **base**: almost always the master branch. this is where you are merging on to
- **compare**: this is your feature branch. this is where you are merging from

![](https://s3.amazonaws.com/media-p.slid.es/uploads/489063/images/3229907/Comparing_master___endorsement___dmil_dhrumil-simple-website.png)

In this screenshot, I am creating a Pull Request from the `endorsement` branch (compare) to the `master` branch (base). Note that this pull request has 1 commit.

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

#### Delete branch

```
git branch -d <branchname>
```


