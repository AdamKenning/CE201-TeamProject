# Requirements and Risk Log

*In this markdown document, list all of the requirements that you have identified for your product so far.*

# Requirements

*List several user stories (no more than 8) that describe the product requirements. For each user story that you include:*

* *Include a URL link to the Jira user-story issue.*
* *Paste in the Story Description and Story Summary from Jira.  Attempt to keep story summaries in the form taught in the lectures, i.e. the form "As a [persona], I [want to], [so that]".  Feel free to update your Jira issues into this form if they are not already.*
* *Give details of whether this story has been assigned to someone yet, and whether it is completed yet.*
* *Include a screenshots of any relevant attachments.*

*In addition to user stories (which is the main thing we are trying to teach for agile), try to include one or two other requirement modelling techniques, e.g. as listed in the lecture.*

*Try to group the requirements under two sub-headings: functional requirements, and non-functional requirements.*

*When marking this section we will be looking to see your team has understood the correct way to represent User-Stories and one or more other requirement modelling methods, and the requirements listed are giving as much relevant information for the development team as possible.*

## Risk Log

*In this section list the risks you have identified for your project.  For each Risk identified:*

* *Include a URL link to the Jira risk issue.* 
* *Paste in the Risk's Description and Summary from Jira.  Also state the Impact and Likilihood.*
* *Give details of whether this story has been assigned to someone yet, and whether it is completed yet.*
* *Include, from the Jira description / comments, details of what mitigating actions are being taking and by whom.*

*When marking this section we will be looking to see several realistic risks have been noted, and are actively being tracked and mitigated against.*

--- 

## Requirements Log - Zubair
## Risk Log - Adam

### Section Summary
Due to the nature of the software our team is creating, and the methods by which we have implemented thus far (and the methods we have planned to implement at a later date), there are inevitable risks involved that concern some of our projects parties.

The purpose of this section of the report is to address such risks and to establish the means by which these risks will be faced and countered before the software reaches its completion.

### Important Context
As far as actual genuine risks that pose a threat to the software in its current state (development), there are none. In its current stage, the software exists in a state of constant development by our team, and is only accessible to our team. Our software which is planned to be hosted as a website, during its development period, will remain offline and inaccessible to any person (or entity) that may negatively impact it.

However, it is once it leaves this developmental safe area when it will become liable to various risks, and it is predominantly those risks that arise then that will be the focus of this document.

Jira, our chosen platform for team coordination and management, has not yet the formal explicit mentions of these risks and their counteractions. Once again, this is still something to be dealt with after other functionality has been addressed. It is in spite of this though, that there does exists the initial thinkings of such countermeasures. These thinkings take the form in the Jira story noted here : 
>Jira story, "Add additional user Stories" : https://ce201-team02.atlassian.net/browse/SCRUM-47

The name of the story, admittedly, is not entirely suggestive of the story itself, but the description is more, descriptive.
>"Note additional user stories that relate to the safeguarding of our software both against cyber related threats, as well as threats to the usability that come from inaccessibility unaccounted for such as colour blindness."

This Jira story assigned to our team member, Adam Kenning, was focusing on broadening our user stories; what we use in guiding the creation of our website. Briefly, user stories serve the purpose of explicitly dictating who our user(s) are, what they need to be able to accomplish using our software, and for what purpose do they need to accomplish this. 

The user stories outlined in the "Add additional user stories" specifically target the risks posed against our software, and as mentioned already will be the subject of this risks assessment log.
### Software Risks
Broadly speaking, The risks posed to our software can be categorized as into two sections:
>1. **Security and data integrity** : Risks that have the potential to negatively impact the security and data integrity of our software.

>2. **Usability and accessibility** : Risks that pose a concern to the usability of our software for a subset of our users, who have special considerations that need to be addressed.

Although the latter, 'Usability and accessibility', may not initially be thought of as something that would constitute a 'risk', it is, and it is an important collection of requirements that need to be considered to eliminate any and all risks. Any aspect (or lack thereof), of our software which dissuades or disallows a user to use our service is inherently a risk. It is thereby of no less important to consider these aspects than aspects relating to the former, 'Security and data integrity', risks section.

#### **Security and data integrity**
This category of risks, broadly covers aspects of our software wherein exist the possibility of a negative impact, on account of actions relating to the electronic handling of our users personal information. By extension, this includes the way in which our software manages the relevant meta information associated with each part.

Subcategories of this section that have been noted and will be accounted for are as follows.
>The meta information, such as the implied relation between users must remain hidden 

>Personal data relating to a user is only accessible to the authorized user(s)

>Data of any kind must only be managed; edited and (or) deleted, by the relevant user(s)

>Information must be able to be shared only with authorized users (When authorized)

>Users, who opt in to share their data for academic study, must remain anonymised

>User accounts must be held secure using strong password enforcement

>User account login credentials, such as passwords, must be stored with strong encryption

Others : 
>2FA authentication
>Session timeouts
>Secure communication timeouts (https)
>anti brute force - password guessing
>Registered devices associated with an account


#### **Usability and accessibility**


Ensure the app has offline capabilities, allowing parents to log data without an internet connection (to be synced when online)


secure login methods

1. Usability and Accessibility


   1.  Accessibility and Usability
    - As a **user with accessibility needs** i need the app to include:
      - **Themes** like sepia and dark mode **to reduce eye strain**
      - **Clear, large fonts** for **easier reading** - dyslexia
      - **Large buttons** for **easier navigation with motor impairments** - parkinson's
    - As a **user with colour blindness** I need the app to include **Colour profiles** for **easier viewing**
      - Protanopia - Red blind
      - Deuteranopia - Green blind
      - Tritanopia - Blue blind
      - Achromatopsia - Complete colour blindness