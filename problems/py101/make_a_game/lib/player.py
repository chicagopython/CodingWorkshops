from .pythonmon import Pythonmon
import random

class Player:
    def __init__(self):
        self._in_game = True
        self.name = None
        self.pymon = None

    def say_hello(self):
        return "Hello!"

    def set_name(self, name):
        self.name = name

    def repeat(self, message):
        return message

    @property
    def in_game(self):
        return self._in_game

    def catch_pymon(self):
        self.has_pymon = True
        list_of_pymon = ["Justin", "Pymander", "Dexter", "Mario"]
        seed = random.randint(0,len(list_of_pymon) - 1)
        name = list_of_pymon[seed]
        self.pymon = Pythonmon(name)
        pass

    def check_pymon(self):
        if self.pymon is not None:
            print(f'Your pymon is called :{self.pymon.name} and has {self.pymon.hp} hp')
        else:
            print("Go catch a Pymon")
        
    def fight_baddie(self):
        if self.pymon is None:
            print("No Pymon")
        else:
            self.pymon.get_attacked()

    @in_game.setter
    def in_game(self, game_state):
        if not isinstance(game_state, bool):
            raise Exception("Must set game state to True or False")
        self._in_game = game_state

    