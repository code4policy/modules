## HTTP

HTML - "Hyper Text Markup Language"
HTTP - "Hyper Text Transfer Protocol"

### So what exactly is this "Hyper Text"?
https://www.w3.org/WhatIs.html
https://www.merriam-webster.com/dictionary/hypertext - see etymology

Request & Response Framework

[http://slides.com/dhrumilmehta/how-to-tell-a-story-with-data-tools-of-the-trade#/6/4](http://slides.com/dhrumilmehta/how-to-tell-a-story-with-data-tools-of-the-trade#/6/4)

[http://slides.com/dhrumilmehta/how-to-tell-a-story-with-data-tools-of-the-trade#/6/5](http://slides.com/dhrumilmehta/how-to-tell-a-story-with-data-tools-of-the-trade#/6/5)

### Which layer is it?

* HTTP is on the "application layer" of the OSI stack
* It assumes a reliable transport layer protocol (like TCP/IP)
* But maybe these acronyms are all TMI...point being - HTTP is an abstraction at the application layer

### HTTP Verbs

http://www.w3schools.com/tags/ref_httpmethods.asp

* **GET** - when you navigate to a website like `www.google.com` you're issuing a get request to google's servers. Their server then sends you back the google homepage.

* **POST** - when you fill out the google search for and hit "Search", you're issuing a "POST" request. POST requests contain a payload in the body that is not visible in the URL. That is why it is most often used to send form data to a website.

* HEAD, PUT, DELETE ... and [some others](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

### GET vs POST

GET | POST
----|-----
Requests data from a specific resource	| Submits data to be processed by a specific resource.
Data is submitted as part of the URL |	Data is submitted in the request body
Less secure but faster | More secure but slower
Can be cached by browser | Not Cached by Browser
Length Limited by URL size | MaxLength determined by server

### Representational State Transfer (REST)

So what is being "got" when you GET?... A Resource!

You'll read a little more about REST-ful webpages in your homework tonight. For now, I want to just show you an example of a REST-ful web app. Regardless of what is going on behind the scenes, a layer of REST-ful abstraction can help things make sense to an outside consumer of your content.

* Demo of the polls database.
	* Note how the URL (Universal Resource Locator) refers to a "resource".
	* I can GET a **resource** or list of resources, or I can **POST** to an **endpoint** which can trigger the creation of a resource.
	* Any kind of request can be programmed to do any kind of thing (for example POST requests can also trigger scraping in the polls database), but a well formed REST-ful web applicaiton will stick to conventions.

* A source once said to me:
> The government is just as series of CRUD applications that interact with each other.

* CRUD Apps - "CRUD apps" have four functions: **C**reate **R**ead **U**pdate **D**elete resoures. Understanding the concept of a CRUD app can help you understand REST and HTTP verbs a little better.
