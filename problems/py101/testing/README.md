**Introduction to PyTest and Continuous Integration**

[![Build Status](https://travis-ci.org/chipycodingworkshop/CodingWorkshops.svg?branch=develop%2Fci)](https://travis-ci.org/chipycodingworkshop/CodingWorkshops)

Objective:

- Introduction to unit testing with pytest
- How to setup continuous integration with Github and Travis-CI

<!-- TOC -->

- [1. Setup Instructions](#1-setup-instructions)
    - [1.1. Git and Github](#11-git-and-github)
    - [1.2. Travis setup](#12-travis-setup)
    - [1.3. Python](#13-python)
- [2. Quick Git command refresher](#2-quick-git-command-refresher)
- [3. Exercise 0: Project Setup](#3-exercise-0-project-setup)
    - [3.1. `team_organizer.py`](#31-team_organizerpy)
    - [3.2. `test_team_organizer.py`](#32-test_team_organizerpy)
    - [3.3. `Makefile`](#33-makefile)
    - [3.4. `Pipfile` and `Pipfile.lock`](#34-pipfile-and-pipfilelock)
    - [3.5. `pytest.ini`](#35-pytestini)
    - [3.6. `travis.yml`](#36-travisyml)

<!-- /TOC -->

# 1. Setup Instructions

## 1.1. Git and Github

After completing the above steps you should have a github account and be able to push
your local changes to this repository to github.

- Follow the setup steps described [here](https://help.github.com/articles/set-up-git/)
- Follow the steps described in [fork a repo](https://help.github.com/articles/fork-a-repo
- Now fork [this repository](https://github.com/chicagopython/CodingWorkshops) by clicking the fork button

## 1.2. Travis setup

In this section we will set up a Continuous Integration pipeline
with Travis-ci.

- First, head over to [Travis-CI.org](https://travis-ci.org/.)
- Sign in with your Github account, and accept the terms and conditions.
- On success, you should be at your profile page that lists the CodingWorkshop repository.
- Once you have located the repo, toggle the button next to the repository to enable pipeline travis CI

If you have multiple repositories, you will have to search for the repository.

## 1.3. Python

This project has made no attempt to be compatible with Python 2.7. 😎

Recommended version: Python 3.6

# 2. Quick Git command refresher

Below are the few most used git commands

    git checkout develop/ci      # checkout to develop/ci branch
    git checkout -b feature/cool # crate a new branch feature/cool
    git add -u                   # stage all the updates for commit
    git commit -am "Adding changes and commiting with a comment"
    git push origin develop/ci   # push commits to develop/ci branch

# 3. Exercise 0: Project Setup

By this step you should have the forked version of CodingWorkshop
repository in your machine. Lets take the time to look at the structure of this
project. All code is located under `/problems/py101/testing` directory.
Make sure you are in this directory for the remainder of this project.

Run `pwd` (`cwd` for Windows) on the command prompt to find out which directory you
are on.

Your output should end in `problems/py101/testing` and contain the files described
below.

## 3.1. `team_organizer.py`

This file is a simplified implementation of the problem of grouping the project
night attendees into teams of four based on the number of lines of code they have
written such that two team members have more lines of code than the other.
This is the system under test.

## 3.2. `test_team_organizer.py`

This file is the test for the above module written using Pytest.

These are two files mentioned above are the only two files that we will be making
modifications to for this project.

## 3.3. `Makefile`

This file contains the commands that are required building the project.
You can run `make help` to see what are the options.

## 3.4. `Pipfile` and `Pipfile.lock`

These two files are used by `pipenv` to create a virtual enviornment that
isolates all the dependencies of this project from other python projects in your computer.
Learn more about [pipenv](https://docs.pipenv.org/).

## 3.5. `pytest.ini`

This file contains the configuration for `pytest`.

## 3.6. `travis.yml`

In addition to all the files in this directory, located at the root of the repository,
is a file called `.travis.yml`. This is used by the continuous intergration tool travis-ci.
This contains the information on how to build this python project.
