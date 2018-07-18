# 1. Introduction to PyTest and Continuous Integration

<!-- TOC -->

- [1. Introduction to PyTest and Continuous Integration](#1-introduction-to-pytest-and-continuous-integration)
    - [2. Setup Instructions](#2-setup-instructions)
        - [2.1. Git and Github](#21-git-and-github)
        - [2.2. Travis setup](#22-travis-setup)
    - [2.3. Python](#23-python)
    - [3. Quick Git command refresher](#3-quick-git-command-refresher)
    - [4. Exercise 0: Project Setup](#4-exercise-0-project-setup)
        - [4.1. `team_organizer.py`](#41-team_organizerpy)
        - [4.2. `test_team_organizer.py`](#42-test_team_organizerpy)
        - [4.3. `Makefile`](#43-makefile)
        - [4.4. `Pipfile` and `Pipfile.lock`](#44-pipfile-and-pipfilelock)
        - [4.5. `pytest.ini`](#45-pytestini)
        - [4.6. `travis.yml`](#46-travisyml)
        - [Test your setup is working](#test-your-setup-is-working)

<!-- /TOC -->

Testing and Continuous Integration is at the heart of building good software.
For this project we will be focus on writing tests for a given problem and use
travis-ci for running them automatically everytime code is checked in.

Objective:

- Introduction to unit testing with pytest
- How to setup continuous integration with Github and Travis-CI

## 2. Setup Instructions

### 2.1. Git and Github

After completing the steps below you should have a github account and be able to push
your local changes to this repository to github.

- Follow the setup steps described [here](https://help.github.com/articles/set-up-git/)
- Follow the steps described in [fork a repo](https://help.github.com/articles/fork-a-repo
- Now fork [this repository](https://github.com/chicagopython/CodingWorkshops) by clicking the fork button

The changes that you make as a part of this exercise, will be pushed to the fork you created for this
repository.

In case you already have created a fork of this repository in your github account, you will
want to bring it up to date with the recent changes. In that case,
you will need to do the following:

- [configuring a remote fork](https://help.github.com/articles/configuring-a-remote-for-a-fork/)
- [syncing a fok](https://help.github.com/articles/syncing-a-fork/)

### 2.2. Travis setup

In this section we will set up a Continuous Integration pipeline with Travis-ci.

- First, head over to [Travis-CI.org](https://travis-ci.org/.)
- Sign in with your Github account, and accept the terms and conditions.
- On success, you should be at your profile page that lists the CodingWorkshop repository.
- Once you have located the repo, toggle the button next to the repository to enable pipeline travis CI

If you have multiple repositories, you will have to search for the repository by typing in the name
of the repository (CodingWorkshop) in the search bar on the dashboard page.

## 2.3. Python

This project has made no attempt to be compatible with Python 2.7. 😎

Recommended version: Python 3.6

## 3. Quick Git command refresher

Below are the few most used git commands

    git checkout develop/ci      # checkout to develop/ci branch
    git checkout -b feature/cool # crate a new branch feature/cool
    git add -u                   # stage all the updates for commit
    git commit -am "Adding changes and commiting with a comment"
    git push origin develop/ci   # push commits to develop/ci branch

## 4. Exercise 0: Project Setup

By this step you should have the forked version of CodingWorkshop
repository in your machine. Lets take the time to look at the structure of this
project. All code is located under `/problems/py101/testing` directory.
Make sure you are in this directory for the remainder of this project.

Run `pwd` (`cwd` for Windows) on the command prompt to find out which directory you
are on.

Your output should end in `problems/py101/testing` and contain the files described
below.

### 4.1. `team_organizer.py`

This file is a simplified implementation of the problem of grouping the project
night attendees into teams of four based on the number of lines of code they have
written such that two team members have more lines of code than the other.
This is the system under test.

### 4.2. `test_team_organizer.py`

This file is the test for the above module written using Pytest.

These are two files mentioned above are the only two files that we will be making
modifications to for this project.

### 4.3. `Makefile`

This file contains the commands that are required building the project.
You can run `make help` to see what are the options.

### 4.4. `Pipfile` and `Pipfile.lock`

These two files are used by `pipenv` to create a virtual enviornment that
isolates all the dependencies of this project from other python projects in your computer.
Learn more about [pipenv](https://docs.pipenv.org/).

### 4.5. `pytest.ini`

This file contains the configuration for `pytest`.

### 4.6. `travis.yml`

In addition to all the files in this directory, located at the root of the repository,
is a file called `.travis.yml`. This is used by the continuous intergration tool travis-ci.
This contains the information on how to build this python project.

### Test your setup is working

Just make a small edit on this file, and push the changes to your branch.
If travis-ci.org shows the tests have passed, Congratulations - you are now
ready to dive in.

