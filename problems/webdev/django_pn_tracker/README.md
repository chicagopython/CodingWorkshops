In this project we will be building a CRUD-style web app using Django and SQLite3.

## The Project
With growing Project Night attendance, ChiPy would like to better keep track of Challenge participation, and the CSV sign up sheets just aren't cutting it. In this project we'll upgrade things a notch by creating a web app (using Django) to keep track of our data (in a basic SQLite3 database). The goal of our app is to have an easy way to enter and view our data, all while maintaining attendee's privacy. To save some time, the django project has already been created, as well as the framework for thee structure for the app we'll be working on. To learn how to set up a Django app from scratch, check out https://docs.djangoproject.com/en/2.1/intro/tutorial01/#creating-a-project.

## Setup
1. Clone the project:

    > git clone https://github.com/chicagopython/CodingWorkshops.git

2. Set up a virtual environment, as desired:
    ```
    # If you are using Linux or OS X, run the following:
    > python3 -m venv venv
    > source venv/bin/activate

    # On Windows, run the following:
    > python3 -m venv venv
    > venv\Scripts\activate
    ```
3. Navigate to the right folder:

    > cd problems/webdev/django_pn_tracker

3. Install our python package requirements:

    > pip install -r requirements.txt


## Instructions
In the steps that follow, instructions will generally reference exactly where code changes need to be made. In the files themselves you'll see large commented blocks of instructions indicating that you're in the right spot. If you don't see commented instructions, double check that you read the prompt correctly. Each step will also have a link to a resource that should directly help you solve the problem at hand. Even if you're not stuck, it's recommended to check out the link to improve your understanding of WHY we're doing what we're doing.

To help visualize the locations of the file, here's the full file tree:
```
├── db.sqlite3
├── django_pn_tracker
│   ├── __init__.py
│   ├── __pycache__
│   ├── apps
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   └── __init__.cpython-36.pyc
│   │   └── challenges
│   │       ├── __init__.py
│   │       ├── __pycache__
│   │       ├── admin.py
│   │       ├── apps.py
│   │       ├── forms.py
│   │       ├── migrations
│   │       │   ├── 0001_initial.py
│   │       │   ├── __init__.py
│   │       │   └── __pycache__
│   │       ├── models.py
│   │       ├── templates
│   │       │   └── challenges
│   │       │       ├── delete.html
│   │       │       ├── edit.html
│   │       │       └── list.html
│   │       ├── tests.py
│   │       ├── urls.py
│   │       └── views.py
│   ├── settings.py
│   ├── static
│   │   ├── css
│   │   │   ├── bootstrap.min.css
│   │   │   └── master.css
│   │   └── js
│   │       ├── bootstrap.min.js
│   │       └── main.js
│   ├── templates
│   │   ├── base.html
│   │   └── index.html
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── setup.cfg
```

### Step 0: Run the app as is
Before we dig in, let's see what the app currently looks like. This'll also confirm that install/setup went as planned. To run the app locally:
    > ./manage.py runserver

Then open the link provided in the terminal: http://127.0.0.1:8000/

### Step 1: Configure settings
While our project already has a lot written, we need to configure settings for our new app. Django projects store these settings in `settings.py` by default. 

**a. Add our 'challenges' app to `INSTALLED_APPS`** in `settings.py`. This is actually done already, so the app would run as is without error. Still, check the comment in the code to see how we add apps.

**b. Point Django to our sqlite db** called `db.sqlite3`. See https://docs.djangoproject.com/en/2.1/ref/settings/#databases for help with the syntax.

### Step 2: Create and integrate a new database table
Our initial objective is to set up a table to display all of our challenge participantion records. Table schemas can be found in `models.py`. 

a. Several tables already exist, but we want to create a new table called `AttendeeInfo` to include:

   * `date` - Date of the event
   * `name` - the participant's name
   * `challenge` - the name of the challenge. Don't forget to account for the foreign key relationship with `Challenge` 
   * `skills` - for now an integer representing a score in the range of 0-10. Read more avoud validators: https://docs.djangoproject.com/en/2.1/ref/validators/

   Read more about models here: https://docs.djangoproject.com/en/2.1/topics/db/models/

**b. Create/complete migration.** In order for our changes to take effect we need to create a migration and then actually migrate it.

    > ./manage.py makemigrations

