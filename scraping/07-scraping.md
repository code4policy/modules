# Web 7: Scraping

**Dependencies**: `pip3 install requests lxml cssselect`

## IMDB Top Rated Movies

http://www.imdb.com/chart/top

```python
#!/usr/bin/env python3

import requests
import lxml.html

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
response = requests.get("http://www.imdb.com/chart/top", headers=headers)
doc = lxml.html.fromstring(response.content)

for row in doc.cssselect('.cli-children'):
    id = row.cssselect('.cli-children .ipc-signpost__text')[0].text
    title = row.cssselect('.cli-children h3')[0].text
    rating = row.cssselect('.cli-children .ipc-rating-star--rating')[0].text
    print(id, title, rating)
```

### ➡️ Try It

Modify the script above to get the

1. year each movie was made and
2. the number of users that rated the movie
3. save the output to a CSV file


#### ❇️ Example

A quick aside....Let's set up this scraper on a cronjob using the `crontab`.

https://crontab.guru/

