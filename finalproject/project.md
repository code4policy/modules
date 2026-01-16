# Project

Please find below a description of expectations for your final project. There are two parts - product and process.

## Product

For your final project, you will work in a scrum-inspired agile software team with your classmates to build a data-driven website about a particular area of policy interest. Your team will select users for your project and build them a data-powered web application with visualizations that serve the needs of that user.

### Selecting Data

You are welcome to select data from any credible data source. Make sure to cite it appropriately in the project.

### Selecting a visualization [optional!]

Selecting the right visualization for your data and the comparisons you're trying to make is a good dataviz skills. Check out the [Financial Times Chart Taxonomy](https://github.com/Financial-Times/chart-doctor/blob/main/visual-vocabulary/FT4schools_RGS.pdf) as you think about what kind of vizualization to select. 

If you choose to make a visualization, you can make a d3 chart. If you'd like to try charting in R, ggplot is a great library for making data visualizations. If you find another way to learn a new thing on your own, [DataWrapper](https://www.datawrapper.de/) also makes great charts. 

Regardless of which tool you use, you will want to follow our class [style guide/charting rubric](https://docs.google.com/document/d/1F-q9jFx8902zhBnJ0o4GwSHQhqJLZKnq-L4SU7kn544/edit). This framework articulates some of the same principles our dataviz guest speakers spoke about. Make sure to think about concepts like presentation, visual heiarchy and chart headlines/labels/etc... 

Here are some other examples of visualizations in D3 

- https://d3js.org/
- https://observablehq.com/@d3/gallery
  
You're welcome to make a new D3 viz with ChatGPT (although do make sure to cite it appropriately) or to pick one from an example. You must make **at least one small modification** to the demo code you've picked. It can be something as simple as modifying a color, or something more ambitious if you chose. 

### Your Dataset

We're **not** going to have a proper "back end" server that pulls from a database and serves up an API. Rather, you will find a dataset and place it in a folder within your repository. The "back end" code should be separate from the "front end" code, you can keep it in a separate folder called "data".

For each dataset you should have:

- a copy of the original data in the format you got it in
- a `README.md` or `README.txt` file with a link to the original data source and an explanation about how you transformed the original data into the final format you needed. If you've done the transformation using a python script (or in any other programming language), just uplaod that script -- no need to document. Just comments within the code will be sufficient. If you used some other means, please document your data transformation process in the README file. It should be a step by step explanation, not just one pithy sentence like "I transformed the data with excel".
- a copy of the final data which will be consumed by the visualization

Remember, sometimes you might be able to tell a better story by filtering the data down to an interesting subset rather than visualizing all of it. Refer back to the ["Making Good Charts" lecture](https://docs.google.com/presentation/d/1tk3kWduR791qut2KFTNWIKlQuk4xrA-bvdIryTQHffE/edit#slide=id.g7c12118c05_0_15) for tips on possible ways to tell a good data-drven story.

### Code Organization / Cleanliness

The front end will contain HTML, CSS, and JavaScript. I will expect each component to be in a separate file.

Your code should also be organized in a meaningful way. One example would be Mozilla's recommended file structure where all the JavaScript is in one folder, all the CSS in another, all the data in another: 

* https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/Dealing_with_files

Another possible structure is the one you see in this example repo: 

* https://github.com/code4policy/example-frontend
* https://github.com/code4policy/example-frontend-2/

You're welcome to use a different file structure, but there should be some consistancy in the way your files are named and organized. Try to make sure that URL's are meaningful in the context of your application, and also that it is clear from the filenames which page each CSS, JavaScript, and data files map to which HTML files. Also, feel free to serve your entire application in either one page, or on multiple pages with links or buttons to navigate between them.

Well commented code will get more points! Feel free to write as many comments in as many places in the code as you'd like. Explain things as you understand them better (or leave notes if something works but you don't understand it).

#### Developing Locally

Please note also that although GitHub pages automatically renders D3 visualization, your computer does not. If you are working locally on your computer you will need to open the folder containing your `index.html` and run

```
python3 -m http.server 8000
```

Then you can view your page as you're building it by typing into the address bar in the browser `localhost:8000`.

### Narrative Structure & Cohesiveness

Try to bring together the website into one cohesive whole. Each person may have worked on different parts of the website, but I am hoping you can learn to give the entire site a consistent look and feel.

In addition to telling a coherent story across the site, one way to give your site a consistent look and feel is to put all the CSS in one file and have some CSS selectors that apply to the whole site, and others that apply only to particular charts on the site. Refer back to the lessons on correctly using "id" and "class" selectors to avoid conflicting CSS.

Some teams may chose to bring this consistency by focusing more on the CSS, others may focus more on having a coherent narrative structure. Some teams may decide to do both. Regardless of how you chose to demonstrate consistency, the website should show that you've been working as a team to build a unified product.

### Visualizations {optional{

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

### User Centric Design

Finally, a core component of agile software development is keeping the user at the center of the software design process. One of the way we do that is to make user personas and user stories to capture requirements. As such, one of the criteria for grading will be how well the project serves the users as stated in the user stories. Remember though, in this class the product is both a website for your users as well as a learning tool for you. In that sense you are one of the users, and your story can also be captured in the user stories. 

For example: A group may spend a lot of time on the styles for their website if one of their user stories involves showing off their design skills in their portfolio. Another team may have a very spartan website, but have spent their time making lots of modifications to the original JavaScript chart because one of their user stories involves exploring an unfamiliar programming language.

## Process

Remember to keep your processes agile. This means you team will value:

- **Individuals and interactions** over processes and tools
- **Working software** over comprehensive documentation
- **Customer collaboration** over contract negotiation
- **Responding to change** over following a plan

### Roles
Appoint a scrum master, a project owner, and team members.

  * The product-owner is in charge of documenting progress on your scrum board every day.
  * The scrum master is in charge of documenting standup meetings.
  * Team members (and the scrum master and product owner) will collaborate using GitHub to build the project together.

### Project Boards

Your project should contain 3 boards:

- Sprint 1
- Sprint 2
- Backlog

The Backlog board will contain all the stories that you didn't get to ordered roughly from smallest to largest with the smaller ones more fleshed out (definitions of done + INVEST). The sprint boards will contain the user stories you took on during that sprint and columns for TODO, DOING, BLOCKED, and DONE.

### Daily Scrum Meeting

Your team will hold a daily scrum meeting. These stand-up meetings can be as brief or as long as you need, although remember, the scrum meeting is intended to be short and is frequently done standing up for this purpose. You don't have to resolve your problems during scrum, just surface them and resolve them with only the parties that need to be present either online or offline.

Remember, one of the twelve principles of agile development is:

>"The most efficient and effective method of conveying information to and within a development team is face-to-face conversation."
[- 12 Principles Behind Agile Manifesto](https://www.agilealliance.org/agile101/12-principles-behind-the-agile-manifesto/)

Since Agile development prioritizes individuals and interactions over processes and tools, and highly values face to face conversations, the scrum meeting should be either in person or via video conference - you may elect to use Slack if scheduling becomes difficult, but that is the least preferred method. If you think video conferences are not working, you can make a quick pivot to in-person meetings.

Please document the date and time of each daily standup meeting for your "process" submission along with whether it was in-person, on skype, or via slack. I should see activity on GitHub during that time. As you say what you did since the last meeting and what you intend to do before the next meeting move the cards to the appropriate column in the board.

The scrum master will note down the number of points completed at the end of each meeting.


### User Stories

In your scrum board, there should be a list containing user stories in this format:

>As a ____
>
>I want ____
>
>so that ____.

The user stories should be well defined. Each card should have an explicit "definition of done" and should mostly meet I-N-V-E-S-T. The stories that you and your team have commited to for the last sprint should be labeled somehow. There should also be additional user stories that are maybe less fleshed out further down in your Backlog.

### Sprint Planning
Your team will hold a sprint-planning meeting at the start of the project period. This meeting will be split into two parts as described in "SCRUM: A Breathtakingly Breif and Agile Introduction". Re-read the section on sprint planning before starting this meeting.

During the first part of the meeting the team will collectively decide how much they think they can accomplish.

During the second part, you will break the stories down into tasks and put them on a scrum board. Everyone on the team will assign tasks to themselves. This will involve a round of scrum "poker".

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

* Link to [task boards](https://www.mountaingoatsoftware.com/agile/scrum/scrum-tools/task-boards) for SPRINT 1, SPRINT 2
* Link to USER STORIES board (for any additional user stories)
* Link to a record of standup meetings including burndown for each sprint. Something like this:

	Date/Time | Type | Points | Remaining | Total
	----------|------|---------------|------------|------
	Jan 1 4pm | In Person | 40 | 60 | 100
	Jan 2 3:30 pm | Skype | 55 | 57 | 112
	Jan 3 10am | In Person | 70 | 42 | 112
	Jan 4 12pm | Slack | 90 | 22 | 112
	Jan 5 8pm | In Person | 110 | 2 | 112
	
	If you're not meeting in person, I would also expect that your project group would have an active slack channel.

* Completed retrospective google form (one per group): https://docs.google.com/forms/d/e/1FAIpQLScqZPQtdVDa59zqL5IbCnhCKilzCNdqK9mKDif9Z2xZH_by8w/viewform?usp=sf_link

Product

* A link to your final project rendered on GitHub pages
* A "data" or "backend" folder containing original source data, transformation steps (or python script), and final data that your visualization consumes for each dataset
* A completed final project **technical reflection** from each student (these will be graded individually): https://forms.gle/PK13tcjCNvtAZFE39

## Submitting the Project

When you're ready to submit the project, please create a new github issue in your repository called "Ready for Review".

In your team's slack channel, post a link, to that issue and mention @dhrumil letting me know that the project is submitted and ready for my review. Once I've recieved that note from you, I may start grading the project. Please note that the projects are due by midnight of **Monday Jan 16** (so Monday night).

Please **let me know** if you think your team needs more time and won't be able to meet the originally set due date so that I know when to expect a submission.

## Grading

Your project will be worth 40% of your grade, that will be divided as follows

* 10% process
	* Sprint Review (1x, the "review" for sprint 2 is the grading process)
	* Scrum Boards (2x sprints, 1x user story backlog)
	* Burndown Charts (2x, 1 per sprint)
	* Collaboration on GitHub
* 30% product
	* Frontend
		* Working software
			* well defined user stories
			* working software that meet the user needs
		* Narrative Structure / Coherence 
		* Visualizations
		* Code organization/cleanliness
		* Demonstrate understanding or experimentation through code comments
	* Backend
		* Data transformation (scripted or documented)
		* Clean and organized


## Availability

I am on Ohyay and Slack most of Saturday and Sunday and available to meet via video chat. If you can't find me, just shoot me a message on Slack letting me know you're coming in case I'm wandering around. The TAs should also be around (on and off) over the weekend.

## Course Evaluations

You should have received an email about the course evaluations, they are accessible through the [canvas page for this class](https://canvas.harvard.edu/) and are **due by January 19**.  Your honest feedback will be particularly important both in helping me understand how to best iterate on the course as well as helping the Kennedy School better understand the role of technical education in the curriculum. Please take some time to thoughtfully fill out the course evaluation.

## Final Note

Please feel free to reach out via slack, email (dhrumil.mehta [at] gmail.com), or twitter (@datadhrumil) if you have any further questions, comments or concerns. I look forward to hearing from you in the future about how you've used the knowledge you picked up during this course.

I hope you all found the projects instructive and enjoyable. Diving into new technologies can be both disorienting and rewarding. Learning new programming skills is often a cyclical process of getting stuck and unstuck. It is not uncommon to get lost in rabbit-holes of debugging or reading about technologies in an attempt to unpack how exactly they work.

Learning how to learn programming by searching the web for relevant resources, reading technical discussions and forums, and testing out example code snippets, as well as leaning on other programmers and knowing who to call when you're stuck are themselves important skills: skills which many of you got a chance to explore in attempts to customize your visualizations (some of you even decided to customize the JavaScript to change the behavior of the visualizations, which was not at all required for the project so kudos to those who tried!).

I hope that the class can serve as a stepping stone if you chose to further study technology or programming. If you don't ever end up coding again, I hope that the exercise of doing hands-on coding work has given you a better understanding of and appreciation for important issues at the intersection of technology and policy. Best of luck and enjoy! 
