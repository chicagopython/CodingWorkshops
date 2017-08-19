# Intro to PyTest
This is a gentle introduction to testing with pytest.
We will use the problem that we have seen before
at project night, [how to group people into teams of 4](https://github.com/chicagopython/CodingWorkshops/blob/master/problems/py101/python_team_project).


team_organizer.py is simplified implementation of the
problem.

test_team_organizer.py is the test for the module.
It has one test implemented to show you what a unit
test in pytest looks like. You Will need to implement
the rest of the tests. Feel free to add more tests.

Documentation: https://docs.pytest.org/en/latest/

# Installation instruction
This exercise is Python 3 only. Follow instructions on the
main wiki to see how to install python3.


First create a virtual environment

    python3 -m venv venv
    source venv/bin/activate


To install the requirements run

    pip3 install -r requirements.txt

This will install pytest and other required packages.

# Run the program
Start by running

      python team_organizer.py

This will drop you to the program's interactive prompt.
Below is a sample interaction where users named a, b, c, 
d, e and f are added using the add command.
Following that, we run the print command where the users
are grouped in to max of size four where two users have
written less lines of code than the others.

     t (master *) testing $ python team_organizer.py 
     Welcome to Chicago Python Project Night Team Organizer
     org> help
     help
     
     Documented commands (type help <topic>):
     ========================================
     add  help  print
     
     Undocumented commands:
     ======================
     exit
     
     org> help add
     help add
     Adds a new user. Needs Name, slackhandle, number of lines
     org> add a @a 100
     add a @a 100
     org> add b @b 200
     add b @b 200
     org> add c @c 300
     add c @c 300
     org> add d @d 400
     add d @d 400
     org> add e @e 500
     add e @e 500
     org> add f @f 50
     add f @f 50
     org> print
     print
     ['f, a, e, d']
     b, c
     org> 
     


# Running the tests

Simply run pytest at the command prompt.
This will run the tests in the test_team_organizer.py

By default pytest will capture everything that goes into
stdout, so that it can have better control over what is
printed out. If you are adding print statements to see
what values your variables have run

    pytest -s

While we do not go into much depth of what can be achieved by
pytest (coming soon to a future project night), here is one cool 
feature you will enjoy.

Say you have hundreds of tests (unlikely for this
exercise), you can easily parallelize those tests by

    pytest -n3

Where 3 is the number of cpus you want to distribute
your tests to.


# Coverage and Styleguide
Once you run pytest, it will show you coverage information
about your code. Also if your code has some styling issue
pytest will fail until you fix your code to be pycodestyle
compliant.

If you want to disble these checking, you can edit
the pytest.ini file and remove the --flake8 or --cov options

# TODO 
Add virtual env for windows