# Intro to PyTest
This is a gentle introduction to testing with pytest.
We will use the problem that we have seen before
at project night, how to group people into teams of 4.

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
    source venve/bin/activate


To install the requirements run

    pip3 install -r requirements.txt

This will install pytest and other required packages.

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


# TODO 
Add virtual env for windows