add users stories for accesibility etc
- colours
  - no red blue green etc
  - sepia
  - greyscale ?
  - dark mode ?
- reading
  - dislexia
    - large clear text
  - parkinsons
    - large buttons




# User Stories MD

---
## Explanation and example

- ### User Story Structure
  - User stories are often expressed in a simple sentence, following a simple structure.
    - “As a **persona**, I **want to**, **so that**.”
  - Explanation of Parts
    - As a **persona**: Defines the user role, like "parent" or "caregiver."
    - I **want to**: Specifies the action or feature the user needs to use.
    - **So that**: Explains the purpose or value this feature provides.
  - This structure ensures that each user story aligns with the software’s goal of supporting child health management 
      and providing actionable insights to users.
  - Source : https://www.atlassian.com/agile/project-management/user-stories
---
## User Stories 
### For Parents
- Tracking Patterns:
  - As **a parent**, I want to **track my child’s feeding, sleep, and diaper patterns** so that I can **establish a healthy routine and monitor their health**.
  - As **a parent**, I want to **log my baby’s feeding times, amounts, and sleep start/end times,** so I can **track nutrition and rest patterns and share these with my paediatrician**.
- Insights & Alerts:
  - As **a parent**, I want to **receive insights and alerts on my child’s routines** to **identify changes that might indicate health issues**.
  - As **a busy dad**, I want **easy access to summaries of my child's daily routines and development** so I can **stay informed and support my partner**.
- Growth Tracking:
  - As **a parent**, I want **to enter my child’s height, weight, and head size over time** so that I can **monitor growth and compare it to standard growth standards for their age group.**
- Data Entry & Access:
  - As **a parent**, I want to **enter data quickly using simple fields**, so **I don't take time inserting information every day**.
  - As **a parent**, I want to **use the software on my smartphone and tablet,** so I can l**og and check information anytime, anywhere**.
- Data Security:
  - As **a parent**, I want **assurance that my data is safely secured** and **so my childs private info is kept private**.
### For Caregivers
- Diaper Tracking:
  - As **a caregiver**, I want to **record diaper changes** so that I can **monitor the child’s digestive health**.
- Health Reporting:
  - As **a caregiver**, I want to **generate daily health reports in PDF format** so I can **provide updated information during healthcare visits**.
- Medication Scheduling:
  - As **a caregiver**, I want to **schedule and track medications** according to a doctor’s prescription **to ensure correct dosage and timing**.
### For Healthcare Providers
- Growth Metrics Access:
  - As **a healthcare provider**, I want **access to growth metrics** so that I can **assess if a child is developing normally**.
### For Students & Researchers
- Anonymised Data Access:
  - As **a student studying Child Development**, I want **access to anonymised child health and wellness data** so I can **analyse patterns in sleep, growth, and nutrition for research or coursework**.
### For School Staff
  - Health and Allergy Management
    - As **a school nurse**, I want **access to allergy information and vaccination history** to **ensure compliance with health requirements**.
  - Medication and Health Records
    - As **a school nurse**, I want to **log and track medications administered to students**, including symptoms and health complaints, to **maintain accurate health records and communicate with parents as needed**
  - Incident Reporting and Notifications
    - As **a school nurse**, I want to **quickly notify parents/guardians about health incidents or concerns** to **keep them informed and coordinate necessary follow-up care**.
  - Emergency Preparedness
    - As **a school nurse**, I want to **receive notifications for students with high-risk conditions** and have access to emergency action plans to **respond effectively during health incidents**.
### Additional (Cross-role) Features
- Interactive Summaries & Graphs:
  - As **a parent or caregiver**, I want **interactive graphs and visual summaries** that show changes over time so i can **quickly assess development**.
- Quick Summaries & Notifications:
  - As **a parent or caregiver**, I want **quick summaries and alerts for key health updates** to **stay engaged and informed**.

--- 
## Extracted software requirements
### General Requirements 
1. Multi-Device Access
   - Mobile & Tablet Support
     - Ensure the app is available on multiple device types for convenience
2. Data Security & Privacy
   - Privacy
     - Ensure that personal data is secure and accessed only by authorised users.
   - Secure Sharing & Permissions
     - Provide a secure way to share access with authorised caregivers (e.g. parents, nannies, school).
3. Simple & Efficient Data Entry
   - Frequent Tasks
     - Include quick inputs / one-click options for common entries (like feeding, sleep, and diaper changes).
   - Custom Fields
     - Allow users to add custom fields, especially for non-standard metrics they may want to track.
4. Alerts & Notifications
   - Customisable Alerts
     - Allow users to customise alerts (e.g. feeding/sleep times) to prevent notification overload.
   - Smart Alerts
     - Include intelligent alert thresholds (e.g., significant changes in feeding, sleep, or growth).
5. Report Export & Sharing Options
   - Export Formats (PDF/CSV)
     - Provide options to export reports in PDF or CSV formats.
   - Daily/Weekly Reports
     - Offer a simple option to generate daily or weekly summaries.
### Parent & Caregiver-Specific Requirements
6. Health Insights & Comparisons
   - Insightful Analytics
     - Provide insights into possible health issues (e.g. feeding or sleep irregularities)
   - Growth & Health Comparisons
     - Include comparisons with standard health metrics based on age, height, and sex
   - Routine Averages
     - Show averages (e.g., daily feeding or sleep hours) to help see patterns and trends over time
7. Growth & Routine Tracking Over Time
   - Interactive Visuals
     - Provide interactive graphs that track growth (height, weight, etc.)
   - Projection Features
     - Use historical data to project future patterns e.g. continued growth.
8. Offline Functionality
   - Offline Access & Syncing
     - Ensure the app has offline capabilities, allowing parents to log data without an internet connection (to be synced when online)
### Healthcare Provider-Specific Requirements
9. Healthcare-Focused Reporting
   - Standardised Growth Charts
     - Integrate standard growth charts for healthcare providers
   - Detailed Growth Metrics
     - Include precise growth data, especially height, weight etc
10. Anonymised Data Options
    - Anonymisation for Research
      - Provide anonymised data access for authorised students/researchers
    - Opt in anonymous data sharing
      - Allow for users to opt in and share data points for data banks etc.
### School Staff (Nurse) Requirements
11. Allergy & Health Information Summaries
    - Emergency Summary Info
      - Include an easily accessible summary of allergies / health notes etc
    - Log and Track Health Incidents
      - Provide functionality to log medications administered, health complaints, and other relevant notes to maintain accurate health records and communicate with parents as needed.
    - Customisable Fields for Allergy Data
      - Allow school nurses to access or add notes to a childs health record e.g. feeling sick at school.
    - Emergency Preparedness
      - Enable notifications for high-risk conditions and access to emergency action plans to respond effectively during health incidents.
---
## App overview and Goal
- Overview
  - This app is designed to assist parents, caregivers, healthcare providers, and other authorised users in tracking and monitoring a child’s daily health and development data. It offers an intuitive interface for logging, viewing, and analysing essential health metrics, enabling users to establish healthy routines, identify potential health issues, and ensure that all caregivers are kept informed.
- Goal
  - The app aims to provide a centralised, secure, and insightful platform for tracking a child’s health and routines. By facilitating informed decision-making and proactive responses to potential health issues, the app supports the child’s growth and wellbeing effectively, while also ensuring seamless communication among caregivers and healthcare providers.