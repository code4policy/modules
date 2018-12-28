# Project

Please find below a description of expectations for your final project.

## Product

For your final project, you will work in a scrum-inspired agile software team with your classmates to tell a data-driven story about a particular area of policy interest. Your team will select one or many datasets, and create a web application with visualizations that tell a coherent story about your data.

### Selecting Data

You are welcome to select data from any data source, as long as you are able to understand the format that the data is in and transform it into a format that works for the visualization that you would like to build.

### Selecting a visualization

As we mentioned in class, [D3JS](https://d3js.org/) (Data Drivien Documents) is not a "charting library", but rather a language in which graphics are written. For this reason there are many examples of D3 graphics out in the wild for you to pull from, and data visualization professionals are adding new ones every day. 

Find a visualization that does a good job explaining to the reader the point you're hoping to make given the dataset you have selected. Remember, D3 gives you lots of options that include interactivity and creative visualization. Here are some example D3 visualizations:

- http://bl.ocks.org/mbostock (Mike Bostock created D3JS, these are his examples)
- http://bl.ocks.org/ (same website, examples by different people)
- https://d3js.org/
- http://christopheviau.com/d3list/gallery.html
- https://github.com/d3/d3/wiki/Gallery


### Your Dataset

We're **not** going to have a proper "back end" server that pulls from a database and serves up an API. Rather, you will find a dataset and place it in a folder within your repository.

For each dataset you should have:

- a copy of the original data in the format you got it in
- a `README.md` or `README.txt` file with a link to the original data source and an explanation about how you transformed the original data into the final format you needed. If you've done the transformation using a python script, just uplaod that script (no need to document). If you used some other means, please document your data transformation process in the README file. It should be a step by step explanation, not just one pithy sentence like "I transformed the data with excel".
- a copy of the final data which will be consumed by the visualization

Remember, sometimes you might be able to tell a better story by filtering the data down to an interesting subset rather than visualizing all of it.

### Chosing a visualizaiton

You can find example D3 visualizations at the following places, but I'd also encourage you to google around. They're all over the internet!

- http://bl.ocks.org/mbostock (Mike Bostock created D3JS, these are his examples)
- http://bl.ocks.org/ (same website, examples by different people)
- https://d3js.org/
- http://christopheviau.com/d3list/gallery.html
- https://github.com/d3/d3/wiki/Gallery

In addition to modifying the data, I am asking that you make at least one small modification to the demo code provided to you. It can be something as simple as modifying a color, or something more ambitious if you chose.

### File Structure

The front end will contain HTML, CSS, and JavaScript. I will expect each component to be in a separate file.

Your code should also be organized in a meaningful way. One example would be Mozilla's recommended file structure where all the JavaScript is in one folder, all the CSS in another, all the data in another: 

* https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/Dealing_with_files

Another possible structure is the one you see in this example repo: 

* https://github.com/dmil/example-project

You're welcome to use a different file structure, but there should be some consistancy in the way your files are named and organized. Try to make sure that URL's are meaningful in the context of your application, and also that it is clear from the filenames which page each CSS, JavaScript, and data files map to which HTML files. Also, feel free to serve your entire application in either one page, or on multiple pages with links or buttons to navigate between them.

#### Developing Locally

Please note also that although GitHub pages automatically renders D3 visualization, your computer does not. If you are working locally on your computer you will need to open the folder containing your `index.html` and run

```
python -m SimpleHTTPServer 8000
```

Then you can view your page as you're building it by typing into the address bar in the browser `localhost:8000`.

### Narrative Structure & Cohesiveness

Try to bring together the website into one cohesive whole. Each person may have worked on different parts of the website, but I am hoping you can learn to give the entire site a consistent look and feel.

Some teams may chose to bring this consistency by focusing more on the CSS, others may focus more on having a coherent narrative structure. Some teams may decide to do both (which will get you more points). Regardless of how you chose to demonstrate consistency, the website should show that you've been working as a team to build a unified product.

### Chart Copy

One additional note about visualizing data in charts. Often a descriptive title and subtitle of the chart (or as we journalists say a "Hed" and "Dek") can go a long way to effectively communicating either the purpose or the content of the data that you are visualizing. The "Hed" can be more describe the narrative you're hoping the reader will focus on while the "Dek" might be a more detailed explanation of the nature of the data itself. If you are looking for inspiration for heds and deks, just browse some articles at http://fivethirtyeight.com or your reputable news site of choice and focus on their charts.

Each chart should have

* A narrative hed (Headline)
* A descriptive dek (Subheadline)
* Axis Labels (what units the axes are in)
* A legend (if there are multiple data series displayed)
* A link citing the original data source
* A link citing the sample D3 code you pulled from
* Footnotes if needed

Kudos if you manage to get all of that into the chart itself. If not, you may write the parts you weren't able to get into the chart in a little note under the chart. If you chose the latter option, I would expect that chart notes will have a different CSS style that distinguish them from the rest of the text on your page.

## Process

Remember to keep your processes agile. This means you team will value:

**Individuals and interactions** over processes and tools

**Working software** over comprehensive documentation

**Customer collaboration** over contract negotiation

**Responding to change** over following a plan

### Roles
Appoint a scrum master, a project owner, and team members.

  * The product-owner is in charge of documenting progress on your scrum board in trello every day.
  * The scrum master is in charge of documenting standup meetings.
  * Team members (and the scrum master and product owner) will collaborate using GitHub to build the project together.

### Daily Scrum Meeting

Your team will hold a daily scrum meeting. These stand-up meetings can be as brief or as long as you need, although remember, the scrum meeting is intended to be short and is frequently done standing up for this purpose. You don't have to resolve your problems during scrum, just surface them and resolve them with only the parties that need to be present either online or offline.

Remember, one of the twelve principles of agile development is:

>"The most efficient and effective method of conveying information to and within a development team is face-to-face conversation."
[- 12 Principles Behind Agile Manifesto](https://www.agilealliance.org/agile101/12-principles-behind-the-agile-manifesto/)

Since Agile development prioritizes individuals and interactions over processes and tools, and highly values face to face conversations, the scrum meeting should be either in person or via video conference - you may elect to use Slack if scheduling becomes difficult, but that is the least preferred method. If you think video conferences are not working, you can make a quick pivot to in-person meetings.

Please add the notes from each scrum meeting into your "process" submission. If you haven't taken notes, please at least document the date and time of each meeting along with whether it was in-person, on skype, or via slack.

### User Stories

In your trello board, there should be a list containing user stories in this format:

>As a ____
>
>I want ____
>
>so that ____.

The user stories should be well defined. Each card should have an explicit "definition of done" and should meet I-N-V-E-S-T. The 5-6 stories that you and your team have commited to for the last sprint should be labeled somehow. There should also be additional user stories that are maybe less fleshed out further down in that list.

### Sprint Planning
Your team will hold a sprint-planning meeting at the start of the project period. This meeting will be split into two parts as described in "SCRUM: A Breathtakingly Breif and Agile Introduction". Re-read the section on sprint planning before starting this meeting.

During the first part of the meeting the team will collectively decide how much they think they can accomplish.

During the second part, you will break the stories down into tasks and put them on a trello board. Everyone on the team will assign tasks to themselves. This will involve a round of scrum "poker".

Most of the tasks on your scrum board will have a number attached to them as a result of this meeting. Those numbers should reflect your progress as a team. You should be keeping track of your "burndown" or "burnup" every day (how many points you've accomplished).

### Sprint Review

Normally during a sprint review, all the stakeholders gather and view a demo of what software you built in the last sprint. Your submission will serve in the place of this meeting. This will happen via a GitHub issue described in the "Submitting your project" section below.

### Retrospective

At the end of the project, your team should hold a retrospective meeting. Each team member is asked to identify one specific thing that the team should:

> Start doing
>
> Stop doing
>
> Continue doing

In addition to one of each per team member, as a team please agree on one thing that you will commit to start, stop, and continue doing in the next sprint. Of course there is no next sprint since the class will end, but assuming you were to iterate on this project, whats one thing you can all agree will change in the next sprint? Keep in mind that the retrospective is more about process than the product, so these should be more about things you as a team can do to have a more productive next sprint. They should also be discrete and actionable items, not vague thoughts like "communicate better".

### Artifacts

Process

* Maintain an active [task board](https://www.mountaingoatsoftware.com/agile/scrum/scrum-tools/task-boards) on Trello. Your user stories will be on this board as well.
* You will submit a "burn down" or a "burn up" chart with how many "points" you accomplished each day as a team
* Maintain a record of your collaboration on GitHub using social features such as commenting on one another's code, recording problems with github issues, or leaving notes when merging branches and approving pull requests. Alternatively, if you're meeting regularly in person and discussing these issue, you can just let me know that. I should also be able to see that you're using branches in a meaninful way when I look through your git history.
* If you're not meeting in person, I would also expect that your project group would have an active slack channel.
* Some kind of record of your "standup" meetings (perhaps the scrum-master's notes about blockers) along with the date and time of each meeting and whether it was in person, on video chat, or using slack.
* A record of your retrospective (each team-members suggestions on what to start, stop, and change in the next sprint) along with a note about **one** thing you've agreed on as a team to start, stop, and change.

Product

* original source data, transformation steps (or python script), and final data that your visualization consumes
* A link to your final project rendered on GitHub pages
* A note from each team member as to what, if anything, they modified in their visualization of choice (beyond switching out the dataset)

(If you want to make the README.md files look nice, just take a look at the raw code behind the file you're currently reading)

## Submitting the Project

When you're ready to submit the project, please create a new github issue in your repository called "Ready for Review" with links to all of the items in the checklist.

In your team's slack channel, post a link, to that issue and mention @dhrumil letting me know that the project is submitted and ready for my review. Once I've recieved that note from you, I may start grading the project. Please note that the projects are due by midnight of **Monday Jan 15**.

Please **let me know** if you think your team needs more time and won't be able to meet the originally set due date so that I know when to expect a submission.

## Grading

Your project will be worth 50% of your grade, that will be divided as follows

* 15% process
* 35% product

The rest of your grade for the course will be:

* 20% in class assignments
* 30% participation (participation during class assignments and discussions, participation on GitHub, Slack, and Trello)


## Availability

I am on campus at least Saturday and Sunday and available to meet either in person or via video chat. My office is in "Belfer Lobby 2A" which is located to the right of the Belfer entrance (although you may have to use a different entrance to the building on weekends). Just shoot me a message on slack letting me know you're coming in case I'm wandering around Harvard Square or at a nearby cafe and I can arrange to meet you there or can help remotely via Slack.

## Course Evaluations

You should have received an email about the course evaluations, they are accessible through the [canvas page for this class](https://canvas.harvard.edu/) and are **due on Thursday Jan 25**. This is the second time this module was offered at HKS and a fairly new curriculum. Your honest feedback will be particularly important both in helping me understand how to best iterate on the course as well as helping the Kennedy School better understand the role of technical education in the curriculum. Please take some time to thoughtfully fill out the course evaluation, your feedback is of particular importance in the context of this module.

## Final Note

Please feel free to reach out via slack, email (dhrumil.mehta [at] gmail.com), or twitter (@datadhrumil) if you have any further questions, comments or concerns. I look forward to hearing from you in the future about how you've used the knowledge you picked up during this course.

I hope you all found the projects instructive and enjoyable. Diving into new technologies can be both disorienting and rewarding. Learning new programming skills is often a cyclical process of getting stuck and unstuck. It is not uncommon to get lost in rabbit-holes of debugging or reading about technologies in an attempt to unpack how exactly they work.

Learning how to learn programming by searching the web for relevant resources, reading technical discussions and forums, and testing out example code snippets, as well as leaning on other programmers and knowing who to call when you're stuck are themselves important skills: skills which many of you got a chance to explore in attempts to customize your visualizations (some of you even decided to customize the JavaScript to change the behavior of the visualizations, which was not at all required for the project so kudos to those who tried!).

I hope that the class can serve as a stepping stone if you chose to further study technology or programming. If you don't ever end up coding again, I hope that the exercise of doing hands-on coding work has given you a better understanding of and appreciation for important issues at the intersection of technology and policy. Best of luck and enjoy! 
