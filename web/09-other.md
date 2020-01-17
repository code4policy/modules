
## The Network Tab!

[http://money.cnn.com/2015/01/21/technology/security/obamacare-website-advertisers/](http://money.cnn.com/2015/01/21/technology/security/obamacare-website-advertisers/)

[https://www.eff.org/deeplinks/2015/01/healthcare.gov-sends-personal-data](https://www.eff.org/deeplinks/2015/01/healthcare.gov-sends-personal-data)

[https://fivethirtyeight.com/features/fandango-movies-ratings/](https://fivethirtyeight.com/features/fandango-movies-ratings/)

### Hanging out in the Network Tab

EXAMPLE
- https://news.gallup.com/poll/113980/Gallup-Daily-Obama-Job-Approval.aspx
- http://polling.reuters.com/#!response/CP3_2/type/week/dates/20180301-20190115/collapsed/true

TRY IT
- http://data.desmoinesregister.com/iowa-caucus/candidate-tracker/index.php

<!--
Gallup

Data in SVG:
https://news.gallup.com/viz/v1/xml/ad26ce43-218c-4a42-82de-ce878fa6d119/POLLFLEXCHARTVIZ/OBAMAJOBAPPR113980.aspx

Data in HTML:
<table id="tabulardata" class="mobile">
<thead>
<tr><th class="col-text">Date(s)</th><th>% Approve</th><th>% Disapprove</th></tr>
</thead>
<tbody>
<tr><td class="col-text">01/17-19/2017</td><td>59%</td><td>37%</td></tr>
<tr><td class="col-text">01/15-18/2017</td><td>58%</td><td>38%</td></tr>
<tr><td class="col-text">01/14-17/2017</td><td>57%</td><td>39%</td></tr>
<tr><td class="col-text">01/13-15/2017</td><td>57%</td><td>38%</td></tr>
<tr><td class="col-text">01/12-14/2017</td><td>57%</td><td>39%</td></tr>
<tr><td class="col-text">01/11-13/2017</td><td>58%</td><td>37%</td></tr>
<tr><td class="col-text">01/10-12/2017</td><td>57%</td><td>40%</td></tr>
<tr><td class="col-text">01/9-11/2017</td><td>57%</td><td>40%</td></tr>
<tr><td class="col-text">01/8-10/2017</td><td>55%</td><td>42%</td></tr>
<tr><td class="col-text">01/7-9/2017</td><td>56%</td><td>40%</td></tr>
</tbody></table>

Reuters
http://polling.reuters.com/api/1.4/polling/json/mean?dimension=CP3_2&daterange=20180301-20190116&compress-responses=1&account=trpoll&auth=1eeb6846e5f8be86

Des Moines Register

http://data.desmoinesregister.com/iowa-caucus/candidate-tracker/data/visits_all.json?cb=1547625985504
-->

Simple request to your simple website.
[https://dmil.github.io/dhrumil-simple-website/](https://dmil.github.io/dhrumil-simple-website/)

Modifying a facebook profile picture.

Making the Ad Go Away on FiveThirtyEight

```javascript
// get rid of top banner
document.getElementById('masterad').setAttribute('style', 'display: none !important');

// get rid of sidebar ads
for (el of document.getElementsByClassName('fivethirtyeight-sidebar-ad')) {
    el.setAttribute('style', 'display: none !important');
}
```

Modifying CSS

Modifying JavaScript


## Cookies

Types of Cookies

[https://en.wikipedia.org/wiki/HTTP_cookie#Terminology](https://en.wikipedia.org/wiki/HTTP_cookie#Terminology)

Check out the cookies on a website.

https://www.dccourts.gov/cco/maincase.jsf


### Not a cookie, but interesting
https://www.propublica.org/about/pixelping

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

Tell me everything you can find out about a website from the network tab.

- cookies
- technologies the website uses
- what takes a long time to load / large elements on page
- local storage
