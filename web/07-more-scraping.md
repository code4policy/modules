# Web 7: Scraping

**Dependencies**: `pip3 install requests beautifulsoup4`

## Scrape Press Pool Reports

https://kinja.com/poolreports

#### Scrape Index

```python
import json
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

posts = []
while True:
    print(url)
    index_soup = get_soup(url)
    posts += parse_index(index_soup)

    # check if load more button exists
    button = index_soup.select('.load-more__button a')
    if button:
        # get url from the load more button
        url = "https://publicpool.kinja.com/" + button[0].get('href')
    else:
        # exit the loop if we reached the last page
        break

with open('index.json', 'w') as f:
    json.dump(posts, f)
```

#### Scrape Post

```python
import requests
from bs4 import BeautifulSoup

def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def parse_post(soup):
    return {
        'subject': soup.select('h1.headline a')[0].text,
        # extract text out of all child elements
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
import json
import requests
from bs4 import BeautifulSoup

def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def parse_post(soup):
    return {
        'subject': soup.select('h1.headline a')[0].text,
        # extract text out of all child elements
        'body': soup.select('div.entry-content')[0].get_text(separator='\n'),
        'timestamp': soup.select('article time')[0].get('datetime'),
    }

def parse_index(soup):
    link_elements = soup.select('.post-wrapper article h1 a')
    links = []
    for el in link_elements:
        link = el.get('href')
        links.append(link)
    return links

url = 'https://kinja.com/poolreports?startTime=1492123377164'

posts = []
while True:
    print(url)
    index_soup = get_soup(url)
    links = parse_index(index_soup)

    # loop through links of posts on current page
    for link in links:
        print(link)
        post_soup = get_soup(link)
        post = parse_post(post_soup)
        posts.append(post)

    # check if load more button exists
    button = index_soup.select('.load-more__button a')
    if button:
        # get url from the load more button
        url = "https://publicpool.kinja.com/" + button[0].get('href')
    else:
        # exit the loop if we reached the last page
        break

with open('posts.json', 'w') as f:
    json.dump(posts, f)
```
