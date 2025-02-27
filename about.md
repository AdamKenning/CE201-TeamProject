# About the Project

This is a django web based application that aims to centralize the health tracking of children for the sake of easy monitoring and sharing between users. 

## Features

- Feature 1
- Feature 2

## Prerequisites

1. Check Python

   ```console
   python --version
   ```

   If not installed, download from : https://www.python.org/downloads/
2. Git

   ```console
   git --version
   ```

   If not installed, download from : https://git-scm.com/downloads

## Post Installation

If you have previously installed the app, then you can start the app more easily using.
If you have not, skip to the installatoin guide.

1. Set your location
   ```
   cd 24-25_CE201-col_team02
   ```
2. Run startup.ps1
   ```console
   .\run.ps1
   ```

## Installation (Auto) (Windows Only)

1. Clone the repository locally
   ```console
   git clone https://cseegit.essex.ac.uk/24-25-ce201-col/24-25_CE201-col_team02
   cd 24-25_CE201-col_team02
   ```
2. Run setup.ps1
   ```console
   .\setup.ps1
   ```

## Installation (Manual)

1. Clone the repository locally
   ```console
   git clone https://cseegit.essex.ac.uk/24-25-ce201-col/24-25_CE201-col_team02
   cd 24-25_CE201-col_team02
   ```
2. Set up a Virtual Environment
   - Windows
     ```console
     python -m venv venv
     venv\Scripts\activate
     ```
   - MacOS
     ```console
     python3 -m venv venv
     source venv/bin/activate
     ```
3. Install project requirements
   ```console
   pip install -r requirements.txt
   ```
4. Run database migrations
   ```console
   python manage.py migrate
   ```
5. (Optional) Setup Admin access
   ```console
   python manage.py createsuperuser
   ```
6. Run the server
   ```console
   python manage.py runserver
   ```
7. (Optional) Load initial example data
   ```console
   python manage.py loaddata fixtures\example_data.json
   ```
