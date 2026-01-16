# Web 7: Scraping

**Dependencies**: `pip3 install requests lxml cssselect`

## IMDB Top Rated Movies

http://www.imdb.com/chart/top

```python
#!/usr/bin/env python3

import requests

url = "https://www.imdb.com/chart/top/"

# get the page
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
response = requests.get(url, headers=headers)

# extract HTML as structured "soup"
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# get each movie (css selector is .cli-children)
movies = soup.select('.cli-children')

for movie in movies:
    # get css selctor .ipc-title from inside the movie
    title = movie.select_one('.ipc-title').get_text()
    rating = movie.select_one('.ipc-rating-star--rating').get_text()
  
    # get metadata .cli-title-metadata-item
    metadata = movie.select('.cli-title-metadata-item')
    year = metadata[0].get_text()
    print(title, rating, year)
```

### ➡️ Try It

Modify the script above to get the

1. year each movie was made and
2. the number of users that rated the movie
3. save the output to a CSV file


#### ❇️ Example

A quick aside....Let's set up this scraper on a cronjob using the `crontab`.

https://crontab.guru/

