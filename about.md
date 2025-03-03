# About the Project

This is a **Django-based web application** designed to **centralize health tracking for children**, making it easier for users to monitor and share health data.

## Key Features

**User Registration & Child Profiles** :

- Parents or carers can sign up as a User, to start using the app, or view the app as a guest with example data
- Users can either create a new child or import an existing child using a private, single use, share code.

**Health Data Tracking** :

- Users can log and track a child's growth, food intake, sleep and medication.
- User can view Data graphically on each tracking page via graphs, and view summary info on the dashboard

**Profiles And Permissions** :

- Users can edit their own profile and edit a child's details (Including customizable profile picture)

**Data Export & Sharing** :

- All logged data can be exported as a PDF for easy printing and sharing with a health practitioner or other caregivers

**Security** :

- Authentication
  - Users Login and Registration handled with Secure authentication system
  - Passwords are hashed using SHA256, never stored as plaintext
- Role-Based Access Control (RBAC)
  - Only Primary guardians of a child had edit permissions of a child
  - Only Primary guardians of a child can view the secret share code of a child
  - Only Primary guardians of a child can export a PDF with the share code of a child
  - Admin users can manage users and data as needed
- Share code system
  - Share code is only randomly generated
  - Share code regenerated use preventing multiple use of the same code
  - 62¹⁰ unique codes (839 quadrillion), making guessing infeasible
- CSRF & SQL injection prevention
  - CSRF tokens used, preventing Cross-Site Request Forgery (CSRF) attacks. See implementation report for more info.
  - Data stored using Django's secure ORM preventing SQL injection

## Prerequisites

1. Check Python

   ```console
   python --version
   ```

   If not installed, download from : <https://www.python.org/downloads/>
2. Git

   ```console
   git --version
   ```

   If not installed, download from : <https://git-scm.com/downloads>

## Post Installation (Starting the App)

If you have installed the app before, you can start it quickly:

(If you haven't installed it yet, skip to the Installation Guide below.)

1. Navigate to the project directory

   ```sh
   cd 24-25_CE201-col_team02
   ```

2. Run the startup script

   ```sh
   .\startup.ps1
   ```

## Installation Guide

### Automatic Installation (Windows Only)

1. Clone the repository

   ```sh
   git clone https://cseegit.essex.ac.uk/24-25-ce201-col/24-25_CE201-col_team02
   cd 24-25_CE201-col_team02
   ```

2. Run the setup script:

   ```sh
   .\setup.ps1
   ```

### Manual Installation

1. Clone the repository locally

   ```sh
   git clone https://cseegit.essex.ac.uk/24-25-ce201-col/24-25_CE201-col_team02
   cd 24-25_CE201-col_team02
   ```

2. Set up a Virtual Environment

   ```sh
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # MacOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies

   ```sh
   pip install -r requirements.txt
   ```

4. Run database migrations

   ```sh
   # Use relevant python version for you system
   python manage.py migrate
   ```

5. (Optional) Create an admin user

   ```sh
   python manage.py createsuperuser
   ```

6. Run the development server

   ```sh
   python manage.py runserver
   ```

7. (Optional) Load example data

   ```sh
   python manage.py loaddata fixtures\example_data.json
   ```
