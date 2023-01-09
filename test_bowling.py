from bowling import BowlingGame


class TestBowling:

    def test_gutter_game(self):
        game = BowlingGame()
        for _ in range(20):
            game.roll(0)

        assert game.score() == 0
