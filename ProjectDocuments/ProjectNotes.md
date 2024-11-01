# Child Health And Wellbeing Tracking Software (CHAWTS)

## 0. Table of Contents
- [0. Table of Contents](#0-table-of-contents)
- [1. Purpose of File](#1-purpose-of-file)
- [2. Project Outline](#2-project-outline)
- [3. Features](#3-features)
## 1. Purpose of File
### Provided Purpose
- Create a Markdown document in the team's git repository and link to that in Jira. This can include drawings/scans 
of notes.  If more than one person wants to do this, then subtask it on Jira, and collaboratively write the document on gitlab (use the webserver cseegit to edit this Markdown document - much easier than using the command line for simply editing a text document).
### Useful information regarding file
- Personal notes should be put in code blocks to differentiate them
  - e.g. `I think we could implement this with like... etc`

## 2. Project Outline

### Idea
- A Child Health and Well-Being Tracking Software
- Source
  - https://moodle.essex.ac.uk/course/section.php?id=188478

### Provided outline
- This project focuses on developing a comprehensive **Child Health and Well-Being Tracking Software** designed to 
assist parents and caregivers in **monitoring key aspects of a child’s growth, health, and daily activities**. With the growing need for data-driven insights into a child's development, this software aims to simplify the management of essential routines, **including sleep patterns, feeding habits, diaper changes, medications, and growth metrics**. By tracking these variables, the **software will provide caregivers with actionable data**, enabling them to make informed decisions about their child’s health and well-being. The system will **generate visual representations of the child’s progress** over time, offering intuitive **graphs, detailed reports, and statistical analyses**. For instance, sleep and feeding patterns will help parents establish healthy routines, while diaper and medication tracking will aid in monitoring health conditions.


- One of the key objectives of this software is to offer **customized insights**, such as **average feeding 
quantities, growth percentile comparisons, and medication schedules**, allowing for better healthcare management. Additionally, **daily reports can be generated in PDF format** for consultations with healthcare providers, enhancing the utility of the software. Ultimately, this solution empowers parents with the necessary tools to keep track of their child's development and to respond proactively to potential health issues. The software not only eases daily caregiving tasks but also promotes healthier lifestyle choices, making it a valuable asset for modern families.

### Summary
- Child health and wellbeing tracking software
- Monitors growth, health & daily activities
  - e.g. sleep patterns, feeding habits, diaper changes, medications, growth metrics
- Provide actionable data ??? 
  - "Data that has been processed and presented in a way to be used to make informed decisions"
- Generate visual representations of progress
  - e.g. Graphs, Reports, Statistical analyses
- Customized insights
  - "You create conditions that detect changes in your data that are important to you"
  - Show user primarily information that they have selected as important
    - e.g. average feeding, growth percentile comparisons, and medication schedules etc
- Daily reports generated in PDF format

## 3. Features

1. Adding a child
   - The software should have the option of adding multiple children by their name, sex, and date of birth
   - All features should automatically adjust for which child is selected.

2. Tracking the sleep timings and duration of the child
   - Adding sleep start time with a date
   - Adding sleep end time with a date
   - Tracking sleep patterns over a given period of time
     - Produce graphs (Line, bar etc) to show naps/hours of sleep per day 
   - Analyze and interpret sleep data for user
     - e.g. Day normal nap time, night normal sleep duration
     - Generate key statistics to help parents make informed decisions

3. Tracking the feeding/eating pattern of a child