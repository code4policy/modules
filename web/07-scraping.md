# Web 7: Scraping

**Dependencies**: `pip3 install requests beautifulsoup4`

## Find the Data

- https://news.gallup.com/poll/113980/Gallup-Daily-Obama-Job-Approval.aspx
- http://polling.reuters.com/#!response/CP3_2/type/week/dates/20180301-20190115/collapsed/true
- http://data.desmoinesregister.com/iowa-caucus/candidate-tracker/index.php

## Scrape Press Pool Reports

https://kinja.com/poolreports

#### Scrape Index

```python
import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp

def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def parse_index(soup):
    post_elements = soup.select('.post-wrapper article')
    posts = []
    for el in post_elements:
        post = {
            'id': el.get('id'),
            'subject': el.select('h1 a')[0].text,
            'link': el.select('h1 a')[0].get('href')
        }
        posts.append(post)
    return posts

url = 'https://kinja.com/poolreports?startTime=1492123377164'

while True:
    print(url)
    index_soup = get_soup(url)
    posts = parse_index(index_soup)
    pp(posts)

    button = index_soup.select('.load-more__button a')
    if button:
        url = "https://publicpool.kinja.com/" + button[0].get('href')
    else:
        break
```

#### Scrape Post

```python
import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp

def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def parse_post(soup):
    return {
        'subject': soup.select('h1.headline a')[0].text,
        'body': soup.select('div.entry-content')[0].get_text(separator='\n'),
        'timestamp': soup.select('article time')[0].get('datetime'),
    }

url = 'https://publicpool.kinja.com/subject-remarks-by-president-trump-at-the-american-far-1831763583'
post_soup = get_soup(url)
post = parse_post(post_soup)

print(post['subject'])
print(post['timestamp'])
print(post['body'])
```

#### Scrape Index and Post

```python
import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp

def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def parse_post(soup):
    return {
        'subject': soup.select('h1.headline a')[0].text,
        'body': soup.select('div.entry-content')[0].get_text(separator='\n'),
        'timestamp': soup.select('article time')[0].get('datetime'),
    }

def parse_index(soup):
    post_elements = soup.select('.post-wrapper article')
    posts = []
    for el in post_elements:
        post = {
            'id': el.get('id'),
            'subject': el.select('h1 a')[0].text,
            'link': el.select('h1 a')[0].get('href')
        }
        posts.append(post)
    return posts

url = 'https://kinja.com/poolreports?startTime=1492123377164'

while True:
    print(url)
    index_soup = get_soup(url)
    posts = parse_index(index_soup)

    for post in posts:
        post_soup = get_soup(post['link'])
        final_post = parse_post(post_soup)
        final_post.update(post)
        print(final_post)

    button = index_soup.select('.load-more__button a')
    if button:
        url = "https://publicpool.kinja.com/" + button[0].get('href')
    else:
        break
```

