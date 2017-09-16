The organizers of Project Nights need your help! Grouping people for
project night team project is a manual task. Why do it manually, when
we can automate it? We open the problem to you.

We want a person to record this data as people walk through the door
so they can ask two simple questions in order to assign people into
groups. We want to take the output of this program and drop the text
into Slack to alert everyone that they have been assigned a
group. This is the general way a user would interact with the tool:

## Set up
On Linux, OS X, run the following

	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt
	python app.py

On Windows

	python3 -m venv venv
	venv\Scripts\activate
	pip install -r requirements.txt
	python app.py

[![asciicast](https://asciinema.org/a/M1hP91h153PuOPEjVYbot6jPj.png)](https://asciinema.org/a/M1hP91h153PuOPEjVYbot6jPj)

## Feature 0: Look into app.py
app.py will be the script that we will implement.
We will be using two external libraries for this
program.

	python_prompt_toolkit
	meetup-api

`prompt_toolkit` makes it easy for building command line prompts
with steroids. `meetup-api` provides us with the data for the
meetup.

`class TeamBuilder` is where you would be writing your application
logic.

`main` function will use the TeamBuilder class to run the logic
that your team will be coming up with.

## Feature 1: Add command
Firstly we need to add a person.

	add <name> <lines>

where <name> is the full name of the person as it appears in the
meetup.com and <lines> is the approximate number of lines of code
that person has written in Python or a similar programming language.
Handle if <lines> is not a number.
Handle names that have more than first and last name.

## Feature 2: List command
Show the number of people added and prints the total count
and the median of the line count.

## Feature 3: Group command
Output groups of four such that each group contains
  - 2 person who have written less than median lines of code
  - 2 person who has written more than written more than median
If there are less the four people left to group, then group them
together.  

## Feature 4. Enhance Group command
Add a unique group name

## Feature 5. Enhance Group command
Make up random room names and add a room name for each group.

## Feature 6. Auto-completion for commands
Adding auto completion is easy with prompt_toolkit.
Add the commands you implemented into the list as an input to
WordCompleter.

## Feature 7. Auto-completion for names
Enhancing the auto-completion for the names is next.
The funcion `get_names` uses meetup-api and gets the names. The event
id can be found from the url of tonight's meetup page.

## Feature 8. Group detail command
Enhance the group command to take detail paramter that would take
a group name and list out the detail of the group.

## Feature 9. Enhance Group command
Print the groups sorted with the average number of lines of code.

## Feature 10. Tell the world
We have also installed asciinema - a tool that allows you
to create recordings of your terminal sessions. In order to tell
the world what your team has made, lets make a small recording.

     ascriinmea rec teamname.json

Run your program and show off all the features you have built.
To finish recording hit Ctrl-D.
Next play the recordings

     asciinema play teamname.json

Once the playback looks good, upload it to the interwebs.

     asciinema upload teamname.json

Finally, tweet the link to @chicagopython with "Python Project Night
Mentorship Workshop". Include the twitter handles of your team members.
