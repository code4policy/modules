# Web 7: Scraping

**Dependencies**: `pip3 install requests lxml cssselect`

## IMDB Top Rated Movies

http://www.imdb.com/chart/top

```python
#!/usr/bin/env python3

import requests
import lxml.html

response = requests.get("http://www.imdb.com/chart/top")
doc = lxml.html.fromstring(response.content)

for row in doc.cssselect('.lister-list tr'):
    id = row.cssselect('td.ratingColumn div[data-titleid]')[0].get('data-titleid')
    title = row.cssselect('td.titleColumn a')[0].text
    rating = row.cssselect('td.ratingColumn.imdbRating strong')[0].text
    print(id, title, rating)
```

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

Modify the script above to get the

1. year each movie was made and
2. the number of users that rated the movie

## Twitter

Scrape: https://twitter.com/DataDhrumil

```python
#!/usr/bin/env python3

import requests
import lxml.html

response = requests.get("https://twitter.com/datadhrumil")
doc = lxml.html.fromstring(response.content)

for tweet in doc.cssselect("div.js-original-tweet"):

	text = tweet.cssselect('.js-tweet-text-container')[0].text_content().strip()
	retweets = tweet.cssselect('.js-actionRetweet .ProfileTweet-actionCountForPresentation')[0].text_content().strip()
	print(text)
	print("retweets = " + retweets)
	print("-------------------------------------")
```

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

Modify the script above to get the

1. number of likes for each tweet
2. number of replies for each tweet

#### ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example

A quick aside....Let's set up this scraper on a cronjob using the `crontab`.

https://crontab.guru/


## SongMeanings

http://songmeanings.com/popular/lyrics/?chart=2018-01-07

```python
#!/usr/bin/env python3

import requests
import lxml.html

response = requests.get("http://songmeanings.com/popular/lyrics/?chart=2018-01-07")
doc = lxml.html.fromstring(response.content)

table = doc.cssselect("table[summary]")[0]
for item in table.cssselect("tbody > tr.item"):
    cells = item.getchildren()
    rank = cells[0].text_content().strip()
    title = cells[1].text_content().strip()
    margin = cells[2].text_content().strip()
    print(rank, title, margin)
```
### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

1. Scrape the title and lyrics of the following song and print them to the terminal

 - https://songmeanings.com/songs/view/7354/