This is a little bit of Django magic. Under the hood Django is automatically generating the SQL commands necessary to update your database. You can see the actual underlying commands in `apps/challenges/migrations`, where a file of commands is created each time we run makemigrations.

   In order to actually make our changes, run:

    > ./manage.py migrate

c. **Register `models.AttendeeInfo` in `admin.py`.** Don't worry about what this does yet, we'll get to it in a later instruction.

### Step 3: Create a page to view the table's records
Now that we've created our table, we want to create a page to view our new table's records.

**a. Create the URL** we want for our page in `urls.py`. We will use `""` and reference `challenges_list` in views. Learn more about Django URLs: https://docs.djangoproject.com/en/2.1/topics/http/urls/

**b. Create the new `challenge_list` view in `views.py`** for our new page. Django has the concept of “views” to encapsulate the logic responsible for processing a user’s request and for returning the response. Syntactically, a view is just a regular python function (or class) that will be called when we travel to the associated url. To learn more about writing views, check out: https://docs.djangoproject.com/en/2.1/topics/http/views/ . In the case of challenge_list, use the following variable names:

* `template_name` as the variable that points to `challenges/list.html`,
* `attendees` should be all of our AttendeeInfo objects (see https://docs.djangoproject.com/en/2.1/topics/db/queries/#retrieving-objects), and
* `context` should be a dictionary mapping the string `"attendees"` to our `attendees` variable. 

The names selected are only important to match the templates that we've already started for you.

**c. Create a template.** Templates are the layers of your app that create the structure of the pages visible to users. Django uses a templating language that's very similar to HTML plus some interactivity with our python code, mostly via syntax surrounded by curly braces. Instead of starting totally from scratch, the template for our record listing is already started in `list.html`, so we'll just fill in the missing section (as indicated with comments). To learn more about template basics (and see some syntax examples) check out: https://docs.djangoproject.com/en/2.1/ref/templates/language/#templates .

**d. Add a link to our new view in our main navigation bar.** This can be done in the body of `base.html`.

### Step 4: Add CRUD capability
Now we can view our new table, but there's nothing in it! Let's create a way to add/edit/delete entries via forms on the front end. To do this, we'll take our steps from 3 and add a little more complexity ala forms:

**a. Create the URL** we want for our page in `urls.py`. We will reference `challenges_add`, `challenges_edit`, and `challenges_delete` views. Note that edit and delete will reference existing objects - the url pattern therefore requires special syntax (revisit https://docs.djangoproject.com/en/2.1/topics/http/urls/ for help)

**b. Create forms.** Set up `AttendeeEditForm` and `ConfirmForm` in `forms.py`. We will reference these in our views. Learn more about model forms here: https://docs.djangoproject.com/en/2.1/topics/forms/modelforms/ , and more about fields here: https://docs.djangoproject.com/en/2.1/ref/forms/fields/ .

**c. Create the three new views in views.py for our new pages.** Mimic the template_name, attendees, and context variable names and style from challenge_list. Use the variable form to instantiate the form object. For example, paste this into challenge_add: `form = forms.AttendeeEditForm()` . See https://docs.djangoproject.com/en/2.1/topics/forms/#the-view and for help.

**d. Create templates.** These are already started for you in `edit.html` and `delete.html`, so just fill in the missing section (as indicated). Note that add and edit will both use `edit.html`. Bonus hint: Are the edit and delete forms really different..? See https://docs.djangoproject.com/en/2.1/topics/forms/#the-template for help.

**e. Add links.** Add links for edit and delete in a new column in the existing table (requires editing `list.html` again).

### Step 4: Add yourselves as records using our new forms
Now that we've created our MVP, let's test it out by adding records for ourselves for this event. You'll notice that there's no event option in the dropdown for this Intro to Django event. For now, add yourselves under 'Demo Event'.

### Step 5: Add interface to add new events
You've seen how to create a form and have a couple of example templates you've already worked with. Now it's time to do one from scratch. Create a form to add challenge records to the Challenge table. You will need a new template in the same folder as our delete.html, edit.html, and list.html. You'll also need to create a new form in forms.py. Lastly we'll need a way to get to our page to add a challenge - let's put it on the main navigation bar next to Challenges List (again in the body of base.html)

### Step 6: Add login requirements so our app isn't open to the world.
After all, we'll have participants names and experience levels stored - that's sensitive information. You're on your own again! If you need help:
* https://docs.djangoproject.com/en/2.1/topics/auth/default/#the-login-required-decorator
* https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators