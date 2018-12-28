# Basics

## Client vs Server

Basic Network
![](https://mdn.mozillademos.org/files/8973/Client-server.jpg)
Source: [Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)

* **Client** - you using your web browser on your computer, phone, smartwatch,etc...
* **Server** - computers that store and serve up webpages, sites, apps etc...

## Lets Zoom In

The term "server" can sometimes be used ambiguously, it can refer the **software** that is serving the data or the **hardware** (the actual device) that is running that software.

### Static Web Server
![](https://mdn.mozillademos.org/files/8659/web-server.svg)
Source: [Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_web_server)

#### ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example

Setting up a local server:

```
cd ~/Development/Harvard/simple-website
python2 -m SimpleHTTPServer 8000
```

Navigate to `http://localhost:8000/` in your web browser

#### Localhost

* `127.0.0.1` or `localhost` resolves to *This Computer* (try running `cat /etc/hosts` in terminal)
* `0.0.0.0` will also work. It means something slightly different, but we won't get into that. If you want to know, do some googling! There are some decent explanations on stackoverflow.


#### ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example
	
Part of the beauty of the web is that any node can be a server. You don't need special hardware. Your computer, your watch, your raspberry pi, your fridge - with the right programming, any one of them can be a server. I will temporarily open the website that python is serving to `localhost` from my computer to the internet securely using a service called [ngrok](https://ngrok.com/).


#### Ports

Notice the example above navigates to the IP address `0.0.0.0` and port `8000`. A **port** is like an extention to a telephone number. Once you've hit the IP address of the correct server, it may be serving different traffic through different ports. The default port for HTTP traffic is port `80`, however you can serve a website through any port you'd like.

Here is a [list of common port numbers](https://en.wikipedia.org/wiki/Port_(computer_networking)#Common_port_numbers), it would be best to avoid serving a website through any of these.

#### ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example

Get the IP address for a website.

```
dig google.com +short
```

Then you can plug that IP into the browser with a port. `XXX.XXX.XXX.XXX:80` will take you to that website's homepage, but another port `XXX.XXX.XXX.XXX:9100` for example, will error out.


* https://en.wikipedia.org/wiki/Port_(computer_networking)#Common_port_numbers

If you're just testing a website, its a good idea to use a higher number (like `8000` or `8080`, at FiveThirtyEight we use port `5380`) so that it doesn't conflict with other kinds of traffic. Most websites in production will be served on port `80` (that's where browsers look for it by default).


## Static vs Dynamic Web Servers

### Static Web Server
![](https://mdn.mozillademos.org/files/13841/Basic%20Static%20App%20Server.png)
Source: [Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Introduction)

A static web server simply serves files.

### Dynamic Web Server
![](https://mdn.mozillademos.org/files/13839/Web%20Application%20with%20HTML%20and%20Steps.png)

Source: [Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Introduction)

A dynamic web server might do a lot of things. Check to see if you're logged in, get personalized information, communicate with a database, communicate with other web applications etc.

#### Serve Side (backend) Frameworks

Web frameworks are often used to organize code on a dynamic server. Some examples include: 

* **Ruby**: Ruby on Rails, Sinatra
* **Python**: Django, Flask
* **JavaScript (NodeJS)**: Express, Koa, ...
* Others you may have heard of (like ASP.NET) https://en.wikipedia.org/wiki/Comparison_of_web_frameworks

#### Client Side (frontend) Frameworks

* **Javascript**: React, Angular, Backbone, Ember ...

#### ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example

 * Polls Frontend [1](https://projects.fivethirtyeight.com/trump-approval-ratings/) [2](https://projects.fivethirtyeight.com/congress-generic-ballot-polls/) (HTML, CSS, JavaScript)
 * Polls Backend [URL Redacted] \(Ruby on Rails\)
