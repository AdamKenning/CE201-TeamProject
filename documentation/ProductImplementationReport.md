# Product Implementation Report

| Quick Info |               |
| ---------- |---------------|
| Author     | Adam Kenning  |
| Finished   | March 5, 2025 |
| Word Count | 8,478         |

## Table of Contents

1. [**Technical Diagram**](#1-technical-diagram)  
2. [**Technical Description**](#2-technical-description)  
   2.1. [Model View Template](#21-model-view-template-mvt)  
   2.2. [Other Areas](#22-other-areas)  
3. [**Data Structures and Algorithms**](#3-data-structures-and-algorithms)  
   3.1. [Data Structures](#31-data-structures)  
   3.2. [Algorithms](#32-algorithms)
4. [**Known Issues**](#4-known-issues)  
   4.1. [Frontend](#41-frontend)  
   4.2. [backend](#42-backend)
5. [**Imported Libraries**](#5-imported-libraries)  
   5.1. [Environment Dependency](#51-environment-dependency)  
   5.2. [Direct Dependencies](#52-direct-dependencies)  
   5.3. [Transitive Dependencies](#53-transitive-dependencies)  
6. [**Licenses**](#6-licenses)  
   6.1. [Django](#61-django-extract)  
   6.2. [Charts.js](#62-chartsjs-full)  
   6.3. [Pillow](#63-pillow-full)  
   6.4. [ReportLab](#64-reportlab-full)  
   6.5. [FontAwesome](#65-fontawesome-extract)  

## 1. Technical Diagram

![Django Graph](image/TeamEffortLog/Adam-Graph-Model.svg)
Visual representation of our Django models, including both default Django models (E.g. User from django.contrib.auth) and Chawts custom models (E.g. Child). "models", explained in more detail later, are how tables for a database and table entries are described in the django framework. This graph shows the relationships between all the various tables in our database.

## 2. Technical Description

The CHAWTS App was developed using the Django framework, a predominantly Python based framework, using the *MVT* architecture to allow for simple expansion and cohesion. MVT (Model-View-Template), similar to the *MVC* (Model-View-Controller), splits the app into three distinct main layers that all communicate with each other (with additional areas i will touch on later). These three layers each run from their respective single python file.

### 2.1. Model-View-Template (MVT)

---

#### Models

This represents the database structure; How the database is stored and structured, each class in **models.py** represents a distinct database table e.g. "Child" Database Entity implemented using Python Class

1. **models.py** (extract): (Author, Adam)

   ```python
   ...
   Class Child(models.Model):
      # A foreign key constraint linking child and parent via a third table
      parents = models.ManyToManyField(User, through='FamilyAssociation', related_name='children')

      # Regular data storing basic information for human identification
      firstName = models.CharField(max_length=50)
      lastName = models.CharField(max_length=50)
      dateOfBirth = models.DateField(default=None)

      # Stores the URL of a profile picture for the child
      profile_picture = models.ImageField(upload_to=profilePicUniqueUpload,blank=True, null=True)

      # A dynamic, single use resetting code for child sharing (e.g. multiple parents)
      shareCode = models.CharField(max_length=10, unique=True, blank=True, null=True)
      # The function for the code resetting
      def shareCodeGenerate(self):
         self.shareCode = get_random_string(length=10)
         self.save()

      # A descriptor for the table
      class Meta:
         db_table = "chawts_child"
   ...
   ```

Each model created subclasses the django.db.models.Model which implements the basic functionality shared between all models. To quickly run through the parts Models.py that make up the functioning of the database:

1. **ProfilePicUniqueUpload** : (Author, Adam)

   This is the only standalone function in models.py, and it serves to generate unique file name replacements, using *UUID4* (Universally Unique Identifier version 4) for files uploaded e.g. profile pictures. This is to mitigate the risk of multiple people uploading profile picture files that share a common name, overwriting each other when stored on the server.
2. **Profile** : (Author, Adam)

   A class that has a one-to-one relationship with the default Django *User* Model. Django already has a preset user model which has most of the functionality our app needed. *Profile* is used to "extend" the *User* model to allow for custom fields such as *profile_picture*.

   The default django User model includes typical fields such as *username*, *password*, *email* etc. But also includes fields that allow for tracking of users engagement e.g. *is_active*, *date_joined*, *last_login*. Finally, it contains fields relating to administration; *is_superuser*, *is_staff*.

   These two classes, *Profile* & *User*, are how the parent/ guardian logging into and using our app, will be stored.
3. **Child** : (Author, Adam)

   Represents the children that are being tracked using our software, the first four fields are simple enough *firstName*, *lastName*, *dateOfBirth* and *profile_picture*, which functions the same as in the *Profile* class.

   the *parents* field is a foreign key link to the next class *FamilyAssociation*.
   The *shareCode* field is a 10-character randomized string used to grant access to a child's profile, allowing multiple caregivers (e.g. two parents and a childminder) to log data for the same child. This code is single-use—once redeemed, it is automatically reset to a new random string. Only the primary parent (explained later) can access and generate this code, ensuring a secure and controlled sharing process while preventing unauthorized users from repeatedly distributing access.
4. **FamilyAssociation** : (Author, Adam)

   Since one user may need access to many children, and one child may be accessed by many users, this becomes a many-to-many relationship. This table exists to store which *User* entity has access to which *Child* entity.

   There are two foreign key constraints, one for the *User* (parent) and one for the *Child*. Additionally there is a single boolean value *is_primary* which indicates which user is the primary guardian of the child, typically this is whichever user initially created the child on in the app prior to sharing the child. This primary user is granted authoritative rights such as deletion and access to the child's share code.
5. **Log** : (Author, Adam)

   Our apps primary purpose is tracking the data associated with a child. Every data point is stored as a log allowing for quick querying and easy data manipulation. There are various log types for the data we track, but they all have some fields in common, Thus the default *Log* class holds common fields that the other log classes can then extend off of. Note : This Class is never directly used itself.

   Fields include the log *type*, Two dateTimeFields for the time the Log was submitted and the time the User states the log was for (e.g. retroActively adding some data for a past event). A foreign key constraint field for a specific child allows the logs to be linked correctly, since a particular log can only describe an event of a particular child. Then the *comment* field exists simply for User notation (akin to additional information).
6. **SleepLog**, **FoodLog**, **GrowthLog** : (Author, Adam)

   These tables store the logs for the category specific data, and extend of the basic *Log* class for added nuanced fields. For example, *FoodLog* Extends *Log* with a field *mealType*. *mealType* is dependent on the child's age; A child younger than 6 months has a different selection of meals than an older child.

   Similarly, the other *Log* extensions implement their own respective fields for tracking data unique to their category.

---

#### Views

The View is where the CHAWTS app logic happens, it processes user requests, Interacts with model and determines what data to serve to the user. This intermediary layer is akin to the "Brains" of the whole App. In a similar way as the django Model, a "view" is written as a Python Function in a single Python files **views.py**.

Each view takes a request from the user (The request taking different forms depending on the use case), and processes it. Based on this request, a view may conditionally retrieve some data from the model database, and pass this data back to the user alongside a given template.

For example, the view changeProfile, used for updating the users profile picture

1. **views.py** (extract): (Author, Adam)

   ```python
   ...
   # Declare this view only accessible if logged in
   @login_required
   def changeProfile(request):
      # Get the users profile from the backend
      profile = Profile.objects.get_or_create(user=request.user)

      # When filling out a form, Post is used to send data to the backend
      if request.method == "POST":
         # Retrieve the Form from request (this would include the profile picture)
         profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

         # Check if the form is correct, and if so, save the data
         if profile_form.is_valid():
               profile_form.save()

               # Redirect back to the current page to the update (refresh)
               return redirect('changeProfile')

      else:
         # If the user is not submitting a form, show them an unfilled form
         profile_form = ProfileForm(instance=profile)

      # Server the user the page html, with the relevant form
      return render(request, 'management/changeProfile.html', {
         'profile_form': profile_form,
      })
   ...
   ```

Most of the views serve similar purposes, however there are some that do not conform. I will discuss the implementation of these views briefly.

1. **Dashboard** : (Author, Adam)

   By far the largest of the views, this handles all the technical side for the Dashboard, Landing for the website and thus serves to provide quick general information as well as general functionality.

   For a person visiting our website, it was important for us to display exemplary information so as to allow a guest to view what the website may look like for them. To allow this, the first check is against if the user is "Authenticated"; logged in. If the user is not logged in (guest), various data that would have been served to the front end is served as blank (This empty data is dealt with and populated later with false example data)

   If the user is logged in, firstly the method gets a specific child id from the session storage (session storage is used to hold temporary information across pages). The child referenced in the session storage is the selected_child*. The specific age of this child is then calculated from the users current date against the selected_child's dataOfBirth field.

   Dashboard is used to select a specific child for the other pages. This aside the dashboard itself is used to show the user general non-specific data about their children. For this, two distinct data sets are generated. These both describe the proportions of data that has been logged for all the children, using different comparators for better data analysis.

   1. Data logs per child
   2. Data logs per category

   All of the various data generated in this view is then passed to the user alongside the dashboard.html template.

   *selected_child : One of the children, selected by the users, from the children associated with that user. This child is then able to be used later to declutter pages by only showing data relevant to that singular child at a time.
2. **sign_Up** : (Author, Adam)

   This view checks the contents of its request, to see if it is a posted form. If is it, and the form is valid, it saves the sign up information as a new user and immediately attempts a login on the newly created user.
3. **growth**, **sleep** : (Author, Adam)

   Both of these these views function for their respective growth and sleep pages.

   For these views to be valid, the user first must be logged in, since as a guest there is no specific data for any children to display. Additionally, a check is done to retrieve the selected_child from the session Id, if a child has not been selected, there once again is no data to show and the user is redirected to the dashboard.

   If these checks are passed, the views pass this selected child alongside the respective pages html template to the frontend.
4. **Food** : (Author, Adam/Charles)

   The food view, is similar to the prior growth and sleep, working on similar logic. However, for the food View, additional information is needed:

   1. chart_data :
      Two sets of data relevant for the data visualizer on the Food page, consisting of the data's labels and calories per meal.
   2. Meals :
      A single set of data of each meal taken.

   This data is passed alongside the selected child and the food.html template.
5. **settings** : (Author, Adam)

   Servers the settings.html template to the user. This page has not had much work done on it, so the view is very simple.
6. **select_child**, **deselect_child** : (Author, Adam)

   These two views allow for the heavily selected_child functionality used heavily across the app. Both views require the user to be logged in.

   Selection is done by using the child_id passed as a parameter of the function alongside the request and setting that id in the current session as 'selected_child_id'. Deselect works in reverse, Checking if the token exists in the session, and deletes it.

   These views then redirect to the dashboard (refresh the page), to reflect the changes.
7. **create_child** : (Author, Adam)

   Used for initiating new child entities, this function takes the form from the requested data parameter. If the requested form is valid, it creates a new child object, without committing the creation of the child. The code for the half-created child is generated, then the child is saved properly.

   A new entry in the family associations table is then created to represent the link between the user who requested the creation of the child and the child itself.

   On successful completion of these steps, the view redirects the user to the dashboard to reflect the new child creation changes.
8. **add_child** : (Author, Adam)

   To enable the many-to-many relationship used in our CHAWTS app for multi-child-parent relationships, the addition of pre-existing children is necessitated. This view implements this functionality by taking the form from the requested data and processing the extracted share code imputed by the user in that form.

   If the code is an invalid code; there exists no children with that specific share code, an exception is thrown and the user is redirected back to the dashboard.

   However, if a child does exist with a matching code, the child can be linked to the user. A new entry in the familyAssociations table is created between the child and the user, wherein the user is not the primary parent of the user. The child's specific shareCode is then reset to a new random string (to prevent misuse), and finally the user is redirected back to the dashboard.

   On the dashboard, if the share code was successful, the user will see the new child amongst their pre-existing children allocated to them.
9. **edit_child** : (Author, Adam)

   To allow for the post-creation editing of a child details (e.g. mis-input of a name, or to update a profile picture), the edit_child view is needed. Alongside the selected_child, this view has a is_primary check present, referring to the child's association to the parent in the FamilyAssociation table.

   If the parent is the primary parent of the child. If the user is not the primary parent of the child, the user is denied access to the view, and redirected to the dashboard. If the user is the primary parent, they are able to submit a new form through the request parameter of the function.

   This form is checked for validity and submitted. The html template is then rendered to the user alongside the form as well as the currently selected child.
10. **changeProfile** : (Author, Adam)

    This view is similar to edit_child, but for the user. Since it is the user who would call this view, to change their own profile, their are minimal security checks needed.

    As long as the user is logged in, the view retrieves the form from the requested data, checks its validity and saves the form, updating the user profile. The user is then redirected to the same page (refreshing it), to reflect the new changes.
11. **pdf_children_all** : (Author, Adam)

    An intermediary view used in curating the PDF document for exportation of logs. All this view does is calls the next view "pdf_file_children_all", and returns that views output as a file "childrenAll.pdf"
12. **pdf_file_children_all** : (Author, Adam)

    This view serves to generate the raw PDF file itself, needed in the prior function to return to the user. To do this, it makes use of the canvas object from the required import reportLab to customize the PDF document, and the BytesIO from the default io import, for system in/outputs.

    This canvas object can be written to using simple commands. For example, using the below *canvas_out* object, the string "test" can be written at position (x,y). Methods exist to add effects (e.g. font size, bold, underline), but this is the basic idea.

    ```python
    ...
    canvas_out = canvas.Canvas(BytesIO())
    canvas_out.drawString(x,y,"test")
    ...
    ```

    The pdf_file_children_all view dynamically generates the logs based off each child's specific logs. It does this by iterating over every log, for every child, and writing to the canvas all data. An internal helper function is used *drawLog* used for automation of repetitive step such as indentation for uniform formal readability.

    As well as the logs for the respective children, the specific details of each child area also appended to the document (name,age, share code etc), and the User who requested the PDF document.

    Once complete, the PDF document is shown to the user and saved to the users device, before returning this PDF document up to the previous view.
13. **testing** : (Author, Adam)

    This view, although not intended to be continued should this project be used as a real viable product, still serves a purpose nonetheless in the meantime. Due to the questionable state of the App (its pages, wherein the user is meant to be able to log data, not existing or barely functional) there is no way to log data for experimental debugging use.

    Thus this view exists. It is merely while the APP is in development, to allow for temporary functionality. This view operates alongside its respective testing.html template, providing a page for a developer to manually log every kind of data at once from one place.

    Initial checks are done as per the other food, growth and sleep logging pages, checking if the user is first logged in, and if there is a child selected in the session. If these are passed, three forms for food, growth and sleep are created (for food, the 6 months exception is applied)

    After this, a check is done against the request method, if it is POST (the user is sending a form across), the respective form handling code will trigger. This is conditional on what type of from is in the request POST. For the respective form type, the form is validated, saved without committing and then associated with the selected child. After this the page is redirected back to testing (refresh), and the relevant forms are served for the user.

---

#### Templates

The template layer is what the user themselves interacts with. It is the front end of the website, responsible fore rendering the HTML, CSS etc to the users screen. Django's templating engine allows for effective embedding of Python-esc logic (e.g. conditionals, for-loops) within the HTML files which is made heavy use of across the respective template HTML files.

Another key function habilitated by the Django templating is the ability to extend one HTML document off another. For instance, in our project there are two token examples of this, from base to base-sidebar, and from base-sidebar to most other pages. Base is the most basic form of any page, containing HTML common to all pages, and links to a base.css with common styling for all pages.

Templates receive data from the views (if needed) and format it accordingly ready for display. For example a relatively simple template, changeProfile.html

1. **changeProfile.html** (full): (Author, Adam)

   ```django
   <!-- Extending of the base.html template -->
   {% extends "base.html" %}
   <!-- Generate dynamic filepath to static (css and other files) -->
   {% load static %}

   <!-- First base.html extension -->
   {% block headExtra %}
      <!-- Custom CSS stylesheet for the page -->
      <link rel="stylesheet" href="{% static 'css/shared.css' %}" type="text/css">
      <title>Profile</title>
   {% endblock headExtra %}

   <!-- Second base.html extension -->
   {% block bodyExtra %}
      <main>
         <!-- Greet user with django entity using "{{entity}}" -->
         <h2>Hello {{user.username }}</h2>
         <!-- Django conditional check -->
         {% if user.profile.profile_picture %}
               <img class="pfp" src="{{ user.profile.profile_picture.url }}" alt="Profile Picture">
         {% else %}
               <img class="pfp" src="/static/images/default.jpg" alt="Default Profile Picture">
         {% endif %}

         <!-- Creation of form for data input -->
         <form class="form" method="post" enctype="multipart/form-data">
               <!-- Setup of CSRF protection token -->
               {% csrf_token %}

               <h2>Upload profile image</h2>
               <!-- Loads the django form -->
               {{ profile_form.as_p }}

               <!-- Buttons for submission and navigation -->
               <input class="button" id="button" type="submit" value="Submit"/>
               <a class="button" href="{% url 'dashboard' %}">Dashboard</a>
         </form>
      </main>
   {% endblock bodyExtra %}
   ```

**A Cross-Site Request Forgery (CSRF) protection token is a security preventative measure used in all form across out APP. A CSRF attack occurs when a malicious external website tricks users into doing unintended actions on a local (in this case our) site, when the user is authenticated. The CSRF token is generated for every form submission and is checked against the CSRF token in the users session. If it is missing, or incorrect then the form is rejected.**

There are too many templates to cover them all (20 in Total), and they are fairly repetitive as well, so i will cover some notable instances.
Broadly there are three Categories of templates, grouped by the role they serve in the application. In the project directory "24-25_CE201-col_team02\djangoProject\chawtsApp\templates", you will see they are grouped similarly. This is a choice predominantly for organizational reasons, though it does simplify some other areas (e.g. local page linking)

1. **management** : (Author, Adam/Zaki)

   These templates serve as the pages that are used by the user to alter various things (post registration). This includes changing the users profile, management of the children allocated to that user (creation, addition and editing), and access to the settings template. With exception to the settings template, authored by Zaki, All the other templates in this category were authored by Adam
2. **registration** : (Author, Adam)

   These templates are ones which are needed to use the aforementioned default Django User model. Since Django has some default user management handling, it was the obvious choice to use this; our applications focus is not directly on the user, and thus the User wasn't too important. To Make use of this default User model, there are various operations needed to be done in a specific manner (e.g. User Authentication, Login etc). For this reason, most of the templates in the registration section, although hand written, follow very closely to the same templates in the Django documentation (including the name choice of the files and the directory "registration")
   That being said, the grouping of these files is due to their shared handling of the User in regards to Authenticating them. These templates include HTML files for logging in and out, changing the user password, and signing up.
3. **tracking** : (Author, Adam/Munashe/Charles/Evan)

   This collection of templates forms the core pages of our app, which is designed for tracking a user's child's health data. The app includes unique pages for analysing different aspects of the child's health. These templates cover various subcategories, such as food, growth, and sleep.
4. **misc** : (Author, Adam)

   his last set contains all the rest of the templates, with minimal to no commonality. In the directory mentioned above, these templates are loose, not organized into a particular folder. This is fine since this last set does not contain too many files. These files include the base template and the base-sidebar template, both of which are never directly used, only extended off of in different templates. As well as the landing page of the website, the dashboard, and the testing template; like the testing view, this template is here during development of the APP, and will not persist in later versions.

Although most of are fairly self explanatory, two key extracts i will exemplify are the templates base.html, and dashboard.html.

1. **base.html** (extract) : (Author, Adam)

   ```django
   <!-- Dynamically load static files (e.g. css, js, media) -->
   {% load static %}

   <!DOCTYPE html>
   <!-- Define the document type and sets the language to english -->
   <html lang="en">
     <head>
       <!-- Define character encoding -->
       <meta charset="UTF-8">

       <!-- Content Security Policy (CSP) -->
       <meta http-equiv="Content-Security-Policy" content="
         default-src 'self';
         script-src 'self' https://cdn.jsdelivr.net;
         style-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com;">

       <!-- Page description and keywords for search engines, and Author crediting-->
       <meta name="description" content="A health tracking application for children.">
       <meta name="keywords" content="chawts, child, health, tracking, growth, food, sleep">>
       <meta name="author" content="Adam, Munashe, Charles, Evan, Zaki, Zubair">

       <!-- FontAwesome for icons, and Charts.js for graphs  -->
       <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css" rel="stylesheet">
       <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

       <!-- Link to css & website icon -->
       <link rel="stylesheet" href="{% static 'css/base.css' %}" type="text/css"/>>
       <link rel="icon" type="image/svg+xml" href="{% static 'icons/LogoHeavy.svg' %}">

       <!-- Block for specific page headers -->
       {% block headSidebar %}
       {% endblock headSidebar %}

       {% block headExtra %}
       {% endblock headExtra %}
     </head>

   ...

   </html>
   ```

   This is the entirety of the base template, which all other templates, directly or indirectly, extend off of. This is evident with the Django block tags; Recall in the prior example changeProfile.html template. The matching block tags that surround code in extended templates, will have their code wrapped with this base.html code when before the final combined html file is served to the user. After this, there is some typical html setup, then a content security policy.

   **A content security policy (CSP) is security feature that prevents attacks such as Cross-Site Scripting (XSS) and data injection by restricting which resources (e.g. scripts, styles, images) can be loaded and executed. it defines a set of rules in the \<meta/> tag or HTTP headers, specifying trusted sources for types of content. This inclusion of a CSP significantly enhances security, especially important for our software which handles sensitive personal health data and general user data.**

   The rest of the code is fairly self explanatory, but briefly, The next section involves various meta names which aid in searching for the website in browsers through search engines, and some crediting to all the members involved in our team. Then there is some linking to FontAwesome which provides icons, and Charts.js for the data visualization across our website. Both of these services are open access and have been used in according with their licenses. See the licenses section at the end of this document.
2. **dashboard.html** (extract) : (Author, Adam)

   ```django
   ...
   <section class="graphAreaFirst">
       <canvas class="pieChart" id="pieChart"></canvas>
   </section>
   <section class="graphAreaSecond">
       <canvas class="barChart" id="barChart"></canvas>
   </section>

   <script src="{% static 'js/dashboard.js' %}"></script>

   {% if user.is_authenticated %}
   <script>
       window.isAuthenticated = true;
       window.childNames = {{ child_names|safe }};
       window.dataLogsPerChild = {{ data_logs_per_child|safe }};
       window.logCategories = {{ log_categories|safe }};
       window.logCategoryCounts = {{ log_category_counts|safe }};
   </script>
   ...
   ```

   This small extract from the much larger dashboard.html, is enough to explain how the Charts.js data is managed on our website. The two first section tags refer to the two graphs dynamically generated by Charts.js.

   **In principle, the backend View fetches data conditionally from the model.py (database), the View then passes this data directly to the frontend alongside the HTML template. Within the HTML template, the Data is passed again to the relevant Javascript file for the template (in this case dashboard.js) which is loaded in the template header. Within this Javascript file, the data is used to generate a graph using Charts.js which is targeted at the two sections above "graphAreaFirst" and "graphAreaSecond" which both hold canvas classes.**

   Below are relevant extracts from the remaining aforementioned files to illustrate the concepts

   **views.py** (extract) : (Author, Adam)

   ```python
   ...
   return render(request, "dashboard.html", {
               "selected_child": selected_child,
               "is_primary": is_primary,
               "selected_child_years": age_years,
               "selected_child_months": age_months,
               "children": children,

               "child_names": json.dumps(child_names),
               "data_logs_per_child": json.dumps(data_logs_per_child),
               "log_categories": json.dumps(log_categories),
               "log_category_counts": json.dumps(log_category_counts),
           })
   ...
   ```

   **dashboard.js** (extract) : (Author, Adam)

   ```javascript
   ...
   document.addEventListener('DOMContentLoaded', function() {
       const isAuthenticated = window.isAuthenticated;

       // use example data if user is not authenticated
       const childNames = isAuthenticated ? window.childNames : ['Alice', 'Bob', 'Charlie','Hugh','Charlotte', 'Susan', 'Kabul'];
       const dataLogsPerChild = isAuthenticated ? window.dataLogsPerChild : [5,0,1,9,10,12,7];
       const logNamePie = isAuthenticated ? 'Logs Per Child' : 'Example Data : Logs Per Child'

       ...

       // graph 1 : pie chart
       const ctx1 = document.getElementById('pieChart');
       new Chart(ctx1, {
           type: 'doughnut',
           data: {
               labels: childNames,
               datasets: [{
                   label: 'Logs',
                   data: dataLogsPerChild,
                   backgroundColor: colours,
                   hoverOffset: 15,
           }]},
           options: {
               maintainAspectRatio: false,
               responsive: true,
               plugins: {
                   title: {
                       display: true,
                       text: logNamePie,
                       font: {
                           size: 20}
           }}}
       });
   ...
   ```

   In the above dashboard.js you can clearly see the JavaScript operations of one of the two Charts.js graphs. The JavaScript file opens with an event listener so as to run the function to generate the graphs on page load. The various constants are declared within the function which are passed between the HTML template and the JavaScript file using window.

   Note that in the prior inline script in the dashboard.html template, the variables were passed to the window for this reason

   These constants are assigned conditionally based on if the user is authenticated (logged in) or a guest. If the user is a guest, and as such has no data associated with them, Some exemplary data is assigned to display the website capabilities in spite of a lack of an account. The previously instantiated HTML canvas tag "pieChart" is then targeted and the rest of the code is Charts.js specific for the curation. This completes the total explanation for how Charts.JS is incorporated into our app, how it interacts with the received backend data to produce dynamic visual data models in the frontend.

---

### 2.2. Other Areas

As well as the MVT architecture which makes up the bulk of the app, there are some other components that also play an important role in its functionality. Below are the key aspects of each. These topics below include the management from user interaction, data routing to external resources and some other bits.

#### Forms

Forms are what Django uses to handle user inputs and data validation. Forms are defined in forms.py, as a series of classes, to manage information entry such as the respective logs for each health tracking category.

**forms.py** (extract) : (Author, Adam)

```python
...
class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['firstName','lastName','dateOfBirth','profile_picture']
        widgets = {
            'dateOfBirth': forms.DateInput(attrs={'type': 'date'})
        }
...
```

Most forms are very similar, and follow a structure akin to the childForm form shown above. By using the database entity models in models.py, we are able to automatically generate forms based of them, simplifying the code considerably ("model = Child")
Along with this are the fields for each imputable piece of data for each form, and widgets. Widgets allow for use of some default html provided by django. For instance (in the example above), rather than typing out a calender date in the form "dd/mm/yyyy", the widget provides a calendar like GUI.

Django widget documentation (extract) : [https://docs.djangoproject.com/en/5.1/ref/forms/widgets/](https://docs.djangoproject.com/en/5.1/ref/forms/widgets/)

```txt
A widget is Django's representation of an HTML input element. The widget handles the rendering of the HTML, and the extraction of data from a GET/POST dictionary that corresponds to the widget.
The HTML generated by the built-in widgets uses HTML5 syntax, targeting \<!DOCTYPE html>. For example, it uses boolean attributes such as checked rather than the XHTML style of checked='checked'.
```

#### URLs

Django uses a URL dispatcher (urls.py) to map user request to views. This allows for dynamic binding of urls between pages, rather than strict static binding. For debugging and development purposes, this is especially helpful when page templates and file directories are reorganized.

Every view becomes associated with a url pattern that lets the user interact with different parts of the application (Visiting different links within the website), e.g. logging the various log types.

**urls.py** (extract) : (Author, Adam)

```python
...
urlpatterns = [
   # empty url redirects to home page
   path("", lambda request: redirect("dashboard/", permanent=False)),

   # child management pages
   path('createChild/',       views.createChild,      name='createChild'),
   path('addChild/',          views.addChild,         name='addChild'),
   path('edit_child/',        views.edit_child,       name='edit_child'),
   path('deselect-child',     views.deselect_child,   name='deselect_child'),
   path('select-child/<int:child_id>/', views.select_child, name='select_child'),

   # user management pages
   path("changeProfile/",     views.changeProfile,    name = "changeProfile"),
   path("settings/",          views.settings,         name = "settings"),

   # Django registration urls
   path("accounts/",          include("django.contrib.auth.urls")),
   path("sign_up/",           views.sign_up,          name="sign_up"),

   # tracking pages
   path("food/",              views.food,             name = "food"),
   path("medication/", views.medication,   name = "medication"),
   path("growth/",            views.growth,           name = "growth"),
   path("sleep/",             views.sleep,            name = "sleep"),

   # miscellaneous pages
   path("dashboard/",         views.dashboard,        name="dashboard"),
   path('pdf_children_all/',  views.pdf_children_all, name='pdf_children_all'),

   # testing page
   path("testing/",           views.testing,          name = "testing"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
...
```

**The last part, "static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)", the only non self-explanatory part, hold the purpose of allowing for serving of static files (e.g. PDFs) during development. Django doesn't serve media files for an in-production app (a typical web server host such as Nginx or Apache would handle this). So during development, until this app is finalized and fully functional, this line is necessary to allow uploaded files to be accessible to users.**

#### Signals

Signals are used in Django to automate some actions as a response to specific event triggers. Each signal takes the form of a single python function in the signals.py file, and is linked to a specific action using an @receiver decorator.

Examples of this include the automatic creation of profile entities for each user; Each Profile model needs a one-to-one relationship with the default django User model which it extends off of. The User models are created on sign up, this process is handled by django automatically, and the creation and linking of profiles is handled is the signal. See below.

**signals.py** (extract) : (Author, Adam)

```python
...
# Auto creation of profile entity
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created and not Profile.objects.filter(user=instance).exists():
        Profile.objects.create(user=instance)
...
```

Another important function habilitated by signals is the automatic deletion of User and Child profile pictures. Since typical databases (for obvious reasons) dont support the storing of files, each profile picture (e.g. Profile and Child tables), is stored as a plaintext reference to that files stored location within the Apps Media directory (and Accessed similarly in a template). See below for deletion of profile picture signal.

**signals.py** (extract) : (Author, Adam)

```python
...
# Deletion of old profile pictures on profile picture update
@receiver(pre_save, sender=Profile)
def delete_old_file_on_update(sender, instance, **kwargs):
    if not instance.pk:
        # If its a new object, there's nothing to delete, ignore
        return

    try:
        old_instance = Profile.objects.get(pk=instance.pk)
        if old_instance.profile_picture and old_instance.profile_picture != instance.profile_picture:
            # If the image is being replaced, delete the old image
            if default_storage.exists(old_instance.profile_picture.path):
                default_storage.delete(old_instance.profile_picture.path)
    except Profile.DoesNotExist:
        # If the profile hasn't been created yet, ignore
        pass

# Deletion of old profile pictures on profile deletion
@receiver(pre_delete, sender=Profile)
def delete_file_on_profile_delete(sender, instance, **kwargs):
    if instance.profile_picture:
        # Delete image file associated with user
        if default_storage.exists(instance.profile_picture.path):
            default_storage.delete(instance.profile_picture.path)
...
```

The deletion of a row in the database table deletes the reference to the media file, not the media file itself, thus the necessity for a signal. On some events (e.g. updating profile picture, deletion of profile), this signal is triggered to delete that file stored on the server. This prevents a bloated server storing media that isn't associated with anyone.

#### Static Files & Media

Django handles static files (e.g. css, js, icons, website images) using the static/ system, to dynamically serve assets and such throughout the apps frontend. Each template initially loads static using the django tag "*{% load static %}*" The specific static folder directory is specified in the settings.py as "*STATIC_URL = 'static/'*". This allows for non strict directory layout.

As for user-uploaded content, such as images in the User and Child profile picture, the media directory is instead used for organizational purposes. During development, static files are hosted locally, however should the app be later moved to production, these would likely be moved and configured for a cloud-based storage (e.g. AWS).

#### Fixtures

For testing purposes and due to the lack of users, during development, an initial exemplary data set was created and stored in the fixture directory. This exemplary data is stored as a JSON for the database data, and a set of royalty free images used to populate the media directory. It is also beneficial for someone who wishes to explore our project as a contributor, to understand the workings of it quickly and effectively.When running setup.ps1, The option is available to preload this data, ready to simulate real world use cases, and test the application.

## 3. Data Structures and Algorithms

*Describe data structures of at least one component of your implementation.*
*Describe at least one algorithm used in your implementation.*
*In both cases, describe the space / time complexity of each.*

### 3.1. Data Structures

One of the main components of the application is the child management, which operates on the child model, which is effectively a django data structure. The data for each child is stored in a relational database (SQLite3), which Django then uses its ORM (Object-Relational Mapper) to abstract the interaction.The child.

**models.py** (extract) : (Author, Adam)

```python
...
class Child(models.Model):
    # Foreign key reference
    parents = models.ManyToManyField(User, through='FamilyAssociation', related_name='children')

    # Data structure attributes
    firstName       = models.CharField(max_length=50)
    lastName        = models.CharField(max_length=50)
    dateOfBirth     = models.DateField(default=None)
    profile_picture = models.ImageField(upload_to=profilePicUniqueUpload,blank=True, null=True)
    shareCode       = models.CharField(max_length=10, unique=True, blank=True, null=True)

    # Method for shareCode generation
    def shareCodeGenerate(self):
        self.shareCode = get_random_string(length=10)
        self.save()

    # Descriptor for the Data structure
    class Meta:
        db_table = "chawts_child"
...
```

Each instance of a child model corresponds to an entry in the table, and each attribute of the child model corresponds to a column. The use of a database and SQLite3 are what allow for linking of a child to parents, and specific logs in the context of a server hosted database

When fetching data, Django ORM optimizes queries depending on the relationship, so space and time complexity will vary, however a simple query in in views.py against the Database (e.g. see below) would be O(n) **time complexity**. "n" being the amount of children associated with the User for whom the view is serving.

```python
...
# O(n) time complexity
children = request.user.children.all()
children = Child.objects.filter(familyassociation__parent=request.user)
children = Child.objects.filter(familyassociation__parent_id=user_id)
...
```

**Space complexity** is harder to estimate. For a simple data structure such as Family associations, which has a small amount of fields, no null fields, and all fields are simple data type (boolean and int), this is simple. Space complexity is **O(1)

**

**models.py** (extract) : (Author, Adam)

```Python
...
class FamilyAssociation(models.Model):
    parent     = models.ForeignKey(User, on_delete=models.CASCADE)
    child      = models.ForeignKey(Child, on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)

    class Meta:
        db_table = "chawts_families"
        unique_together = ('parent', 'child')
...
```

However it is more complex in e.g. the prior Child model which has a profile_picture attribute, referencing a media file. The profile picture image far exceeds the space requirement for the rest of data structure. Additionally the profile_picture itself is optional, meaning e.g. some child objects will be a few kilobytes in size with no image associated with them, and some may exceed a few megabytes with an an image. It is hard therefore to assign a direct value for space complexity.

Albeit not strictly allowed, when ignoring the image referencing of the Child mode, the only thing that varies the Space complexity of the child model is the amount of Users associated with it in the FamilyAssociations foreign table reference. Since this is a many-to-many relationship between the User model and the Child model, the space complexity is proportional to the amount of users; **O(n)**, where "n" is the amount of users the child is shared with.

```Python
...
# O(n) time complexity
users = child.parents.all()
users = User.objects.filter(familyassociation__child=child)
users = User.objects.filter(familyassociation__child_id=child_id)
...
```

### 3.2. Algorithms

Our CHAWTS app, that runs of Django doest strictly have any algorithms in the same way, say, a sorting function might. This is due to the nature of the web based software needing minimal calculation, rather presenting data as it is stored iteratively.

The most viable candidate would likely be generation of the PDFs within the views.py, albeit an implicit one. The PDF generation involves iterating through each of the children associated with the User, and their respective logs, formatting it conditionally to maintain a structured document.

Within the PDF view, the section specifically which is algorithmic is the filling in the PDF. This consists of two parts

1. A *drawLog* internal function :

   - This takes a set of logs and formats them correctly, iteratively appending them onto the PDF document
   - Depending on the logName (Growth, Food etc.), different formats are applied to fit the data each log tracks.
2. Main loop for each child :

   - For each child associated with the user requesting the PDF, The algorithm determines how much page space is needed to contain all the logs for that child. If there is not enough remaining space on the current page, it seeks forward to the next.
   - The child's Info is Added, including calculation for their Current age
   - For every child to whom the User is the primary parent of, the PDF adds the share code below that child, otherwise this step is skipped
   - the *drawLog* Function is called for each of the child's log categories

At each step where the PDF is written to, a pointer location is kept track of, moving up/down/left/right to avoid over writing text and incorrectly indented/formatted outputs, whilst allowing for dynamic reports.

**Time complexity** for this function is proportional to both the amount of children associated with the user, and the amount of logs associated with each child from this set of children. Since the algorithm iteratively loops over each child O(C), and iteratively loops over logs for each child O(L), the time complexity would be O(C*L) assuming each child has at least some Logs. This would be linear in terms of the total amount of logs.

**Space Complexity** is dependent on the space used bt the PDF buffer and the logs/children that are being processed. The PDF buffer grows in accordance with the content added to it, but is ultimately written and saved to a file. Additionally, since Logs and children are processed sequentially without needing to store copies, the resulting space complexity is O(1)

## 4. Known Issues

Our Project has suffered quite substantially due to both poor management, and poor work, provided by various team members. Because of this, there are Large gaps in the functioning of our project. In no particular order.

### 4.1. Frontend

1. Settings page (Author, Zaki)
   1. No backend linkage
   2. Buttons dont do anything
2. Food page (Author, Charles)
   1. CSS incorrectly implemented
3. Medication page (Author, Munashe)
   1. No backend linkage
   2. CSS missing
4. Growth page (Author, Munashe)
   1. No backend linkage
   2. CSS missing
5. Sleep page (Author, Evan)
   1. No backend linkage
   2. Buttons dont do anything
   3. Little to no CSS styling
6. Dashboard (Author, Adam)
   1. Footer not useful
7. Sign up Page (Author, Adam)
   1. CSS occasionally goes off screen
8. Missing Pages
   1. Diaper page
   2. View all children page

### 4.2. Backend

1. Related to the user
   1. changeProfile (Author, Adam)
      1. Can't change profile name
   2. login (Author, Adam)
      1. No 2FA
   3. Sign Up (Author, Adam)
      1. Cant setup profile simultaneously
2. Related to the children
   1. Import Child (Author, Adam)
      1. No further authentication past share code
      2. Cant revoke access after child is shared
   2. No ability to delete / remove children
3. Export PDF (Author, Adam)
   1. Limited implementation
   2. No support for visual data
4. Misc
   1. urls.py : No redirect for mismatch urls
   2. signals.py : No auto delete for Child Profile picture
   3. models.py : Not needed Types parameter in base Log

## 5. Imported Libraries

### 5.1. Environment Dependency

1. Python (3.12.9) - Programming language used to build the project

### 5.2. Direct Dependencies

1. Django (5.1.6) - The web framework used for building the backend of the application
2. Charts.js (4.4.8) - Used for dynamic, interactive data visualization.
3. Pillow (11.1.0) - Used for managing images (e.g. profile pictures).
4. ReportLab (4.3.1) - Used for generating PDF reports.
5. FontAwesome (6.3) - Provides vector icons for UI elements.

### 5.3. Transitive Dependencies

(Libraries that came with Django)

1. SQLParse (0.5.3) - Used for parsing and formatting SQL queries.
2. TZData (2025.1) - Provides time zone data for time-handling functions.
3. ASGriref (3.8.1) - Used for handling asynchronous requests.
4. Chardet (5.2.0) - Used in detection of text encoding (for handling multiple file formats)

## 6. Licenses

This project makes use of various open-source libraries and frameworks, each of which comes with its own license terms. Below, you will find the licenses of each, including key conditions and links to the full text for reference. We have ensured that any usage in this project remains in compliance with these licenses.

### 6.1. **Django** (Extract)

```txt
Copyright (c) Django Software Foundation and individual contributors.
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,are permitted provided that the following conditions are met:

1  Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2  Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3  Neither the name of Django nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

Full License : [https://github.com/django/django/blob/main/LICENSE](https://github.com/django/django/blob/main/LICENSE)

### 6.2. **Charts.js** (full)

```txt
The MIT License (MIT)

Copyright (c) 2014-2024 Chart.js Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

Full License : [https://github.com/chartjs/Chart.js/blob/master/LICENSE.md](https://github.com/chartjs/Chart.js/blob/master/LICENSE.md)

### 6.3. **Pillow** (full)

```txt
The Python Imaging Library (PIL) is

Copyright © 1997-2011 by Secret Labs AB
Copyright © 1995-2011 by Fredrik Lundh and contributors

Pillow is the friendly PIL fork. It is

Copyright © 2010 by Jeffrey A. Clark and contributors

Like PIL, Pillow is licensed under the open source MIT-CMU License:

By obtaining, using, and/or copying this software and/or its associated documentation, you agree that you have read, understood, and will comply with the following terms and conditions:

Permission to use, copy, modify and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appears in all copies, and that both that copyright notice and this permission notice appear in supporting documentation, and that the name of Secret Labs AB or the author not be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission.

SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL SECRET LABS AB OR THE AUTHOR BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```

Full License : [https://github.com/python-pillow/Pillow/blob/main/LICENSE](https://github.com/python-pillow/Pillow/blob/main/LICENSE)

### 6.4. **ReportLab** (Full)

```txt#
Copyright (c) 2000-2014, ReportLab Inc.
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1  Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2  Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3  Neither the name of the company nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE OFFICERS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

Full License : [https://github.com/Distrotech/reportlab/blob/master/LICENSE.txt](https://github.com/Distrotech/reportlab/blob/master/LICENSE.txt)

### 6.5. **FontAwesome** (extract)

```txt
Icons: CC BY 4.0 License (https://creativecommons.org/licenses/by/4.0/)
Fonts: SIL OFL 1.1 License
Copyright (c) 2024 Fonticons, Inc. (https://fontawesome.com) with Reserved Font Name: "Font Awesome".

This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is copied below, and is also available with a FAQ at: http://scripts.sil.org/OFL

SIL OPEN FONT LICENSE
Version 1.1 - 26 February 2007

PERMISSION & CONDITIONS
1  Neither the Font Software nor any of its individual components, in Original or Modified Versions, may be sold by itself.

2  Original or Modified Versions of the Font Software may be bundled, redistributed and/or sold with any software, provided that each copy contains the above copyright notice and this license. These can be included either as stand-alone text files, human-readable headers or in the appropriate machine-readable metadata fields within text or binary files as long as those fields can be easily viewed by the user.

3  No Modified Version of the Font Software may use the Reserved Font Name(s) unless explicit written permission is granted by the corresponding Copyright Holder. This restriction only applies to the primary font name as presented to the users.

4  The name(s) of the Copyright Holder(s) or the Author(s) of the Font Software shall not be used to promote, endorse or advertise any Modified Version, except to acknowledge the contribution(s) of the Copyright Holder(s) and the Author(s) or with their explicit written permission.

5  The Font Software, modified or unmodified, in part or in whole, must be distributed entirely under this license, and must not be distributed under any other license. The requirement for fonts to remain under this license does not apply to any document created using the Font Software.

Copyright 2024 Fonticons, Inc.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

Full License : [https://github.com/FortAwesome/Font-Awesome/blob/6.x/LICENSE.txt](https://github.com/FortAwesome/Font-Awesome/blob/6.x/LICENSE.txt)
