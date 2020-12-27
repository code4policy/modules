# Git

> Git (/ɡɪt/[8]) is a version control system (VCS) for tracking changes in computer files and coordinating work on those files among multiple people. It is primarily used for source code management in software development,[9] but it can be used to keep track of changes in any set of files. As a distributed revision control system it is aimed at speed,[10] data integrity,[11] and support for distributed, non-linear workflows.[12]
> -Wikipedia


> Git is an open source program for tracking changes in text files.
> -GitHub (https://help.github.com/articles/github-glossary/)

## What is Git?

Keeping track of file versions is hard.

![](http://petapixel.com/assets/uploads/2015/07/psdrevisioning.jpg)

### So what is Git, and why does it help us?
Above all else, Git is a fast and **distributed** version control system, that allows you to efficiently handle projects large and small.

Here are some problems we face as developers, and how git solves them:

#### Reverting to past save points (commits)

Git allows us to make save points at any time. These save points are called 'commits'. Once a save point is made, it's permanent, and allows us to go back to that save point at any time. From there, we can see what the code looked like at that point, or even start building off that version.

![](../assets/commits1.jpg)

#### Keeping track of what each save point 'meant' (commit messages)

Every commit has a description (commit message), which allows us to describe what changes were made between the current and previous commit. This is usually a description of what features were added or what bugs were fixed.

Additionally, git supports tagging, which allows us to mark a specific commit as a specific version of our code (e.g. '2.4.5').

![](../assets/commitmessages.jpg)


#### Comparing changes to past save points (diff)

It's often important to see content of the actual changes that were made. This can be useful when:

* tracking down when and how a bug was introduced
* understanding the changes a team member made so you can stay up-to-date with progress
* reviewing code as a team for correctness or quality/style

Git allows us to easily see these changes (called a `diff`) for any given commit.

#### Non-linear workflow (branches)

Git enables you to work using a non-linear workflow. This means that you can have multiple versions of a project or "branches" with different save points, or "commits", simultaneously within the same folder and easily toggle bgttween them. You can split new branches off a project when you're looking to experiment or implement a new feature, and you can merge those branches back into the main (formerly known as "master") branch when you're ready to incorporate them into a project.

![](https://wac-cdn.atlassian.com/dam/jcr:746be214-eb99-462c-9319-04a4d2eeebfa/01.svg?cdnVersion=1386)

#### Fearlessness in making changes

In developing software, we often want to experiment in adding a feature or
refactoring (rewriting) existing code. Because git makes it easy to go back to a
known good state, we can experiment without worrying that we'll be unable to
undo the experimental work.

## Git versus GitHub

* **Git** is a distributed version control system. It is a technology.

	![](../assets/git.png)

* **GitHub** is a social coding platform where git repositories are stored and where people can collaborate on projects. GitHub is great both for collaboration within your organization, but also provides an excellent model for open source collaboration across organizations or with the public. We do both of these here at FiveThirtyEight.

	![](../assets/github.png)


* On **GitHub** you can find **Git** repositories. 

	![](../assets/git-notequal-github.png)

Learn More: https://jahya.net/blog/git-vs-github/

## Some Vocabulary

The basics:

* **Git** - version control software
* **Repository** - a folder containing your files and also containing a structure that helps keep track of changes in those files. When you intialize a repository, git creates a hidden folder (`.git` folder) that stores the changes to those files.
* **Commit** - the basic unit of a git repository is a commit. It is a set of changes to a file. A commit usually comes with an id as well as a **commit message** that describes the change.

Working with others:

* **GitHub** - a place to host git repositories and collaborate
* **Local Repository** - the version of a git repository on your local computer
* **Remote Repository** - the version of a git repository stored somewhere else that your local repository is connected to (frequently on GitHub)


## Git and GitHub for things other than code
* Auditing system for changes on a file
* For collaboratively editing a text document
* [For drafting government web design standards!](https://github.com/18F/web-design-standards)
* Open [comment period](https://github.com/whitehouse/source-code-policy/issues?q=is%3Aissue+is%3Aclosed) for policy
* [Drafting](https://github.com/twitter/innovators-patent-agreement) and [collaborating on](https://github.com/twitter/innovators-patent-agreement/issues) legal documents
* Design (image diff) 
	* https://help.github.com/articles/rendering-and-diffing-images/
* Open journalsim showcase
	* 	https://github.com/showcases/open-journalism
* Github for Government
	* https://government.github.com/
	* https://government.github.com/community/

