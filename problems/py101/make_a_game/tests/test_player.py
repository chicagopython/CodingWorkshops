import pytest

from lib.player import Player


class TestPlayer:
    def test_player_says_hello(self):
        assert Player().say_hello() == "Hello!"

    def test_player_sets_name(self):
        player = Player()
        player.set_name("Player Name")
        assert player.name == "Player Name"

    def test_player_repeats_message(self):
        assert Player().repeat("A message") == "A message"

    def test_player_updates_play_state(self):
        player = Player()
        # assert default player state
        assert player.in_game is True
        # assert we can set player to inactive
        player.in_game = False
        # assert that the player state has changed
        assert player.in_game is False

    def test_cannot_update_player_to_invalid_state(self):
        player = Player()
        with pytest.raises(Exception):
            player.in_game = "Some kind of invalid state!"
