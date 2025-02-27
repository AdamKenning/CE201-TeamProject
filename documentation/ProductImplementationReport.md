# Team Implementation Report

*This section should describe the technical details of your implementation.  The subheadings and italicised text below may be used to guide you.*

## Technical Diagrams

*Include a class diagram / circuit diagram, and/or any other relevant technical diagrams.*

## Technical Description

The CHAWTS App was developed using the Django framework, a predominantly Python based framework, using the *MVT* architecture to allow for simple expansion and cohesion. MVT (Model-View-Template), similar to the *MVC* (Model-View-Controller), splits the app into three distinct main layers that all comunicate with each other (with additional areas i will touch on later). These three layers each run from their respective single python file.

### Model

This represents the database structre; How the database is stored and structured, each class in **models.py** represents a disctince database table e.g. "Child" Database Entity implemented using Python Class

```python
Class Child(models.Model):
    # A foreign key contraint linking child and parent via a third table
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

Each model created subclasses the django.db.models.Model which implements the basic functionailty shared between all models. To quickly run through the parts Models.py that make up the functioning of the database:

1. **ProfilePicUniqueUpload** : (Author, Adam)
   This is the only standalone function in models.py, and it serves to generate unique file name replacements, using *UUID4* (Universally Unique Identifier version 4) for files uploaded e.g. profile pictures. This is to mitigate the risk of multiple people uploading profile picture files that share a common name, overwriting each other when stored on the server.
2. **Profile** : (Author, Adam)
   A class that has a one-to-one relationship with the default Django *User* Model. Django already has a preset user model which has most of the functionality our app needed. *Profile* is used to "extend" the *User* model to allow for custom fields such as *profile_picture*.

   The default django User model includes typical fields such as *username*, *password*, *email* etc. But also includes fields that allow for tracking of users engagement e.g. *is_active*, *date_joined*, *last_login*. Finally, it contains fields relating to adiminstratarion; *is_superuser*, *is_staff*.

   These two classes, *Profile* & *User*, are how the parent/ guardian loging into and using our app, will be stored.
3. **Child** : (Author, Adam)
   Represents the children that are being tracked using our software, the first four fields are simple enough *firstName*, *lastName*, *dateOfBirth* and *profile_pciture*, which functions the same as in the *Profile* class.

   the *parents* field is a foreign key link to the next class *FamilyAssociation*.
   The *shareCode* field is a 10-character randomized string used to grant access to a child’s profile, allowing multiple caregivers (e.g. two parents and a childminder) to log data for the same child. This code is single-use—once redeemed, it is automatically reset to a new random string. Only the primary parent (explained later) can access and generate this code, ensuring a secure and controlled sharing process while preventing unauthorized users from repeatedly distributing access.
4. **FamilyAssociation** : (Author, Adam)
   Since one user may need access to many children, and one child may be accessed by many users, this becomes a many-to-many relationship. This table exists to store which *User* entity has access to which *Child* entity.

   There are two foreign key contraints, one for the *User* (parent) and one for the *Child*. Additionally there is a single boolean value *is_primary* which indicates which user is the primary guardian of the child, typically this is whichever user initially created the child on in the app prior to sharing the child. This primary user is granted authoritative rights such as deletion and access to the childs share code.
5. **Log** : (Author, Adam)
   Our apps primary purpose is tracking the data associated with a child. Every data point is stored as a log allowing for quick queriying and easy data manipulation. There are various log types for the data we track, but they all have some fields in common, Thus the default *Log* class holds common fields that the other log classes can then extend off of. Note : This Class is never directly used itself.

   Fields include the log *type*, Two dateTimeFields for the time the Log was submitted and the time the User states the log was for (e.g. retroActively adding some data for a past event). A foreign key contraint field for a specific child allows the logs to be linked correctly, since a particular log can only describe an event of a particular child. Then the *comment* field exists simply for User notation (akin to additional information).
6. **SleepLog**, **FoodLog**, **GrowthLog** : (Author, Adam)
   These tables store the logs for the catagory specific data, and extend of the basic *Log* class for added nuanced fields. For example, *FoodLog* Extends *Log* with a field *mealType*. *mealType* is dependent on the childs age; A child younger than 6 months has a different selection of meals than an older child.

   Similarly, the other *Log* extensions implement their own respective fields for tracking data unique to their catagory.

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
        # If the user isnt submitting a form, show them an unfilled form
        profile_form = ProfileForm(instance=profile)
  
    # Server the user the page html, with the relevant form
    return render(request, 'management/changeProfile.html', {
        'profile_form': profile_form,
    })
```

Most of the views serve similar purposes, however there are some that do not conform. I will discuss the implementation of these views briefly.

