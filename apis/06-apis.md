# APIs

> ... there is software that, using “APIs,”
**treats other web sites as just another part of the software infrastructure, another
function it can call to get things done.**
>
>Our computers are so small and the Web so great and vast that this last scenario
seems like part of an inescapable trend. Why wouldn’t you depend on other
web sites whenever you could, making their endless information and bountiful abilities
a seamless part of yours? And so, I suspect, such uses will become increasingly common until, one day, your computer is as tethered to the Web as you yourself are
now.
>
>\- [Swartz: Introduction](https://web.archive.org/web/20220121020916/https://www.morganclaypool.com/doi/pdfplus/10.2200/S00481ED1V01Y201302WBE005)


## How Web Apps are Structured

> The other week I made one of my rare excursions from my plushly-appointed bed
and attended a local party. There I met a man who made a website for entering
and visualizing data. I asked him whether he had an API, since it seemed so useful
for such a data-intensive site. He didn’t, he said; it would be too much work to
maintain both a normal application and an API.
>
> I tell you this story because the fellow at the party was wrong, but probably
in the same way that you are wrong, and I don’t want you to feel bad. If even well dressed
young startup founders at exclusive Williamsburg salons make this mistake,
it’s no grave sin.
> 
> See, the mistake is, that if you design your website following the principles
in this book, **the API isn’t a separate thing from your normal website, but a natural
extension of it**. All the principles we’ve talked about—smart URLs, GET and
POST, etc.—apply equally well to web sites or APIs. The only difference is that
instead of returning HTML, you’ll want to return JSON instead.
>
> \- [Swartz (Chapter 5)](https://web.archive.org/web/20220121020916/https://www.morganclaypool.com/doi/pdfplus/10.2200/S00481ED1V01Y201302WBE005)


## Resources

> “The key abstraction of information in REST is a resource. **Any information that can be named can be a resource**: a document or image, a temporal service (e.g. "today's weather in Los Angeles"), a collection of other resources, a non-virtual object (e.g. a person), and so on. In other words, any concept that might be the target of an author's hypertext reference must fit within the definition of a resource. A resource is a conceptual mapping to a set of entities, not the entity that corresponds to the mapping at any particular point in time.” - Roy Fielding’s dissertation.

### URLs (Uniform Resource Locators)

	
![](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL/mdn-url-all.png)

[https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL)



### Thinking in terms of "Resources"

#### ❇️ Example

What are the "Resources" on Crunchbase? (Lets try to map out their database, what do we think it looks like?). [https://www.crunchbase.com/](https://www.crunchbase.com/).


### What a URL reveals about a web app

> Furthermore, URLs have to last. Those t-shirts and links and blogs will
not disappear simply because you decided to reorganize your server, or move to a
different operating system, or got promoted and replaced by a subordinate (or voted
out of office). They will last for years and years to come, so your URLs must last
with them.
>
> Moreover, URLs do not just exist as isolated entities (like “http://
example.org/lunch/bacon.html”). They combine to form patterns
(“bacon.html”, “lettuce.html”, “tomato.html”). And each of these
patterns finds its place in a larger path of interaction (“/”, “/lunch/”,
“/lunch/bacon.html”).
>
> Because of all this, URLs cannot be some side-effect or afterthought, as
many seem to wish. Designing URLs is the most important part of building a web
application and has to be done first. Encoded in their design are a whole series of
implicit assumptions about what your site is about, how it is structured, and how it
should be used; all important and largely-unavoidable questions.
>
> \- [Swartz (Chapter 2:: Building for Users: Designing URLs)](https://web.archive.org/web/20220121020916/https://www.morganclaypool.com/doi/pdfplus/10.2200/S00481ED1V01Y201302WBE005)


## A Case Study

Let's take a look at https://www.fec.gov/. This is the website for the Federal Election Commission (FEC). It contains data about federal campaign finance in the United States in a format for humans to consume.

And let's look at the FEC API: [https://api.open.fec.gov/developers/](https://api.open.fec.gov/developers/). This API has the same data as the website, but in a format that computers can consume (JSON).

## Querying APIs With Python

To query an  API with python, we're going to use the `requests` library (http://docs.python-requests.org/en/master/). The `requests` library makes it very simple to run basic HTTP commands like issue a GET request and parse the response or issue a POST request.

Here is a simple example using that library to get some data on candidate H8WI01024, Paul Ryan.

```python
import requests 

url = "https://api.open.fec.gov/v1/candidate/H8WI01024/?sort=name&page=1&api_key=DEMO_KEY&per_page=20"

# Issue a GET reequest to the URL specified
response = requests.get(url)

# Parse JSON data out from the response
data = response.json()
```

### Querying the FEC API

Lets take a look at the script Ihsaan has written to hit the FEC API. You can find the script here: https://github.com/dmil/code4policy/blob/master/apis/

or pasted below:
	
```python
import requests
import json
import os
	
# base url for specific api
base_url = 'https://api.open.fec.gov/v1/'
	
# operation to execute for the api
operation = 'candidates'
	
# get key from environment variable
key = os.environ['FECKEY']
	
# additional api parameters specific to the operation
api_parameters = {'api_key': key, 'office':'H', 'sort':'name', 'state':'MA', 'election_year':[2016]}
	
# ping api
response = requests.get(base_url + operation, params = api_parameters)
	
# print status code and load returned data into json
print('Response Code: {0}\n'.format(response.status_code))
data = json.loads(response.text)
	
# save raw data
with open('fec_api_results.json', 'w') as outfile:
    json.dump(data, outfile)
	
# loop through results and print name
for candidate in data['results']:
    print(candidate['name'])
```

## JSON/XML & More about APIs

![](https://www.evernote.com/shard/s150/sh/e700e882-9ada-44b0-8f0e-aef58f2a1f39/bf14351db3d329e4/res/d4b5c513-f127-4268-b312-9af0059a9123/skitch.png?resizeSmall&width=832)

source: [https://www.infoq.com/presentations/API-design-mistakes](https://www.infoq.com/presentations/API-design-mistakes)


APIs from Programmable Web till December 2013

![](https://www.evernote.com/shard/s150/sh/d9d3e18e-8209-4ea4-ba3c-dd606a9a88d7/7ff673fe21f09207/res/28b78161-2d50-42e4-bc19-13e9b17c916c/skitch.png?resizeSmall&width=832)

![](https://www.evernote.com/shard/s150/sh/46b2d712-aad5-4098-b28d-5738102147ce/7755ad888bb941fd/res/94b12abb-fc75-496d-97e4-6a4aef5cb952/skitch.png?resizeSmall&width=832)
source: [https://www.infoq.com/presentations/API-design-mistakes](https://www.infoq.com/presentations/API-design-mistakes)

> And so the “Semantic Web Activity” at the Worldwide Web Consortium
(W3C) has spent its time writing standard upon standard...Few have received any widespread use and those that have (XML) are uniformly
scourges on the planet, offenses against hardworking programmers that have
pushed out sensible formats (like JSON) in favor of overly-complicated hairballs
with no basis in reality (I’m not done yet!—more on this in chapter 5).

[Aaron Swartz’s A Programmable Web](https://web.archive.org/web/20220121020916/https://www.morganclaypool.com/doi/pdfplus/10.2200/S00481ED1V01Y201302WBE005): Chapter 1 - Introduction: A Programmable Web

>	JSON (pronounced like “Jason”), for the uninitiated, is a simple format for
exchanging basic pieces of data between software. Originally based on JavaScript
but quickly adopted by nearly every major language, it makes it easy to share data
over the Web.

> 	Wait!, you may cry, I thought XML was for sharing data on the Web. Sadly,
you have been misled by a sinister and harmful public relations campaign. XML is
probably just about the worst format for sharing data. Here’s why:


[Aaron Swartz’s A Programmable Web](https://web.archive.org/web/20220121020916/https://www.morganclaypool.com/doi/pdfplus/10.2200/S00481ED1V01Y201302WBE005): Chapter 5 - BUILDING A PLATFORM: PROVIDING APIS 
