## Resources for Finding D3 Examples

For your projects, the best ways to find inspirations for visualizations are to explore existing galleries and examples. Recently, many d3 visualizations 
have moved into [Observable Notebooks](https://observablehq.com/), which is a technology created by Mike Bostock (the creator of d3!) and others  
that enables collaborative environments for creating data visualizations. While Observable Notebooks are a great technology, it isn't always easy to 
transfer d3 code from notebooks into a local Javascript, HTML, CSS environment. We've listed some resources below to help with the process of reproducing
data visualizations online on your local devices, either through pure d3 examples or through Observable notebooks.


1. [D3.js Graph Gallery](https://d3-graph-gallery.com/index.html)

    Great website for exploring simple d3 visualizations! The code is nicely divided into HTML and Javascript, and you can even change the code on the wesbite
    to see changes directly from the browser. Note that the data source for these visualizations are often in the following format:

        // get the data
        d3.csv("https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/data_doubleHist.csv", function(data)
  
    When using these visualizations, make sure that your own data matches the same format as the csv file in the link. You can replace the link with your
    own local csv file to visualize different datasets.

2. [D3.js Gallery by Christophe Viau](https://christopheviau.com/d3list/gallery.html)

    Most of the examples on this website are all in pure d3, with the Javascript, d3, CSS code all contained within the `index.html` file. 
    Once you are able to get the visualization to render, we recommend that you split your code into separate Javascript, HTML, and CSS files for 
    best practice.

3. [Observable Gallery](https://observablehq.com/@d3/gallery)
    
    Although the Observable Gallery contains many great visualization examples, it is not recommended to try and translate Observable code to Javascript: 
    the process can be involved and time-consuming if you don't know what parts of the code to change.
