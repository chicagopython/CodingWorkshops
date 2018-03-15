In this project we will be building a fully functional web app using
Flask.

### The project
In the [team project command line application](https://github.com/chicagopython/CodingWorkshops/tree/master/problems/py101/python_team_project), we built an awesome command line
application for creating teams out of people who have RSVP-ed for a Python Project
Night. However, it is much easier to give a link of your app to someone
than asking them to use a command line. So, we will create a web app, that allows
forming teams from the list of RSVP-s from meetup.com. We
will ask for the number of lines of code that a person has written in
Python or an equivalent language and use it for putting them in a team. The number of lines is just a rough estimate. As a reference, the linux kernel is over 23 million lines of code!

In short, imagine this as a tool that one of the
organizers uses to checkin attendees as they start coming in on the day of
Project Night.

Short url for this page: **https://git.io/vdQj6**

### Is this project for you
Before you progress further, let's check if we are ready to solve this. You should
- Have a personal computer with working wifi and power cord
- Have Python 3 installed on your computer. Yep, Python 3 only.
- Have [Atom](https://atom.io/) or [Sublime Text](https://www.sublimetext.com/3) installed in your computer.
- Have written & ran programs in Python from the command line
- Have some idea about lists, dictionaries and functions
- Have created a virtual environment and installing packages with `pip`
- You have read the [flask quick introduction](http://flask.pocoo.org/docs/0.12/quickstart/)

### What is not supported
This project is not tested using Jupyter Notebook, PyCharm,
Spider, or any other ide/text editor/programming environment for that matter.
Atom or Sublime Text and the command line are the only supported development
environment for this project.

Sounds good? Then let's dive into building a fully functional web app using flask.

### Minimum Viable Product
Our objective is to build an web based interface using Flask that
- Shows a list of people who have RSVP-ed for the project Night
- Each entry in the list should have
  - The name of the person
  - The meetup.com profile image of the person
  - An input text box that allows entering lines of code
- On hitting the submit button we should get teams of four


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

 		> cd path/to/CodingWorkshops/problems/webdev/flask_team_project/

- On Windows

		> cd path\to\CodingWorkshops\problems\webdev\flask_team_project


Here you will find the basic skeleton of the app under `app.py`.

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

[![asciicast](https://asciinema.org/a/M1hP91h153PuOPEjVYbot6jPj.png)](https://asciinema.org/a/M1hP91h153PuOPEjVYbot6jPj)

### Feature 0: run app.py
With your environment now set up run

    flask run

And you'll see 🔥.

The reason is there is a string in the `app.py` file that allows meetup.com to identify who is trying to get data from them. It is called the API key. The one currently in the code is one of my old ones. You need to get one for your team from [here](https://secure.meetup.com/meetup_api/key/) - obviously, you'll have to be logged into meetup.com to get the key.
Plug in your key whereever most relevant in `app.py` and run the above command again.

This will start a [web server](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_web_server) on port 5000.
Next load up http://locahost:5000/rsvps in your web browser. 

This will show you the list of people who RSVPed for a previous meetup.
Goto tonight's meetup page and get the meetup id from the url.

   https://www.meetup.com/_ChiPy_/events/244121900/
   
The last section of the url is the `event_id`.

### Feature 1: Read app.py
`app.py` is the script is where the magic happens.

Lets start at the routes:

    @app.route('/rsvps')
    def rsvps():


    @app.route('/teams', methods=['GET', 'POST'])
    def teams():

Discuss among the team how render_template function is used in rsvps and teams
function.

Two useful tools are pretty print and `pdb`

#### Pretty print

    >> from pprint import pprint as pp
    >> pp(member_rsvps)

This will give you a better view of what the function `get_names()` returns.

#### pdb
Python comes with a debugger `pdb`. Here's a [cheat sheet](https://appletree.or.kr/quick_reference_cards/Python/Python%20Debugger%20Cheatsheet.pdf)

You can stick the following line anywhere in the code and make it halt so that you can better inspect the data and flow.

    import pdb; pdb.set_trace()

### Feature 2: Show profile images in rsvps
Make changes to rsvps.html (inside templates) to show images of next to the
names of the people.

### Feature 3: Add a text box next for lines of code
Add an input type textbox that will take a number as input

### Feature 4: Display the lines of code
On hitting submit, the numbers you entered against each person should show up
on the `/teams` page.

### Feature 5: Display teams
As of now, everybody is listed under one team: Team 1.
Split the list of people selected into teams of 4

Your display of each team should include

    Team Number: XYZ
    Name of team member1, Lines of code, (pic)
    Name of team member2, Lines of code, (pic)
    Name of team member3, Lines of code, (pic)
    Name of team member4, Lines of code, (pic)
    (Total lines of code:)

where things in () are optional.
There is no specific criteria for creating the teams as of now. We handle that
next.

### Feature 6: Tell the world
Record a gif of your app in motion and tweet tweet the link to @chicagopython with "Python Project Night Mentorship". Include the twitter handles of your team members.

### Feature 7: Integrate team creating logic (optional)
Code reuse is a hallmark well written code base. Of course, we are
not talking about copy pasting the code, but using the abstractions that a
programming language provides so that there is minimum duplication of code.

Use the code that you wrote in the team project command line application. The logic
that you have implemented earlier for grouping your list of people into teams
should now be used for creating your teams.

Thanks! Thats all folks!
If you found a bug or think you some instructions are missing - just open a issue in this repository.
