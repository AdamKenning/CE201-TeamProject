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
 # user stories (collective team effort)


Functional Requirements
1.	Tracking and Logging Routines
- Story Summary:
  - As a parent and caregiver, I want to log feeding, sleep, diaper changes, and medication schedules so that I can track patterns to track my child’s health.
- Story Description:
  - This story focuses on the app functionality that allows caregivers to log essential routines, including the time and type of activity (e.g., feeding, sleep, diaper change). It should support visual summaries and allow users to compare daily patterns for better health management.
2.	Growth and Development Monitoring
- Story Summary:
  - As a parent, I want to track my child's height, weight, etc., over time so that I can monitor their growth and compare it to standard benchmarks.
- Story Description:
  - This story focuses on recording growth data such as height and weight, presenting these metrics visually (e.g., graphs), and comparing them to percentile standards for health insights.
3.	Insights and Alerts
- Story Summary:
  - As a parent and caregiver, I want to be notified about changes in routines or health so that I can identify potential issues early.
- Story Description:
  - Notifications should be triggered based on deviations in logged data, such as irregular sleep patterns or skipped medications, and provide actionable insights for the caregiver.
4.	Interactive Visual Summaries
- Story Summary:
  - As a parent, I want simple interactive graphs and visual summaries to quickly understand development trends.
- Story Description:
  - This story focuses on creating interactive dashboards that present patterns and trends in feeding, sleep, and growth data, helping parents make informed decisions.


Non-Functional Requirements
5.	Multi-Device Support
-Story Summary:
  - As a parent or caregiver, I want to use the app on multiple devices so that I can manage my child on the go.
- Story Description:
  - Ensure the app is compatible across platforms (iOS, Android, web) with data synchronisation in real-time.
6.	Secure Data Handling
- Story Summary:
  - As a parent, I want assurance that my child data is securely stored and anonymised so I can protect their privacy.
- Story Description:
  - Implement encryption for stored data, secure login methods, and anonymisation protocols for data shared with researchers.

## requirements modelling technique (Use Cases)
- A use case diagram can illustrate how different users such as parents, caregivers, healthcare providers, and researchers interact with the system.
- Actors: Parent, Caregiver, Healthcare Provider, Researcher
- Use Cases:
  - Log feeding/sleep/diaper/medication
  - Track growth metrics
  - View interactive graphs
  - Generate and share reports
  - Receive alerts
  - Access anonymised data




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
For each risk, the format will remain the same for the purposes of homogenous reading. This format is as follows : 
- **Risk title** : The subject in question
  - **Description** : A brief description of the risk
  - **Mitigation** : Method(s) by which the risk can be averted

Broadly speaking, The risks posed to our software can be categorized as into two sections:
>1. **Security and data integrity** : Risks that have the potential to negatively impact the security and data integrity of our software.

>2. **Usability and accessibility** : Risks that pose a concern to the usability of our software for a subset of our users, who have special considerations that need to be addressed.

Although the latter, 'Usability and accessibility', may not initially be thought of as something that would constitute a 'risk', it is, and it is an important collection of requirements that need to be considered to eliminate any and all risks. Any aspect (or lack thereof), of our software which dissuades or disallows a user to use our service is inherently a risk. It is thereby of no less important to consider these aspects than aspects relating to the former, 'Security and data integrity', risks section.

#### 1. **Security and data integrity**
This category of risks, broadly covers aspects of our software wherein exist the possibility of a negative impact, on account of actions relating to the electronic handling of our users personal information. By extension, this includes the way in which our software manages the relevant meta information associated with each part.

Subcategories of this section that have been noted and will be accounted for are as follows.

- Personal data relating to a user is only accessible to the authorized user(s)
  - This relates to the raw information associated to each user account (and Child profile). Due to the server hosted nature of our software, it is crucial to the planned operations, that users be able to have their accounts hosted with us, being able to sign in / out for instance. In doing this, we would require some login system, and profiling of our users, such as name, email, etc. This personal information relating to each user must remain visible only to that user. In the case of a child's information, this applies to who has access to this information e.g. a Parent account.
  - This can be mitigated with a simple login terminal which authenticates that the user is who they say they are via a password and known account identifier e.g. email / username. This risk will be broadened with the next two risks.

