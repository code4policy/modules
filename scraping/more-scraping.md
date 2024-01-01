# Web 8: More Scraping

**Dependencies**: `pip3 install requests beautifulsoup4`

## Scrape Press Pool Reports

https://kinja.com/poolreports

#### Scrape Post

```python
import requests
from bs4 import BeautifulSoup

def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def parse_post(soup):
    return {
        'subject': soup.select('header h1 a')[0].text,
        # extract text out of all child elements
        'body': soup.select('div.js_post-content')[0].get_text(separator='\n'),
        'timestamp': soup.select('main time')[0].get('datetime'),
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
        'subject': soup.select('header h1 a')[0].text,
        # extract text out of all child elements
        'body': soup.select('div.js_post-content')[0].get_text(separator='\n'),
        'timestamp': soup.select('main time')[0].get('datetime'),
    }

def parse_index(soup):
    links = []
    for el in soup.select('a.js_link h2'):
        link = el.parent.get('href')
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

    if len(posts) > 100:
        break

    # check if load more button exists
    button = index_soup.select('div.row a.js_link button.button')
    if button:
        # get url from the load more button
        url = "https://publicpool.kinja.com/" + button[0].parent.get('href')
    else:
        # exit the loop if we reached the last page
        break

with open('posts.json', 'w') as f:
    json.dump(posts, f)
```
