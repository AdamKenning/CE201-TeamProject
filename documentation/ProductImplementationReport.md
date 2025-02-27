# Team Implementation Report

*This section should describe the technical details of your implementation.  The subheadings and italicised text below may be used to guide you.*

## Technical Diagrams

*Include a class diagram / circuit diagram, and/or any other relevant technical diagrams.*

## Technical Description

The CHAWTS App was developed using the Django framework, a predominantly Python based framework, using the *MVT* architecture to allow for simple expansion and cohesion. MVT (Model-View-Template), similar to the *MVC* (Model-View-Controller), splits the app into three distinct main layers that all communicate with each other (with additional areas i will touch on later). These three layers each run from their respective single python file.

### Model

This represents the database structure; How the database is stored and structured, each class in **models.py** represents a distinct database table e.g. "Child" Database Entity implemented using Python Class

```python
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

### View

The View is where the CHAWTS app logic happens, it processes user requests, Interacts with model and determines what data to serve to the user. This intermediary layer is akin to the "Brains" of the whole App. In a similar way as the django Model, a "view" is written as a Python Function in a single Python files **views.py**.

Each view takes a request from the user (The request taking different forms depending on the use case), and processes it. Based on this request, a view may conditionally retrieve some data from the model database, and pass this data back to the user alongside a given template.

For example, the view changeProfile, used for updating the users profile picture

```python
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

    This canvas object can be written to using simple commands. For example, using the blow **canvas_out** object, the string "test" can be written at position (x,y). Methods exist to add effects (e.g. font size, bold, underline), but this is the basic idea.

    ```python
    canvas_out = canvas.Canvas(BytesIO())
    canvas_out.drawString(x,y,"test")
    ```

    The pdf_file_children_all view dynamically generates the logs based off each child's specific logs. It does this by iterating over every log, for every child, and writing to the canvas all data. An internal helper function is used *drawLog* used for automation of repetitive step such as indentation for uniform formal readability.

    As well as the logs for the respective children, the specific details of each child area also appended to the document (name,age, share code etc), and the User who requested the PDF document.

    Once complete, the PDF document is shown to the user and saved to the users device, before returning this PDF document up to the previous view.
13. **testing** : (Author, Adam)
    This view, although not intended to be continued should this project be used as a real viable product, still serves a purpose nonetheless in the meantime. Due to the questionable state of the App (its pages, wherein the user is meant to be able to log data, not existing or barely functional) there is no way to log data for experimental debugging use.

    Thus this view exists. It is merely while the APP is in development, to allow for temporary functionality. This view operates alongside its respective testing.html template, providing a page for a developer to manually log every kind of data at once from one place.

    Initial checks are done as per the other food, growth and sleep logging pages, checking if the user is first logged in, and if there is a child selected in the session. If these are passed, three forms for food, growth and sleep are created (for food, the 6 months exception is applied)

    After this, a check is done against the request method, if it is POST (the user is sending a form across), the respective form handling code will trigger. This is conditional on what type of from is in the request POST. For the respective form type, the form is validated, saved without committing and then associated with the selected child. After this the page is redirected back to testing (refresh), and the relevant forms are served for the user.

### Template


*This section should describe the software implementation in prose form.  Focus on how the code was designed and built.*
*It should make a clear description that could be used by any future developers to maintain and extend your code, if necessary.*
*Describe important functions / classes / class hierarchies.*
*In this section, you should also wish to highlight any technical achievements your team is particularly proud of, including relevant code snippets.*

## Algorithms and Data Structures

*Describe data structures of at least one component of your implementation.*
*Describe at least one algorithm used in your implementation.*
*In both cases, describe the space / time complexity of each.*

## Imported Libraries

*List any 3rd party libraries that were used and describe what functionality they provided.*

## Known Issues

*List any known issues (bugs) in your software, and describe workarounds if they exist.*