- User accounts must be held secure using strong password enforcement
  - A password such as "abc123" is likely a password that would be guessed very quickly, and would risk unwanted people gaining access to sensitive personal information. For this reason it is important to disallow the users from creating their accounts with passwords that may be guessed easily/ brute forced, albeit at the cost of easy memorization.
  - This can be easily implemented using enforced password characters such as having at least one uppercase letter, lowercase letter, special symbol (#!%"£$& etc.), number. Additional rules may be forced such as disallowing sequential patterns e.g. ABC, MNO, 123, 7890, qwerty. Since patterns like these are also easy to guess. This rule could be implemented as "any series of sequential numbers 3 or more is not allowed, in any part of the password". Finally, although not enforced, the user may be warned if a series of numbers matches a date like sequence e.g. DDMMYYYY or YYMMDD etc.

- User account login credentials, such as passwords, must not be stored as plaintext
  - In a worst case scenario e.g. a data breach, wherein our stores of user data are accessed without proper authorization and/or made public. It is important that the party perpetrating the attack does not gain access to all the users passwords. If such an event were to occur, and login information including plaintext passwords became public, this would allow any unauthorized user to access any other users information, both of the parent account type, and the child. Additionally, it is not uncommon for the public as a general populace to reuse their respective login credentials. Should our store of login credentials become compromised, it may risks malicious action to more vital information such as banks or work accounts, unrelated to the application itself.
  - This can be mitigated by storing a hashed version of the password—a scrambled form generated by a hashing function. The hash must consistently produce the same output for the same input, allowing the system to verify passwords by comparing the stored hash with the hash of the entered password. If they match, the password is correct. This approach avoids storing the actual password while still enabling secure authentication. An effective implementation of this may be to use a combination of a common password hashing algorithm e.g. Argon2 (state of the art for modern cracking attacks), with some 'salt'. Salt is unique random series added to each password in case two people have the same password by chance.
  
- The meta information, such as the implied relation between users must remain hidden 
  - Since our software relies on an entity relationship model of sorts, e.g. Parent user account, which can view multiple child profiles. It is also important that the non explicit information about users is also hidden. For instance, without knowing the name of an account, it is possible to determine who is who by how the accounts link together. This where possible should be minimised. This is an exemplary issue that by its nature, cannot be fully eliminated. The links, inherent to the program must always be there. None the less, they can be minimised to some degree.
  - Use of indirect identifiers can cloud the relationships e.g. hashed references. This paired with a separate "mapping" layer of sorts, handling relationships, accessible only with strict authenticated and access would minimise this risk substantially. Additionally, compartmentalization can be taken advantage of to ensure nothing can see anything its not supposed to see.

- Information must be able to be shared only with authorized users (When authorized)
  - Our software will be setup such that one child's information can be accessible to multiple accounts (e.g. a parent or caretaker). The respective parent / main child guardian, must be able to share their child's  with relevant parties, whilst maintaining that no others gain access to it.
  - A simple way to avoid this is via access tokens. Simplified for the end user, the parent may be able to generate an access token to the child, which allows another specified user to view (and/or edit) the child's information. When no longer needed, the parent may revoke the access token, in turn removing that person accessing the child's information. It is important, for this to work, that only the parent of the child has access to the creation / deletion of these access tokens.

- Users, who opt in to share their data for academic study, must remain anonymised
  - One feature our software aims to provide is a means by which parents can opt in to allow their child's (non identifying) information to be shared for the purposes of non profit academic endeavours. e.g. Student research. Once a parent has opted in, it is important that the child's information is presented anonymised and without any form of identifiers that may reveal the child in anyway.
  - This can be mitigated using two key ideas. Firstly, the public set of data, the anonymised information must be published naturally, with no way of identifying which entry belongs to which child e.g. Using an ID that is unrelated to the child's personal ID. The child profile would know which public entry is its, but the public entry will store no information as to which child it belongs to. The second, to mitigate tracking, is to stage updates of this public data set e.g. update all entries at the end of the calendar month at once. This would disallow the public from knowing which child is associated which which update. Additionally, specific information that may cause issues e.g. specific food eaten / medication taken may be omitted and/or remove exact timestamps of events to further anonymise information.

Some other ideas that are not planned for our software, but may be worth looking into at a later date are listed here.
- 2FA authentication
- Session timeouts
- Registered devices 


#### 2. **Usability and accessibility**
This category encompasses the risks that may directly or indirectly hinder the seamless use of our software for certain groups of users. These risks include potential barriers that may arise from the design, navigation, functionality choice or other miscellaneous aspects. This category is targeted particularly for individuals who rely on assistive technologies or require adaptations to accommodate specific needs. Addressing these risks ensures that our software remains inclusive, and usable for all users.

Subcategories of this section that have been noted and will be accounted for are as follows.

- The app must be accessible for people who colour impaired/ blind
  - This applies effectively exclusively to this subset of people only, as there is no intended use for any other user group to find benefit from seeking the same accommodation as this. Put short, some of our users may have their colour vision effected and come under one of the three colour blind types : protanopia, deuteranopia, tritanopia or complete colour blindness achromatopsia. It is crucial that our software remains functional for these users with no part failing as a result of missing colour.
  - To combat this, By default as a general rule one colour(or shade) on top of another should not be the same 'brightness'. In a worst case scenario, a fully colour blind individual would see the whole page in shades of grey, thus anything with similar brightness will end up being indistinguishable. Ensuring that our website as a base, can work for this worst case, it will be guaranteed to work for the lesser cases too; partial colour blindness. Additionally, in the settings, we intend to add specific 'colour profiles' for each specific colour deficit. These colour profiles would change the colours used across the website enough to make them even more visible, while keeping the feel of the website true to its original nature. These colour profiles would be accessible from the settings. We have planned ahead with this issue, having implemented the colours for our website as a set of variables shared throughout all the pages; Changing these root colour variables would uniformly update the whole website allowing for easy colour profile editing.
- The app should have colour profiles for different environments
  - This is targeted towards people who may not be affected by colour visibility impairments, but still prefer specific widely adopted colour profiles. This may be for any number of reasons, but typically it is as a result of the need to reduce eye strain when operating in low light level environments; A bright screen against a dark room will strain the eyes and cause discomfort to the user
  - This issue is very similar to the prior one but results from a slightly different set of needs, but as such can be resolved with an almost identical method. Should the user wish, they should be able to once again, navigate to the settings and choose another colour profile. This set of colour profiles however would target these different needs. Exemplary colour profiles for this risk may include a for instance, a dark theme or a sepia theme. Both widely adopted styles which both reduce eye strain in low light level environments.
- Buttons should be easy to press
  - Given that our software is planned to include the functionality of logging child activity e.g. sleep etc. it is important we accommodate for people who may have difficulty navigating our software, who have difficulty managing software in general. This includes, but is not limited to, people such as those who suffer from parkinson's, and may have a hard time targetting a button which is small, and neighbouring closely with other buttons. This may result with an infuriating user experience which would drive users away from our software.
  - The mitigation of this is held entirely within the graphical design of our website and as such can be easily aided via simple editing to the CSS of our software. For instance, changing the size of buttons, the spacing between neighbouring buttons and crowding of elements on a screen, the affected user would find it easier to navigate the software and complete the actions they had intended to complete.
- Text should not be hard to read
  - The last factor to consider is the possibility that some of our users may have reading impairments, whether that be due to needing the aid of reading glasses, or having some form of dyslexia that contributes to their inability to correctly digest texts. A user who has difficulty managing these conditions or similar conditions may find it difficult to navigate the core functionality of our software.
  - To minimise the poor user experience felt by this group of users, our software can adapt to accommodate, while not taking away from the user experience of unaffected users. Ensuring legibility over the entire website would allow these users to navigate the software and resolve this issue. To enforce an acceptable quality of legibility, it can be formalized a single typeface across the whole website which favours readability. This is in contrast to a typeface which may be harder to read in small texts.


