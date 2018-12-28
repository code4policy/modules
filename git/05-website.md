# Git 6: Website

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example

1. Create a blank repository called `<name>-simple-website` where `<name>` is your name.
2. Navigate to your `~/Development/` folder in the terminal.
3. Clone the repository using the SSH link given to you in GitHub, it should look something like this:

	```
	git clone git@github.com:XXXXX/XXXXXXX-simple-website.git
	```
4. Create a new page called `index.html` with the `touch` command

5. In a text editor, add this simple HTML code to `index.html`.

	```html
	<!DOCTYPE html>
	<html>
	<body>

	<h1>Hello World</h1>

	</body>
	</html>
	```
6. Double click on that file to view it in a web browser (you can refresh the page to view it again after you add new code)

7. Commit to github what you have so far. Lets view it in GitHub!

## Hosting Your Website

### Static Web Server (a breif aside)

A **static web server** consists of two parts. The "assets", which are files that are served (HTML, CSS, JavaScript, Images, Text, Videos, Etc) and the "server" or the code that servers the website. We'll get into this more later in the class.

### Github Pages

GitHub also doubles as a static web server! If you enable a feature called "[GitHub Pages](https://pages.github.com/)", in addition to storing your files, GitHub will run a static web server that can serve those pages on the web.

### ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example

1. Add a heading (h1, h2) and paragraph (p) tag

	```
	<!DOCTYPE html>
	<html>
	<body>
	
	<h1>Hello,World</h1>
	<h2>My First Subheading</h2>
	
	<p>My first paragraph.</p>
	
	</body>
	</html>
	```

2. Commit this with a meaningful commit message.

	```
	git status
	git add index.html
	git commit -m "add a subhead and a paragraph"
	git status
	```

3. Push the code to github.

	```
	git push
	```

4. Go to the github repo's settings and under Github Pages choose "master" branch as the source.

	![](https://i.imgur.com/8EhdwWM.png)

5. Go to username.github.io/myname-simple-website and you should see the HTML page we created. You might have to wait a minute before it shows up.

## HTML

HTML stands for [HyperText](https://www.merriam-webster.com/dictionary/hypertext) Markup Language. 

* https://www.w3.org/WhatIs.html

The promise of HTML was originally to link text pages to one another. So lets do like the 60s and link some pages of hypertext to each other. 

### Links

https://www.w3schools.com/tags/tag_a.asp

### ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example

1. Lets create a new page called to say goodbye
	
	```
	touch goodbye.html
	```

2. Put the following code in `goodbye.html`
	
	```html
	<!DOCTYPE html>
	<html>
	<body>

	<h1>Goodbye World</h1>
	<h2>Adios</h2>
	
	<p> What a short website </p>
	
	</body>
	</html>
	```
3. Commit this page

	```
	git status
	git add goodbye.html
	git commit -m "add goodbye page"
	```

4. Lets add navigation. In `index.html` inside the body tag, lets add the following.

	```
	<a href="goodbye.html"> Goodbye Page </a>
	```
	
	and in `goodbye.html` lets add a link back

	```
	<a href="index.html"> Home Page </a>
	```
	
5. Now lets commit both of those in one commit
	
	```
	git status
	git add index.html
	git add goodbye.html
	git commit -m "add navigation links to website"
	```

6. Push to GitHub

	```
	git push
	```
	and then view it online at `username.github.io/myname-simple-website`

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It: Bullet points

The `<ul> </ul>` tag creates an "unordered list". Within it are "list items" `<li> </li>`. Here is some example code below. 

```html
<ul> 
	<li> Executive Branch </li>
	<li> Legislative Branch </li>
	<li> Judicial Branch </li>
</ul>
```
Add some bullet points to your homepage and then commit the new code to GitHub.

## Project

You should now have the tools to start building an MVP of your project. We'll plan the first sprint at the end of today. Remember the agile principles: 

> Our highest priority is to satisfy the customer through early and continuous delivery of valuable software

https://www.agilealliance.org/agile101/12-principles-behind-the-agile-manifesto/