1. **Dashboard** : (Author, Adam)
   By far the largest of the views, this handles all the technical side for the Dashboard, Landing for the website and thus serves to provide quick general information as well as general functionality.

   For a person visiting our website, it was important for us to display exemplory information so as to allow a guest to view what the website may look like for them. To allow this, the first check is against if the user is "Authenticated"; logged in. If the user is not logged in (guest), various data that would have been served to the front end is served as blank (This empty data is dealt with and populated later with false example data)

   If the user is logged in, firstly the method gets a specific child id from the session storage (session storage is used to hold temporary information accross pages). The child referenced in the session storage is the selected_child*. The specific age of this child is then calculated from the users current date against the selected_childs dataOfBirth field.

   Dashboard is used to select a specific child for the other pages. This aside the dashboard itself is used to show the user general non-specific data about their children. For this, two distinct data sets are generated. These both describe the proportions of data that has been logged for all the children, using different comparators for better data analysis.

   1. Data logs per child
   2. Data logs per catagory

   All of the various data generated in this view is then passed to the user alongisde the dashboard.html template.

   *selected_child : One of the children, selected by the users, from the children associated with that user. This child is then able to be used later to declutter pages by only showing data relevent to that singular child at a time.
2. **sign_Up** : (Author, Adam)
   This view checks the contents of its request, to see if it is a posted form. If is it, and the form is valid, it saves the signup information as a new user and immediatly attempts a login on the newly created user.
3. **growth**, **sleep** : (Author, Adam)
   Both of these these views function for their respective growth and sleep pages.

   For these views to be valid, the user first must be logged in, since as a guest there is no specific data for any children to display. Additionally, a check is done to retrieve the selected_child from the session Id, if a child has not been selected, there once again is no data to show and the user is redirected to the dashboard.

   If these checks are passed, the views pass this selected child alongside the respective pages html template to the frontend.
4. **Food** : (Author, Adam/Charles)
   The food view, is similar to the prior growth and sleep, working on similar logic. However, for the food View, additional information is needed:

   1. chart_data :
      Two sets of data relevant for the data visualizer on the Food page, consisting of the datas labels and calories per meal.
   2. Meals :
      A single set of data of each meal taken.

   This data is passed alongisde the selected child and the food.html template.
5. **settings** : (Author, Adam)
   Servers the settings.html template to the user. This page has not had much work done on it, so the view is very simple.
6. **select_child**, **deselect_child** : (Author, Adam)
   These two views allow for the heavily selected_child functionailty used heavily accross the app. Both views require the user to be logged in.

   Selection is done by using the child_id passed as a paramater of the function alonside the request and setting that id in the current session as 'selected_child_id'. Deselect works in reverse, Checking if the token exists in the session, and deletes it.

   These views then redirect to the dashboard (refresh the page), to reflect the changes.
7. **create_child** : (Author, Adam)
   Used for initiating new child entities, this function takes the form fomr the requested data paramater. If the requested form is valid, it creates a new child object, without comiting the creation of the child. The code for the half-created child is generated, then the child is saved properly.

   A new entry in the family associations table is then created to represent the link between the user who requested the creation of the child and the child itself.

   On sucessfull completion of these steps, the view redirects the user to the dashboard to reflect the new child creation changes.
8. **add_child** : (Author, Adam)
   To enable the many-to-many relationship used in our CHAWTS app for multi-child-parent relationships, the addition of prexisting children is necessitated. This view implements this functionailty by taking the form from the requested data and processing the extracted share code inputed by the user in that form.

   If the code is an invalid code; there exists no children with that specific share code, an exception is thrown and the user is redirected back to the dashboard.

   However, if a child does exist with a matching code, the child can be linked to the user. A new entry in the familyAssociations table is created between the child and the user, wherin the user is not the primary parent of the user. The childs specific shareCode is then reset to a new random string (to prevent misuse), and finally the user is redirected back to the dashboard.

   On the dashboard, if the sharecode was successfull, the user will see the new child amongst their pre-existing children allocated to them.
9. **edit_child** : (Author, Adam)
   To allow for the post-creation editing of a child details (e.g. mis-input of a name, or to update a profile picture), the edit_child view is needed. Alongside the selected_child, this view has a is_primary check present, refering to the childs association to the parent in the FamilyAssociation table.

   If the parent is the primary parent of the child. If the user is not the primary parent of the child, the user is denied access to the view, and redirected to the dashboard. If the user is the primary parent, they are able to submit a new form through the request paramater of the function.

   This form is checked for validity and submitted. The html template is then rendered to the user alongside the form as well as the currently selected child.
10. **changeProfile** : (Author, Adam)
11. **testing** : (Author, Adam)
12. **pdf_children_all** : (Author, Adam)
13. **pdf_file_children_all** : (Author, Adam)

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
