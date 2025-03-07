## Team member name Ruoyu Sun(Charles):
### Sprint 8 (University Week 18):
https://ce201-team02.atlassian.net/browse/SCRUM-88
https://ce201-team02.atlassian.net/browse/SCRUM-96
https://ce201-team02.atlassian.net/browse/SCRUM-102

Now that we have completed the MVP, the product needs further work to be fully functional.
Django is the main tool we are going to use, so this week our team focused on getting Django up and running.
Also we plan to start by setting up a virtual environment on our laptops, allowing each of us to work on our individual parts and eventually merge them.
By working on our own branches, we can ensure that others cannot interfere with our work, and it is easy for me to complete this task. It took 30 minutes.

### Sprint 9 (University Week 19):
https://ce201-team02.atlassian.net/browse/SCRUM-115
https://ce201-team02.atlassian.net/browse/SCRUM-108

As we began working on the implementation for this project, our main task this week was to familiarize ourselves with Chart.js, which we plan to use for creating charts and graphs. We also attempted to integrate it into our project as a test. It took 1 hour.
Alongside this, we also need to address the errors in the front end from the MVP, as it is not functioning optimally. We plan to refine it and convert it into the appropriate backend format.

### Sprint 10 (University Week 20):
https://ce201-team02.atlassian.net/browse/SCRUM-130

This week, I continued working on my assigned page, the food page.
Additionally, I was tasked with figuring out how to export a PDF for a specific child, including all the relevant information. It took me about an hour to discover.

### Sprint 11 (University Week 21):
https://ce201-team02.atlassian.net/browse/SCRUM-144
https://ce201-team02.atlassian.net/browse/SCRUM-150

This week, I worked on converting the food page to the backend, making the charts function dynamically.
After saving the data, the table is automatically updated, and a line chart is generated to visualize the food intake. It took 2 days during this week.

### Sprint 12 (University Week 22):
https://ce201-team02.atlassian.net/browse/SCRUM-155

As we only have two weeks left before the deadline, we need to start working on the report.
I chose to write the Product Context Report section, but I haven’t finished it this week.
Additionally, some errors still exist, so we need to fix them and try to make it looks better.

### Sprint 13 (University Week 23):

During this week, I finished my report by Thursday. Our team will meet on Friday to fix any remaining issues and upload the final product.

## Team Member : Munashe

### Sprint 8 (University week 10)
https://ce201-team02.atlassian.net/browse/SCRUM-82

In this scrum we were meant to get the virutal machine working so that all of us as a group can work together on one things, when we started we were struggling using github, it would take quite some time for things to go through when typing the ocde and a lot of the time things would freeze, so we decided to then used visual studio code, we went on csee gitlab and then copied the https link and then i went a cloned the git repository. And after that as a group we where then able to start working together.

https://ce201-team02.atlassian.net/browse/SCRUM-83

In this scrum we had to get django working, which was quite complicated to do howeer i had help from my team members who are more knowledgeable in the the area about visual studio code and python etc.

https://ce201-team02.atlassian.net/browse/SCRUM-84

For this we had to run the server on our devices so we can make improvemtns and see how it would look for the final product.
What we had:
## deactivate virtual environment if currently in one

if ($env:VIRTUAL_ENV) {

    deactivate

}

Write-Host "[1/3] Starting Virtual Environment..."

set-Location (Split-Path $MyInvocation.MyCommand.Path) # set location to wherever this file is

. .\venv\Scripts\Activate

Set-Location djangoProject

Write-Host "[2/3] Applying Migrations..."

python manage.py migrate *> $null

Write-Host "[3/3] Starting the Server..."

python manage.py runserver

When i run this this is what i get in the terminal:
March 04, 2025 - 14:36:49

Django version 5.1.6, using settings 'djangoProject.settings'

Starting development server at http://127.0.0.1:8000/

I can then click on the link and it will then take me to the website.



### Sprint 8 – 9 (university week 17)
https://ce201-team02.atlassian.net/browse/SCRUM-110

For this i went on the chart.js to look up on how to make a line graph to show the child development over time i idid find this quite difficult to know how to do this. However i then found a website where i can do this and for this i also made a tab where it will be a weight height and head size. Where the user can switch between where they want to see.
https://ce201-team02.atlassian.net/browse/SCRUM-91

For this i had to go back to my page and make sure that everyhintg works as it should and that i should be optimizing my code before i start working on how to figure out how to the database stuff. For this i was making sure that i was checking the spelling of the things in my page, seeing ways in which i can make my code simpler and easier to read. And testing things out so that they work.

### Sprint 10 (university week)

https://ce201-team02.atlassian.net/browse/SCRUM-128
for this i had to make a medication page. On this page the user can select which child is taking which medicine. On the page there would be input boxes for the parents or caregivers where they can put the medication name how much they are taking like dosage where its 5 ml or like 2 tables. I also had a place for how many time are they taking the medication in a day and what time they are doing it so that they can keep track. I also added a status if the medication has been completed or they are not using it anymore. And there was also a date added slot so they can keep track. I also added a calendar so the adult can look back and see what medication they have taken or time.

### Sprint 11 (university week)

https://ce201-team02.atlassian.net/browse/SCRUM-126
https://ce201-team02.atlassian.net/browse/SCRUM-127

For this i had to finalize my page fully, this is that part the i struggled with a lot i  am not that good with programming so i struggled a lot with this one. I was able to finish the html part of my website. Then there was the more difficult part of  connecting it to the database this is the part that i struggled with the most because i had no knowledge in this area, however i had teammates who did know, so the assisted me with it. When i go to the improved page it links with the database so when i add a child on the main page it then links with the my growth page. Next i had to work on a medication page this was i page that i wa interested in doing but it was not that far off from my own page, so that was a lot that i could bring over to make things easier.

### Sprint 12 (university week)

https://ce201-team02.atlassian.net/browse/SCRUM-156

For this scrum i had to write a report on the product and i chose to do the marketing side of it. For this i had to write a marketing plan, i inlcuded things like the customers, what demographic is most likely to  purschase / donwload  our application. I then had to touch on the economics side of it.  like what is the total size of the market. How much of the market can we have when we release our application. And what is the current demand in the space that we are in. And the trend like what are other apps doing that make the popular. I also took a look at other apps like i did before where i looked for ideas on wha makes  a growth tracker good, this time i was looking at what our app does better than those ones on the market. For the last part i had to make a sales forecast for how well our app will do. however last minute changes were made in the database py area, so im not sure if my medication page works well.s

## Zaki Hamdan

### Sprint 8 (University Week 18):

In week 18, I managed to get my virtual environment and Django working on my personal computer. Figuring out how to get Django working on macOS turned out to be hassle to deal with and took much longer than expected to get running. it took around 45 mins to get it done
https://ce201-team02.atlassian.net/browse/SCRUM-85

https://ce201-team02.atlassian.net/browse/SCRUM-97

### Sprint 10 (University Week 20):

In week 20, I added a feature where a user can change the colour of their screen in case the user is colourblind and unable to differentiate between certain colours. It took a few hours to complete this task.
https://ce201-team02.atlassian.net/browse/SCRUM-129