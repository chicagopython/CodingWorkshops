<!-- TOC -->

- [Flask Dashboard for tracking developer time](#flask-dashboard-for-tracking-developer-time)
    - [0.0.1. Is this project for you](#001-is-this-project-for-you)
    - [0.0.2. Reference documents](#002-reference-documents)
    - [0.0.3. What is not supported](#003-what-is-not-supported)
    - [0.0.4. Minimum Viable Product](#004-minimum-viable-product)
    - [0.0.5. Flask](#005-flask)
    - [0.0.6. Setup your environment](#006-setup-your-environment)
        - [0.0.6.1. Get the source code](#0061-get-the-source-code)
    - [0.0.7. Files](#007-files)
    - [0.0.8. Set up virtualenv](#008-set-up-virtualenv)
    - [0.0.9. Feature 0: run app.py](#009-feature-0-run-apppy)
    - [0.0.10. Exercise 1: Shows the list of tasks that a mentee has added](#0010-exercise-1-shows-the-list-of-tasks-that-a-mentee-has-added)
    - [0.0.11. Exercise 2: Shows the list of tasks of a particular type](#0011-exercise-2-shows-the-list-of-tasks-of-a-particular-type)
    - [0.0.13. Exercise 3: Show the total time spent by the mentee for each of the task types](#0013-exercise-3-show-the-total-time-spent-by-the-mentee-for-each-of-the-task-types)
    - [0.0.12. Exercise 4: Build a better UI](#0012-exercise-4-build-a-better-ui)
    - [0.0.14. Exercise 5: Integrate the task filtering with these aggregate metrics](#0014-exercise-5-integrate-the-task-filtering-with-these-aggregate-metrics)
    - [0.0.15. Exercise 6: Add tasks from UI](#0015-exercise-6-add-tasks-from-ui)
    - [0.0.16. Exercise 7: Show the list of hashtags and their corresponding counts](#0016-exercise-7-show-the-list-of-hashtags-and-their-corresponding-counts)

<!-- /TOC -->
# Flask Dashboard for tracking developer time
Chipy's mentorship program is an extra-ordinary jounery for becoming a better developer. As a mentee, you are expected to do a lot - you read new articles/books, write code, debug and troubleshoot, pair program with other mentees in coding workshop or your mentor. This is involves managing time efficiently and doing the effective things. But as the old adage goes, "you can't manage what you can't measure".

This project is the second of the three part series of building tools for the mentees for tracking time. The end goal of such a tool will be to aggregate anonymous data and analyze how does a typical mentee spend on blogging (b), coding (c), debugging (d), pair program (p) with mentor or other mentees.

In this project we will be building a fully functional web dashboard for tracking developer efforts using Flask.


Short url for this page: **https://git.io/vdQj6** #TODO

## 0.0.1. Is this project for you
Before you progress further, let's check if we are ready to solve this. You should
- Have a personal computer with working wifi and power cord
- Have Python 3 installed on your computer. Yep, Python 3 only
- Have [Atom](https://atom.io/) or [Sublime Text](https://www.sublimetext.com/3) installed in your computer
- Have written & ran programs in Python from the command line
- Have some idea about lists, dictionaries and functions
- Have created a virtual environment and installing packages with `pip`
- You have read the [flask quick introduction](http://flask.pocoo.org/docs/0.12/quickstart/)


In addition, you should be familiar with [Part 1](https://github.com/chicagopython/CodingWorkshops/tree/master/problems/py101/trackcoder) of this three part exercise.

## 0.0.2. Reference documents
Reading these links before attending project night, would help you a lot by providing
the background needed to work through the exercieses.

- [Aggregation in Peewee ORM](http://docs.peewee-orm.com/en/latest/peewee/query_examples.html#aggregation)
- [Flask Getting Started](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
- [Flask routing](http://flask.pocoo.org/snippets/57/)
- [Flask Context processors](http://flask.pocoo.org/docs/1.0/templating/#context-processors)
- [What is a Web server](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_web_server)


## 0.0.3. What is not supported
This project is not tested using Jupyter Notebook, PyCharm,
Spider, or any other ide/text editor/programming environment for that matter.
Atom or Sublime Text and the command line are the only supported development
environment for this project.

Sounds good? Then let's dive into building a fully functional web app using flask.

## 0.0.4. Minimum Viable Product
Our objective is to build a dashboard that tells the story of the progress 
of a mentee during the mentorship program. The key metrics on this dashboard
comes from data captured by them using the command line tool built in Part 
1 of this project. We want to get insights on the time spent in each task type,
and the effect of each task on the entire progress. Later in Part 3 we will use
data science approaches to analyze any patterns in this data.

![](dashboard.gif)

This is just a reference implementation to give you an idea of what a dashboard
might look like, but you are not required to stick to this and encouraged to
think of your own design. 

## 0.0.5. Flask
For building the web interface, we will be using Flask.
Flask is a micro web framework - it takes care of handling of the HTTP
protocol for you and allows you focus on your application. It is flexible,
lightweight yet powerful.

## 0.0.6. Setup your environment
### 0.0.6.1. Get the source code
- If you are familiar with `git`, run

		git clone https://github.com/chicagopython/CodingWorkshops.git

- If not, go to https://github.com/chicagopython/CodingWorkshops
- Click on the Download Zip and unzip the file that gets downloaded
- From your command line, change directory to the path where you have downloaded it.
- On linux or OS X

 		> cd path/to/CodingWorkshops/problems/webdev/flask_trackcoder/

- On Windows

		> cd path\to\CodingWorkshops\problems\webdev\flask_trackcoder


## 0.0.7. Files

- `app.py` - Here you will find the basic skeleton of the flask app. This is where you will be
  writing your python code for controlling the business logic of the problem.
- `static/styles` - If you want to add static css and javascript, that goes here. [Docs](http://flask.pocoo.org/docs/1.0/tutorial/static/)
- `templates` - This folder has the file `tasks.html` which serves as the view for your app, rendering the data on the browser. [Docs](http://flask.pocoo.org/docs/1.0/tutorial/templates/) 

## 0.0.8. Set up virtualenv
If you are using Linux or OS X, run the following to create a new virtualenv

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    export FLASK_APP=app.py

On Windows, run the following

    python3 -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    set %FLASK_APP%=app.py


## 0.0.9. Feature 0: run app.py
With your environment now set up run

    flask run

This will start a web server on port 5000.
Next load up http://locahost:5000/tasks in your web browser. 

This will show you the list of tasks that have been added to the database built and provided
in Part 1 of our project.


## 0.0.10. Exercise 1: Shows the list of tasks that a mentee has added
`app.py` is the script is where the magic happens.

Lets start with the routes:

    @app.route('/tasks/<task>', methods=['GET', 'POST'])
    def tasks(task):
            tasks = [t for t in ToDo.select()]
        return render_template('tasks.html', tasks=tasks)

Visit http://localhost:5000/tasks and you will see all the tasks.
How many tasks do you see?

Feel free to add your own tasks 

    cd ../../py101/trackcoder/  # change to Part 1
    python app.py -a d 5  "#bootstrap trying to get form alignment working"

Now if you refresh the page, you should be able to see the tasks you added on
the dashboard.

## 0.0.11. Exercise 2: Shows the list of tasks of a particular type

Recall that we have the following task types.
 - blogging (b)
 - coding (c)
 - debugging (d)
 - pair programming at project night (p)
 - research (r)
 - meeting with mentor (m)

Change the tasks route so that it takes a parameter of task type and filters
out tasks of only that type. In absence of any task type, we should be
able to see all the tasks.

Note: The data comes from database which is located in the folder
'../../py101/trackcoder/to_do_list.db'. Changing it to another sqlite file,
would change what you see on the dashboard.

## 0.0.13. Exercise 3: Show the total time spent by the mentee for each of the task types

Find the cummulative time spent on each task type. These times should be 
placed next to each other so that it is easy to compare how much time
is devoted into each of the activity.

Hint: You might find [context processors](http://flask.pocoo.org/docs/1.0/templating/#context-processors)
useful.

## 0.0.12. Exercise 4: Build a better UI
UI/UX is critical to keep your audience engaged. The sample template `tasks.html`, comes with
bootstap integrated, however it does not use any additional styling yet. That is what you would be doing as a part of this exercise.

Here is the template from Bootrap that is used in the demo above.
https://getbootstrap.com/docs/4.0/examples/dashboard/

It can be downloaded from https://getbootstrap.com/docs/4.0/examples/, however please feel
free go with anything else that suits your team's design.

Hint: your html template should go to `template` directory and the `css` or `js`
files should go into `static/styles` directory.

Note: Using a content delivery network, or CDN, you can get bootstrap css, js files into your app.

    <!-- Latest compiled and minified CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

    <!-- Latest compiled and minified JavaScript -->
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>

If you are adding a css file locally, you can do it in the following manner

    <link rel="stylesheet" href="{{ url_for('static',filename='styles/dashboard.css') }}">

Bootstrap natively supports cards, and you see the examples [here](https://getbootstrap.com/docs/4.0/components/card/).

## 0.0.14. Exercise 5: Integrate the task filtering with these aggregate metrics 

Provide a way to easily filter out tasks of each type. Take a look at the demo above,
on how it uses the cards almost as a button to filter each task type. Feel free to
come up with your own design.

## 0.0.15. Exercise 6: Add tasks from UI

Add a form to the UI so that you can add a task from the web frontend.
The task will take in three parameters 
- a task type
- minutes spent
- description

For example: 

    d, 30, #flask form submission 

could be an entry for the task.

## 0.0.16. Exercise 7: Show the list of hashtags and their corresponding counts

Some of the task descriptions have hashtags in them that allows quickly aggregating
on content type in addition to task type. For example, multiple tasks could
be on the content - for example "asyncio" or "data_science". By filteing on hashtag,
we would be able to see task types and time spent on them.

Hint: You might find [context processors](http://flask.pocoo.org/docs/1.0/templating/#context-processors)
useful.
