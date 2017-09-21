The organizers of Project Nights need your help! Grouping people for
team projects is a manual task. Why do it manually, when
we can automate it?

### Is this project for you
Before you progress further, let's check if we are ready to solve this. You should
- Have a personal computer with working wifi and power cord
- Have Python 3 installed on your computer. Yep, Python 3 only.
- Have [Atom](https://atom.io/) or [Sublime Text](https://www.sublimetext.com/3) installed in your computer.
- Have written & ran programs in Python from the command line
- Have some idea about lists, dictionaries and functions
- Have some idea about `virtualenv` and installing packages with `pip`

This project is not tested using Jupyter Notebook, PyCharm,
Spider, or any other ide/text editor/programming environment for that matter.
Atom or Sublime Text and the command line are the only supported development environment for this project.

Short url for this page: **https://git.io/vdv43**

Sounds reasonable? Then let's dive in - and build an awesome command line app using python.


### Can command line applications be cool
You bet!
Checkout this PyCon 2017 video on which this project is based

<a href="http://www.youtube.com/watch?feature=player_embedded&v=hJhZhLg3obk" target="_blank"><img src="http://img.youtube.com/vi/hJhZhLg3obk/0.jpg"
alt="Amjith Ramanujam Awesome Command Line Tools PyCon 2017" width="560" height="315" border="10" /></a>

The slides are available [here](https://speakerdeck.com/pycon2017/amjith-ramanujam-awesome-command-line-tools).

### What is a Team Project
Glad you asked! A team project is an hour long problem solving session where each team
consists of four members of different expertise level. The teams are formed from the
list of attendees of the project night.


### The Objective
Our objective is to build an awesome command line application in Python3 that
- allows creating list of people who want to participate in a team project
- once the list is created, the program automatically creates teams of four

### A Balanced Team
To keep the team composition balanced in terms of experience, we want every team
to have two members with more experience than the other two.
Measuring experience is very subjective and difficult, but we will keep it simple.
We will rely on a (not very scientific) metic - lines of code written till date.

We will create a list by taking names of people from tonight's RSVP list. Along with their name we will also include the number of lines of code that person has written till date in Python or an equivalent language. Imagine this as a tool that one of the organizers uses to checkin attendees as they start coming in on the day of Project Night.

And yeah, this number of lines can be just a rough estimate. As a
reference, the linux kernel is over 23 million lines of code!

### Bootstrap
- If you are familiar with `git`, run

		git clone https://github.com/chicagopython/CodingWorkshops.git

- If not, go to https://github.com/chicagopython/CodingWorkshops
- Click on the Download Zip and unzip the file that gets downloaded
- From your command line, change directory to the path where you have downloaded it.
- On linux or OS X

 		> cd path/to/CodingWorkshops/problems/py101/python_team_project/

- On Windows

		> cd path\to\CodingWorkshops\problems\py101\python_team_project


Here you will find the basic skeleton of the app under `app.py`. (after September 21, 2017)

### Set up virtualenv
If you are using Linux or OS X, run the following to create a new virtualenv

	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt
	python app.py

On Windows, run the following

	python3 -m venv venv
	venv\Scripts\activate
	pip install -r requirements.txt
	python app.py

[![asciicast](https://asciinema.org/a/M1hP91h153PuOPEjVYbot6jPj.png)](https://asciinema.org/a/M1hP91h153PuOPEjVYbot6jPj)

Next let's get started by looking into the code.

## Feature 0: Look into app.py
app.py is the script contains some code to get you started.
We will be using two external libraries for this
program.

	python_prompt_toolkit
	meetup-api

- `prompt_toolkit` makes it easy for building awesome command line apps
- `meetup-api` provides us with the data for the meetup
- `asciinema` which is also in the `requirements.txt` isn't strictly necessary and we'll talk about it last

`execute` function is where you would be writing your application logic.

You should not require to make changes to `main` and `get_names` functions. In an upcoming project nights we will dig into `get_names` and make changes to it.

Next let's run app.py

	   python3 app.py

This should drop you to a prompt.

	>

Type in something to that prompt.

	> Hola amigo
	> You issued: Hola amigo

Try a few more

	> Gracias
	> You issued:Gracias

You can now press the up arrow key and access the history of the commands you have issued. To exit out of the program, you can type Ctrl-D.

	>
  GoodBye!

### Feature 1: Implement the Add command
Next let's create a command where the user of the program can register new participants to build up the list of users from whom teams will be formed.

The command should look like the following

	add <name> <number of lines>

where <name> is the full name of the person as it appears in the
meetup.com and <lines> is the  number of lines of code
that person has written in Python or a similar programming language in their life.

   > add Tathagata Dasgupta 1


### Feature 2: Add some error checking (optional)
You might be asking what if the user incorrectly types something that is not a number
for the `number of lines`. Indeed that would be incorrect. Show an error message
if <number of lines> is not a number.

		> add Tathagata Dasgupta o
		ERROR: number of lines should be, er, a "number"

Are there other error conditions that can arise?

## Feature 2: Implement a List command
Next add a new command list.
Show the number of people added and prints the total count
and the median of the line count.

		> add Tathagata Dasgupta 1
		> add Jason Wirth 2
		> add Adam Bain 3
		> add Brian Ray 4
		> add Guido van Rossum 5
		> list
		> People added so far:
		Tathagata Dasgupta, 1
		Jason Wirth, 2
		Adam Bain, 3
		Brian Ray, 4
		Guido Van Rossum, 5

		Number of people: 5
		Median line count: 3

Your output need not be exactly the same, but should show the
correct data. The Median line count will be used in the next
features.
Hint: Python3 has the statistics module, so you can use

	import statistics
	statistics.median([1,2,3,4,5])


## Feature 3: Add the teams command (optional)
The next command we will implement is `teams` command. Let's say you
have added a few people already and know what the median line count
is for the people you have added so far. On issuing the `teams` command
it should output teams of four such that each team contains
  - 2 person who have written less than the median lines of code
  - 2 person who has written more than written more than median

If there are less the four people left to group, then group them
together.

With our running example, there would be a team of four, and the
remaining 1 should be in another group.

		> teams
		Group 1: Tathagata Dasgupta, Jason Wirth, Brian Ray, Guido Van Rossum
		Group 2: Adam Bain


## Feature 4. Enhance Team command (optional)
Add a unique team name

## Feature 5. Enhance Team command (optional)
Make up random room names and add a room name for each team.

## Feature 6. Enhance Teams command (optional)
Print the teams sorted with the average number of lines of code for each team.

## Feature 7. Auto-completion for commands (optional)
Adding auto completion is easy with `prompt_toolkit`. In `app.py` the following line is used to include the
`add` command to auto-completion.

		command_completer = WordCompleter(['add'], ignore_case=True)

Add the remaining commands.


## Feature 8. Auto-completion for participant names (optional)
Typing in names of the attendees of project night would be time consuming
and error prone. Let's add auto-completion magic to it!

The funcion `get_names` uses meetup-api and returns a list of names for the attendees.
All you need to do is include a call to `get_names` in the command_completer.

## Feature 9. Tell the world (optional, OS X or Linux only)
We have also installed asciinema - a tool that allows you
to create recordings of your terminal sessions. In order to tell
the world what your team has made, let's make a small recording.

     ascriinmea rec teamname.json

Run your program and show off all the cool features you have built in your app.
To finish recording hit Ctrl-D.
Next play the recordings

     asciinema play teamname.json

Once the playback looks good, upload it to the interwebs.

     asciinema upload teamname.json

Finally, tweet the link to @chicagopython with "Python Project Night
Mentorship". Include the twitter handles of your team members.

Note: This is tested only in OS X. Let me know your experience for running it on
other operating systems.
If you see an error

		asciinema needs a UTF-8 native locale to run. Check the output of `locale` command.

the run the following command before running asciinema.

		export LC_ALL=en_US.UTF-8


Thanks! Thats all folks!
If you found a bug or think you some instructions are missing - just open a issue in this repository.
