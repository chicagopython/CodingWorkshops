# Make a Game

## Overview

For a long time, computer games made use of few, if any, graphics. Many of them were text based adventures that you could run directly on your command line. Some examples included:

- [Zork](https://en.wikipedia.org/wiki/Zork)
- Adventureland
- [Dwarf Fortress](https://en.wikipedia.org/wiki/Dwarf_Fortress)

and many others. Players would input their directions using words and the computer would return back what happened. 

## Your Task

Your task for this evening is to, working together, create something fun to play! Your group will take turns typing (in other words, one computer per group and only one person typing at a time) and helping to develop (offering ideas, thoughts on what to do next, etc.). It can be helpful to have another person with their computer open to research, but ultimately, this is a group effort! Everyone should have a chance to write code, offer suggestions, research libraries, etc. 

## Setup

1. You'll need one computer that your group will share that can install and run [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/). While an OS-X or Linux machine will likely do the best for this step, a Windows machine will be able to do it as well. If you run into any challenges installing Pipenv, please ask for help!
2. The project is in the ChiPy project night repo. If you do not have the repository already, run 

	```
	git clone https://github.com/chicagopython/CodingWorkshops.git
	```

3. Navigate to the folder for this challenge:

	```
	cd CodingWorkshops/problems/py101/make_a_game
	```

4. Run `pipenv install`, which will install all of the libraries we have recommended for this exercise.
5. After you've installed all of the libraries, run `pipenv shell`, which will turn on a virtual environment running Python 3.7.
6. Run `python run.py` to see the program in its current state or `pytest -vv` to run all tests.
7. If you make changes, this project uses a library called [Black](https://github.com/psf/black) to automatically format the code for you (this known as a [linter](https://en.wikipedia.org/wiki/Lint_(software)). To run it, from the root of the directory, run `black .`

## What's in this repository?

In this repository is a basic shell of a game. This game sets up a `Player()` which parrots back what the player writes to it until they decide to leave. Some of the key features here that you might want to use or modify or extend are:

1. _Tests_ -- in the `tests/` folder are a series of tests to make sure that the `Player()` object continues to work as expected. As you add new functionality, you might want to practice [test-driven development](https://en.wikipedia.org/wiki/Test-driven_development) to ensure that your code continues to work as you want it to!
2. _run.py_ -- This is the main file that the player will run to play the game. One thing to note is the section that starts with `while player.in_game:` -- this section sets up a loop that will keep running until the `in_game` attribute is set to False. This way, your players can continue to do things and the game won't run once through the code and immediately finish. You'll likely add extra things into this section.
3. _Player() class_ -- This class holds information about the player -- what its name is, what message it wants to repeat, whether it still wants to play the game...classes are useful for persisting or modifying some sort of collected state or values about a "thing", as well as defining actions that that thing may take. For example, our `Player()` can currently `say_hello()` and it has an `in_game` status that can be either `True` or `False`. A different object might have different behaviors or different attributes that can be set. Depending on your game, you may want to set up more of these classes -- for example, you could set up a `Map()` class to hold onto information about a map (what room the player is currently in, what rooms they can go to, etc.) or an `Enemy()` class (what the enemy can do, how it interacts with the player, whether it is defeated or not, etc.

## So what should we do?

A good way to begin might be the following:

1. Decide what type of game you want to make: do you want to make a madlibs clone? Tic-tac-toe? A small dungeon? A word game? Put together a couple of ideas and identify what you'd like to build (and don't worry if you don't finish in time! This exercise is for you to be introduced to some Python concepts, not to emerge with a fully-developed game).
2. Identify what basic building blocks you would need to interact with in the game. For example, if you were making a madlibs clone, you would want to identify what the user could enter, some scripts for those words to be entered into, and something that reads the story out after all the words have been entered. This can help with figuring out the basic flow of the game (for example, you would not want the story to be revealed before all the words are entered!)
3. Start adding code and testing the game -- you could both add automated tests (like the ones in `tests/` or try playing your game to see if it works. 

Happy Developing!
