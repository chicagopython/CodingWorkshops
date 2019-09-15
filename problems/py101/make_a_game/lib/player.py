class Player:
    def __init__(self):
        self._in_game = True
        self.name = None

    def say_hello(self):
        return "Hello!"

    def set_name(self, name):
        self.name = name

    def repeat(self, message):
        return message

    @property
    def in_game(self):
        return self._in_game

    @in_game.setter
    def in_game(self, game_state):
        if not isinstance(game_state, bool):
            raise Exception("Must set game state to True or False")
        self._in_game = game_state
