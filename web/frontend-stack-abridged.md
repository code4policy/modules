# Front-End Stack

We'll be leaning on Mozilla's tutorials to learn the basics of HTML, CSS, and JavaScript. This is your standard front-end stack for the browser.

## HTML

* Tutorial: [https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics
)

## CSS

CSS is how you add styles to a webpage. We will dive a bit deeper into CSS later in the class, but the following will at least introduce you to the idea of CSS.

1. Paste the following into file called `styles/styles.css`:
	
	```css
	p {
	  color: red;
	}
	```
	
2. Link that stylesheet to your webpage by putting the following somewhere between `<head>` and `</head>` inside your html file:

	```html
	<link href="styles/style.css" rel="stylesheet">
	```
	
3. Make sure to commit to Git and then push to GitHub

* Tutorial: [https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)

## JavaScript

JavaScript is the programming language understood by the browser. We'll spend a little more time understanding JavaScript later in the course, for now, this will introduce you to the idea.

1. Save the following JavaScript file into `scripts/main.js`.
		
	```javascript
	// Define a Function
	function sayOuch() {
		alert('Ouch! Stop poking me!');
	}
		
	// Use a CSS selector to identify an element
	var foxImage = document.querySelector('img');
		
	// Assign the function to the onclick event on that element
	foxImage.onclick = sayOuch;
	```
2. Link the JavaScript file to the HTML file by placing the following at the **bottom** of the body section (between `<body>` and `</body>`).

	```html
	<script src="scripts/main.js"></script>
	```

3. Make sure to commit to Git and then push to GitHub

* Tutorial: [https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)