# Git 7: Merge Conflicts

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example

1. 	`cd` into the universe folder and open the directory in sublime as well.

	```
	cd ~/Development/universe
	subl ~/Development/universe
	```

2. Run `git status` to make sure the repository is "clean" (i.e. there are no "untracked files", "unstaged changes", or "staged changes").

3. Run `git pull` to ensure you have the latest changes in the repository.

4. Create a branch called `blue-universe`.
	1. Modify the facts in `mars.txt` to add a new line "Mars is blue". Use `git diff` to ensure that you only modified that one line and nothing else.
	2. Commit this change to the branch.
	3. Push the branch.
	4. Create a pull request but do not merge it.

5. Check out the master branch and then create a new branch called `red-universe`.
	1. Modify the facts in `mars.txt` to add a new line "Mars is red". Use `git diff` to ensure that you only modified that one line and nothing else.
	2. Commit this change to the branch.
	3. Push the branch.
	4. Create a pull request but do not merge it.

6. Merge the `red-universe` pull request. Try to merge the `blue-universe` pull request and it should say the branch cannot be automatically merged. This mean's there is a merge conflict.

7. Create a branch called `the-upside-down`.
	1. Edit `united_states.txt` with the text: "Hawkins, Indiana: The Demogorgon was here."
	2. Commit this change to the branch.
	3. Push the branch.
	4. Do not merge this branch back in as [the upside down](http://strangerthings.wikia.com/wiki/The_Upside_Down) runs parallel to the real `universe`...

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example

1. Make sure the repository is clean and you are in the master branch.

2. Create a branch called `alternative-facts`.
 
3. Go back to the `master` branch.
	1. `git checkout master`
	1. Add two facts to `mars.txt`: "Mars has polar ice caps." and "Mars is a little more than half the size of earth."
	2. Commit these changes to `master`.

4. Go back to the `alternative-facts` branch.
	1. `git checkout alternative-facts`
	1. Add two facts to `mars.txt`. "Mars is gaseous." and "Mars is double the size of earth."
	2. Commit these changes to `alternative-facts`.
	3. Create a pull request using `alternative-facts`.

5. Attempt to merge the pull request and try to resolve the merge conflicts.


## ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

1. Get into your teams.

2. The product owner should:
	1. create a repository under their account named `demo-website`
	2. add the remaining team members as collaborators to the repo. this is done under the repo settings
	3. enable github pages on this repo with the `master` branch as the source

3. Everyone should clone the empty repository.

    ```
    git clone git@github.com:XXXXX/demo-website.git
    ```

4. The product owner should create an `index.html` and a an empty folder called `our-team`. Commit and push this change directly to the `master` branch. Here is a sample `index.html`:
	
	```html
	<!DOCTYPE html>
	<html>
	<body>

	<h1>Demo Website</h1>

	</body>
	</html>
	```

5. Everyone else should pull these changes.

    ```
    git pull
    ```

6. All team members, should create branches titled `add-member-<name>`.

	For example a team might have `add-member-rachel`, `add-member-monica`, `add-member-phoebe`, etc.

7. In this branch, each team member should create a file that is titled `our-team/<name>.html`. For example, I would create `our-team/dhrumil.html`. Add some basic information about yourself to this page. Be sure to only create this one file - there should be no other changes to the repository. It's important to keep your code changes isolated when working with git to avoid unecessary merge conflicts.
	1. Each member should:
		1. commit this change to the branch
		2. push it
		3. create a pull request
	2. Product owner should review and merge all of the PRs. There should be no conflicts.

8. The product owner should create links to each of these individal pages back into the `index.html`.

	```html
	<!DOCTYPE html>
	<html>
	<body>

	<h1>Our Website</h1>

	<ul>
	    <li><a href="our-team/rachel.html">Rachel</a></li>
	    <li><a href="our-team/monica.html">Monica</a></li>
	    <li><a href="our-team/phoebe.html">Phoebe</a></li>
	    <li><a href="our-team/joey.html">Joey</a></li>
	    <li><a href="our-team/chandler.html">Chandler</a></li>
	    <li><a href="our-team/ross.html">Ross</a></li>
	</ul>

	</body>
	</html>
	```

9. All team members should checkout the master branch and pull the latest code.

    ```
    git checkout master
    git pull
    ```

Your repository and website should look something like this:
- https://github.com/AlJohri/our-website
- http://aljohri.com/our-website/
