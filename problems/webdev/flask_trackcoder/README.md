Chipy's mentorship program is an extra-ordinary jounery for becoming a better developer. As a mentee, you are expected to do a lot - you read new articles/books, write code, debug and troubleshoot, pair program with other mentees in coding workshop or your mentor. This is involves managing time efficiently and doing the effective things. But as the old adage goes, "you can't manage what you can't measure".

This project is the second of the three part series of building tools for the mentees for tracking time. The end goal of such a tool will be to aggregate anonymous data and analyze how does a typical mentee spend on blogging (b), coding (c), debugging (d), pair program (p) with mentor or other mentees.

In this project we will be building a fully functional web dashboard for your effort tracking using Flask.


Short url for this page: **https://git.io/vdQj6** #TODO

### Is this project for you
Before you progress further, let's check if we are ready to solve this. You should
- Have a personal computer with working wifi and power cord
- Have Python 3 installed on your computer. Yep, Python 3 only
- Have [Atom](https://atom.io/) or [Sublime Text](https://www.sublimetext.com/3) installed in your computer
- Have written & ran programs in Python from the command line
- Have some idea about lists, dictionaries and functions
- Have created a virtual environment and installing packages with `pip`
- You are able to run the program #TODO from the command line
- You have read the [flask quick introduction](http://flask.pocoo.org/docs/0.12/quickstart/)

### What is not supported
This project is not tested using Jupyter Notebook, PyCharm,
Spider, or any other ide/text editor/programming environment for that matter.
Atom or Sublime Text and the command line are the only supported development
environment for this project.

Sounds good? Then let's dive into building a fully functional web app using flask.

### Minimum Viable Product
Our objective is to build a dashboard that tells the story of the progress 
of a mentee during the mentorship program. The key metrics on this dashboard
comes from data captured by them using the command line tool built in Part 
1 of this project. We want to get insights on the time spent in each task type,
and the effect of each task on the entire progress. Later in Part 3 we will use
some data science approaches to analyze any patterns in this data.


### Flask
For building the web interface, we will be using Flask.
Flask is a micro web framework - it takes care of handling of the HTTP
protocol for you and allows you focus on your application. It is flexible,
lightweight yet powerful.

### Setup your environment
#### Get the source code
- If you are familiar with `git`, run

		git clone https://github.com/chicagopython/CodingWorkshops.git

- If not, go to https://github.com/chicagopython/CodingWorkshops
- Click on the Download Zip and unzip the file that gets downloaded
- From your command line, change directory to the path where you have downloaded it.
- On linux or OS X

 		> cd path/to/CodingWorkshops/problems/webdev/flask_trackcoder/

- On Windows

		> cd path\to\CodingWorkshops\problems\webdev\flask_trackcoder


### Files

- `app.py` - Here you will find the basic skeleton of the flask app
- `static/styles` - If you want to add static css and javascript, that goes here
- `templates` - This file has the html template for showing rendering the data on the browser 

### Set up virtualenv
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

#TODO asciinema

### Feature 0: run app.py
With your environment now set up run

    flask run

This will start a web server on port 5000.
Read more one web servers [here](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_web_server)
Next load up http://locahost:5000/rsvps in your web browser. 

This will show you the list of tasks that have been added to the database built and provided
in Part 1 of our project.

### Exercise 1: Shows the list of tasks that a mentee has added
`app.py` is the script is where the magic happens.

Lets start at the routes:

    @app.route('/tasks/<task>', methods=['GET', 'POST'])
    def tasks(task):
            tasks = [t for t in ToDo.select()]
        return render_template('tasks.html', tasks=tasks)

Visit http://localhost:5000/tasks and you will see all the tasks.
How many tasks do you see?

### Exercise 2: Shows the list of tasks of a particular type

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

### Exercise 4: Build a better UI
UI/UX is critical to keep your audience engaged.

Here is the template from Bootrap that is used in the demo above.
https://getbootstrap.com/docs/4.0/examples/dashboard/

You can download it from https://getbootstrap.com/docs/4.0/examples/, however you can
use any other template you think would be appropriate.

Note: your html template should go to `template` directory and the `css` or `js`
files should go into `static/styles` directory.

Hint: Using a content delivery network, or CDN, you can get bootstrap css, js files into your app.

    <!-- Latest compiled and minified CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

    <!-- Latest compiled and minified JavaScript -->
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>

Hint: If you are adding a css file locally, you can do it in the following manner

    <link rel="stylesheet" href="{{ url_for('static',filename='styles/dashboard.css') }}">


### Exercise 3: Show the total time spent by the mentee for each of the task types

These should be placed next to each other so that one can compare how much time
is devoted into each of the activity.

### Exercise 5: Integrate the task filtering with these aggregate metrics 

Clicking on each of the task types should show only those tasks that are of
that type, and filter out any task which is of different type.

### Exercise 6: Show the list of hashtags and their corresponding counts

Some of the task descriptions have hashtags in them that allows quickly aggregating
on content type in addition to task type. For example, multiple tasks could
be on the content - for example "asyncio" or "data_science". By filteing on hashtag,
we would be able to see task types and time spent on them.

### Exercise 7: Add tasks from UI

Add a form to the UI so that you can add a task from the web frontend.
The task will take in three parameters - a task type, minutes spent, 
and description.

