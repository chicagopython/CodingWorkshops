<!-- TOC -->

- [1. Flask Dashboard for tracking developer time](#1-flask-dashboard-for-tracking-developer-time)
    - [1.1. Is this project for you](#11-is-this-project-for-you)
    - [1.2. Reference documents](#12-reference-documents)
    - [1.3. What is not supported](#13-what-is-not-supported)
    - [1.4. Minimum Viable Product](#14-minimum-viable-product)
    - [1.5. Flask](#15-flask)
    - [1.6. Setup your environment](#16-setup-your-environment)
        - [1.6.1. Get the source code](#161-get-the-source-code)
    - [1.7. Files](#17-files)
    - [1.8. Set up virtualenv](#18-set-up-virtualenv)
    - [1.9. run app.py](#19-run-apppy)
    - [1.10. Shows the list of tasks that a mentee has added](#110-shows-the-list-of-tasks-that-a-mentee-has-added)
    - [1.11. Shows the list of tasks of a particular type](#111-shows-the-list-of-tasks-of-a-particular-type)
    - [1.12. Add a form to search for tasks](#112-add-a-form-to-search-for-tasks)
    - [1.13. Add a from to add new Task from the UI](#113-add-a-from-to-add-new-task-from-the-ui)
    - [1.14. Show the total time spent by the mentee for each of the task types](#114-show-the-total-time-spent-by-the-mentee-for-each-of-the-task-types)
    - [1.15. Improve the UI](#115-improve-the-ui)
    - [1.16. Integrate the task filtering with these aggregate metrics](#116-integrate-the-task-filtering-with-these-aggregate-metrics)
    - [1.17. Show the list of hashtags and their corresponding counts](#117-show-the-list-of-hashtags-and-their-corresponding-counts)

<!-- /TOC -->
# 1. Flask Dashboard for tracking developer time

Chipy's mentorship program is an extra-ordinary jounery for becoming a better developer. As a mentee, you are expected to do a lot - you read new articles/books, write code, debug and troubleshoot, pair program with other mentees in coding workshop or your mentor. This is involves managing time efficiently and doing the effective things. But as the old adage goes, "you can't manage what you can't measure".

This project is the second of the three part series of building tools for the mentees for tracking time. The end goal of such a tool will be to aggregate anonymous data and analyze how does a typical mentee spend on blogging (b), coding (c), debugging (d), pair program (p) with mentor or other mentees.

In this project we will be building a fully functional web dashboard for tracking developer efforts using Flask.

Short url for this page: **http://bit.ly/flask_trackcoder**

## 1.1. Is this project for you

Before you progress further, let's check if we are ready to solve this. You should

- Have a personal computer with working wifi and power cord
- Have Python 3 installed on your computer. Yep, Python 3 only
- Have [Atom](https://atom.io/) or [Sublime Text](https://www.sublimetext.com/3) installed in your computer
- Have written & ran programs in Python from the command line
- Have some idea about lists, dictionaries and functions
- Have created a virtual environment and installing packages with `pip`
- You have read the [flask quick introduction](http://flask.pocoo.org/docs/0.12/quickstart/)

In addition, you should be familiar with [Part 1](https://github.com/chicagopython/CodingWorkshops/tree/master/problems/py101/trackcoder) of this three part exercise.

## 1.2. Reference documents

Reading these links before attending project night, would help you a lot by providing
the background needed to work through the exercieses.

- [What is a Web server](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_web_server)
- [Flask Quick Start](http://flask.pocoo.org/docs/1.0/quickstart/)
- [Flask routing](http://flask.pocoo.org/snippets/57/)
- [Flask Web Forms](https://pythonspot.com/flask-web-forms/)
- [Flask Context processors](http://flask.pocoo.org/docs/1.0/templating/#context-processors)
- [Aggregation in Peewee ORM](http://docs.peewee-orm.com/en/latest/peewee/query_examples.html#aggregation)

## 1.3. What is not supported

This project is not tested using Jupyter Notebook, PyCharm,
Spider, or any other ide/text editor/programming environment for that matter.
Atom or Sublime Text and the command line are the only supported development
environment for this project.

Sounds good? Then let's dive into building a fully functional web app using flask.

## 1.4. Minimum Viable Product

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

## 1.5. Flask

For building the web interface, we will be using Flask.
Flask is a micro web framework - it takes care of handling of the HTTP
protocol for you and allows you focus on your application. It is flexible,
lightweight yet powerful.

## 1.6. Setup your environment

### 1.6.1. Get the source code

If you are familiar with `git`, run

    git clone https://github.com/chicagopython/CodingWorkshops.git

- If not, go to https://github.com/chicagopython/CodingWorkshops
- Click on the Download Zip and unzip the file that gets downloaded
- From your command line, change directory to the path where you have downloaded it.
- On linux or OS X

        > cd path/to/CodingWorkshops/problems/webdev/flask_trackcoder/

- On Windows

        > cd path\to\CodingWorkshops\problems\webdev\flask_trackcoder

## 1.7. Files

- `app.py` - Here you will find the basic skeleton of the flask app. This is where you will be
  writing your python code for controlling the business logic of the problem.
- `static/styles` - If you want to add static css and javascript, that goes here. [Docs](http://flask.pocoo.org/docs/1.0/tutorial/static/)
- `templates` - This folder has the file `tasks.html` which serves as the view for your app, rendering the data on the browser. [Docs](http://flask.pocoo.org/docs/1.0/tutorial/templates/) 

## 1.8. Set up virtualenv

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

## 1.9. run app.py

With your environment now set up run

    flask run

This will start a web server on port 5000.
Next load up http://locahost:5000/tasks in your web browser.

This will show you the list of tasks that have been added to the database built and provided
in Part 1 of our project.

## 1.10. Shows the list of tasks that a mentee has added

`app.py` is the script is where the magic happens.

Lets start with the routes:

    @app.route('/tasks/<task>', methods=['GET', 'POST'], defaults={'tasks':None})
    def tasks(task):
        tasks = [t for t in ToDo.select()]
        return render_template('tasks.html', tasks=tasks)

Visit http://localhost:5000/tasks and you will see all the tasks.
How many tasks do you see?

Feel free to add your own tasks

    cd ../../py101/trackcoder/  # change directory to go to Part 1
    python app.py -a d 5  "#bootstrap trying to get form alignment working"

Now if you refresh the page, you should be able to see the tasks you added on
the dashboard.

## 1.11. Shows the list of tasks of a particular type

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

Think how will you handle if an invalid task type is requested.

## 1.12. Add a form to search for tasks

Add a search text box that allows the user to search with any word that might
appear on the description of the task.

Hint: Take a look at the example of Flask-WTF above. You'll also need to take
a look at [how to do substring search](http://docs.peewee-orm.com/en/latest/peewee/query_operators.html?highlight=contains) usnig peewee.

## 1.13. Add a from to add new Task from the UI

Add a form to the UI so that you can add a task from the web frontend.
The task will take in three parameters

- a task type
- minutes spent
- description

Think about the UI from the user's perspective. Instead of having to fill in three fields
you may choose to have one single text box, where they can enter

    d, 30, #flask form submission

and you handle splitting the input into task type, minutes, description.

## 1.14. Show the total time spent by the mentee for each of the task types

Find the cummulative time spent on each task type. These should be
placed next to each other so that it is easy to compare how much time
is devoted into each of the activity.

Hint: While there might be different ways of doing this, you might find [context processors](http://flask.pocoo.org/docs/1.0/templating/#context-processors)
useful.

## 1.15. Improve the UI

UI/UX is critical to keep your audience engaged. The sample template `tasks.html`, comes with
bootstap integrated, however it does not use any additional styling yet.

Here is the template from Bootrap that is used in the demo above.
https://getbootstrap.com/docs/4.0/examples/dashboard/. It can be downloaded from https://getbootstrap.com/docs/4.0/examples/.

Feel free to go with any styling that goes with your team's design.

Your html template should go to `template` directory and the `css` or `js`
files should go into `static/styles` directory.

## 1.16. Integrate the task filtering with these aggregate metrics

Now that you have a way to filter by task type and aggregated metrics on each task type, integrate these to provide a more unified user experience. Take a look at the demo above, on how it uses the cards almost as a button to filter each task type. Feel free to come up with your own design.

Hint: Cards are a very common way of displaying aggregated information and Bootstrap natively supports cards. You see the examples [here](https://getbootstrap.com/docs/4.0/components/card/).

## 1.17. Show the list of hashtags and their corresponding counts

Adding hashtags on task descriptions allows aggregating the efforts
on another dimension than the pre-defined task types. For example, if
you want to see how much time was spent on debugging on
"#data science" vs "asyncio", aggregating on tasks that have those
hashtags is an easy way.

Provide a way to aggregate the hashtags that has been used in the tasks
and show the count next to each of them. Clicking on a particlar
hashtag should show only the tasks that have that hashtag.
