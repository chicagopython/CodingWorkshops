# 1. Introduction to PyTest and Continuous Integration

<!-- TOC -->

- [1. Introduction to PyTest and Continuous Integration](#1-introduction-to-pytest-and-continuous-integration)
    - [1.1. Setup Instructions](#11-setup-instructions)
        - [1.1.1. Git and Github](#111-git-and-github)
        - [1.1.2. Travis setup](#112-travis-setup)
    - [1.2. Python](#12-python)
    - [1.3. Quick Git command refresher](#13-quick-git-command-refresher)
    - [1.4. Exercise 0: Project Setup](#14-exercise-0-project-setup)
        - [1.4.1. `team_organizer.py`](#141-team_organizerpy)
        - [1.4.2. `test_team_organizer.py`](#142-test_team_organizerpy)
        - [1.4.3. `Makefile`](#143-makefile)
        - [1.4.4. `Pipfile` and `Pipfile.lock`](#144-pipfile-and-pipfilelock)
        - [1.4.5. `pytest.ini`](#145-pytestini)
        - [1.4.6. `travis.yml`](#146-travisyml)
        - [1.4.8. Test your setup is working](#148-test-your-setup-is-working)

<!-- /TOC -->

Testing and Continuous Integration is at the heart of building good software.
For this project we will be focus on writing tests for a given problem and use
travis-ci for running the tests automatically everytime code is checked into Github.

**Objective**:
In this project we will explore

- Introduction to unit testing with pytest
- How to setup continuous integration with Github and Travis-CI

## 1.1. Setup Instructions

For doing this project you will need a Github account, a Travis-ci.org account and git
installed locally.

### 1.1.1. Git and Github

After completing the steps below you should have a github account and be able to push
your local changes to this repository to github.

- Follow the setup steps described [here](https://help.github.com/articles/set-up-git/)
- Read the steps described in [fork a repo](https://help.github.com/articles/fork-a-repo)
- Use the steps described above to fork this repository [CodingWorkshops](https://github.com/chicagopython/CodingWorkshops)

The changes that you make as a part of this exercise, will be pushed to the fork you created for this
repository.

In case you have already have created a fork of this repository in your github account, you will
want to bring it up to date with the recent changes. In that case,
you will need to do the following:

- [configuring a remote fork](https://help.github.com/articles/configuring-a-remote-for-a-fork/)
- [syncing a fok](https://help.github.com/articles/syncing-a-fork/)

### 1.1.2. Travis setup

Continuous Integrration is a critical part of building your software. It automatically runs
the tests when you check in code into your version control (git) and paves the way for
continuous delivery, i.e. release often and release early.
In this section we will set up a Continuous Integration pipeline with Travis-ci.

- First, head over to [Travis-CI.org](https://travis-ci.org/.)
- Sign in with your Github account, and accept the terms and conditions.
- On success, you will be landing on your profile page that lists the CodingWorkshop repository
- Once you have located the repo, toggle the button next to the repository to enable travis CI

If you have multiple repositories, you will have to search for the repository by typing in the name
of the repository (CodingWorkshop) in the search bar on the dashboard page.

## 1.2. Python

This project has made no attempt to be compatible with Python 2.7. 😎

Recommended version: Python 3.6

## 1.3. Quick Git command refresher

Below are the few most used git commands

    git checkout master          # checkout to master branch
    git checkout -b feature/cool # crate a new branch feature/cool
    git add -u                   # stage all the updates for commit
    git commit -am "Adding changes and commiting with a comment"
    git push origin master       # push commits to develop/ci branch

## 1.4. Exercise 0: Project Setup

After completing the steps in setup, you should have the cloned versoin of the fork of CodingWorkshop
repository in your local machine. Lets take the time to look at the structure of this
project. All code is located under `/problems/py101/testing` directory. So from your
terminal go to the directory where you have cloned the repository.

    cd path/to/clone/problems/py101/testing

Make sure you are in this directory for the remainder of this project.

Run `pwd` (`cwd` for Windows) on the command prompt to find out which directory you
are on.

Your output should end in `problems/py101/testing` and contain the files described
below.

### 1.4.1. `team_organizer.py`

This file is a simplified implementation of the problem of grouping the project
night attendees into teams of four based on the number of lines of code they have
written such that two team members have more lines of code than the other.
This is the system under test.

### 1.4.2. `test_team_organizer.py`

This file is the test for the above module written using Pytest.

These are two files mentioned above are the only two files that we will be making
modifications to for this project.

### 1.4.3. `Makefile`

This file contains the commands that are required building the project.
You can run `make help` to see what are the options.

### 1.4.4. `Pipfile` and `Pipfile.lock`

These two files are used by `pipenv` to create a virtual enviornment that
isolates all the dependencies of this project from other python projects in your computer.
Learn more about [pipenv](https://docs.pipenv.org/).

### 1.4.5. `pytest.ini`

This file contains the configuration for `pytest`.

### 1.4.6. `travis.yml`

In addition to all the files in this directory, located at the root of the repository,
is a file called `.travis.yml`. This is used by the continuous intergration tool travis-ci.
This contains the information on how to build this python project.

### 1.4.8. Test your setup is working

Just make a small edit on this file, and `git push origin master` the changes to your repository.
If travis-ci.org gets triggered and is all green for this push, congratulations - you are now
ready to dive in.

If you run into issues, [ask your question on slack](https://chipy.slack.com/messages/C093F7W8P/details/)
