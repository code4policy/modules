# Project Planning

Your project will involve creating a webpage where you visualize one or more datasets in order to tell a story about or make a case for something in your area of policy interest.

In order to do this you will need to select one or more datasets and visualizations. Please make sure you have one distinct set of data and one distinct visualization minimum per team member. I ask that each team member contribute one pre-planning exercise. You may not use all of them in your final project, but this will provide you with a few options to start from.

## Find a relevant dataset

http://data.gov is a good place to start, but you're welcome to consider datasets from other places as well. Depending on the expertise on your team and your level of comfort with different data formats, it may be easiest to look for data that is either in a simple JSON structure or a CSV file.

You may also consider data that has been exposed via an API (we'll discuss these in class), however it may take a little more effort to get data out of an API compared to pre-prepared datasets.

If you're particularly ambitious, you may be able to scrape information off of a webpage and create your own dataset if it doesn't exist. This may require some extra work but could be worth the effort.

## Find an appropriate visualization

To visualize the data you've selected, we'll be using [Data Driven Documents in Javascript](https://d3js.org/) (D3JS). Lets harness the power of D3 and aim for something beyond a simple line chart or bar chart that you might build in excel. For example, if I wanted to visualize federal spending, I may consider using a treemap chart like [this one](https://bl.ocks.org/mbostock/8fe6fa6ed1fa976e5dd76cfa4d816fec) to visualize the spending in different categories.

You can find example D3 visualizations at the following places, but I'd also encourage you to google around. They're all over the internet!

- http://bl.ocks.org/mbostock (Mike Bostock created D3JS, these are his examples)
- http://bl.ocks.org/ (same website, examples by different people)
- https://d3js.org/
- http://christopheviau.com/d3list/gallery.html
- https://github.com/d3/d3/wiki/Gallery

In this course you won't be asked to create you own D3 visualization (unless you want to try!). We will however, select an example visualization, and learn enough code to tweak it to suit the needs of your dataset. You will also manipulate the data in your dataset to fit the format that the visualization requires.

This [graphic by FT Visual Journalism team](https://github.com/ft-interactive/chart-doctor/tree/master/visual-vocabulary) is a good starting point if you're not sure what type of visulization you need.

## Data manipulation

The end goal will be to take the example visualization, and feed it data to fit your needs. Start thinking about the following

### Technical Components

1. Back end

   - Collect the data at its source in either JSON or CSV, or from an API or create a dataset by coding up a web scraper.

   - To convert data into the format used by the D3 visualization, you can use the [data-converter.py](https://github.com/dmil/code4policy/blob/master/data-converter.py) script. Make sure to run `pip install pandas` in the terminal before you run it for the first time, then enter the following command in the terminal:
   ```
   python data-converter.py -f <filename> -o <output format(csv, tsv, or json)>
   ```
   
   - Write code (or find another way) to manipulate the original data into the JSON or CSV format that the visualization is looking for.

2. Front End

  - You will also need to clean up the front-end code provided in the example visualization. You will split it up into its component parts (HTML/CSS/JavaScript) in separate files.

  - You will need to arrange the charts, the text, and other components of the page (or pages) in an aesthetically pleasing way and write new styles so that your page does not look barren.

## Scrum Artifacts

You will have to submit SCRUM artifacts including but not limited to, a Trello board, a burn-down chart, and user stories as well as your reflection on your groups adherence to agile values.

## Using Github

You will collaborate on GitHub. I hope to see commits from all the team members. Branching is encouraged, forking is un-necessary.

## Examples

Here are some examples of projects from last year. I expect that the projects from this year will be a little more polished, last time we started the projects on the last day of class. However it should give you a sense of the structure your project might take on.

* https://ekrat.github.io/VT-Police/index.html
* https://srikbe.github.io/education-front-end/
* https://hkstechdevelopment.github.io/front-end-repo/

## Conclusion

More details coming soon. This should give you a general sense of what the project will be like. Each member should take some time tonight to (1) find a dataset or two (2) find a visualization or two and (3) think through what it is going to take to join that dataset to the visualization that will work best for it.
