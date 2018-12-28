# Git 12: Workflow

## Overall Workflow

When working with branches, here is the general workflow to adhere to.

1. Before starting work:

    ```bash
    # always start your branching from the master branch
    git checkout master
    
    # pull the latest
    git pull
    
    # create a new branch, branch-ed off of the master branch
    git checkout -b my-awesome-feature
    ```

2. Commit changes and push to your branch in GitHub regularly.

    ```bash
    
    # add files to the staging area
    git add filename1
    git add filename2
    git add filename3
    
    # commit with a descritive message
    git commit -m "descriptive message of the change i just made"
    
    # push to your branch on GitHub
    git push
    ```

3. Also make sure to periodically pull from master: 

    ```bash
    git pull origin master
    ```

    **Pulling from master periodically is very important!** This will keep your code relatively in-sync and prevent deferring massive merge conflicts down the line.

4. When you're done with your work

    ```bash
    # makes sure you've commited and pushed 
    # all the changes to your branch in GitHub
    
    git status
    ```
    
    then open up GitHub and **issue a pull request back to master**.

## Workflow Types

### Feature Branches

![](https://i.imgur.com/T6pJPY8.jpg)

The feature branch workflow is where every small or large feature gets its own branch. These branches are shortlived and are quickly merged back into master. Each feature branch corresponds to a pull request and the branch is deleted after the PR is merged.

### Team Member Branches

![](https://i.imgur.com/PDV613j.jpg)

The team member workflow is where each team member gets their own branch. These branches stay alive throughout the duration of the project and can be merged back in as frequently as you like. In this approach you can only have one PR open at a given time per team member.
