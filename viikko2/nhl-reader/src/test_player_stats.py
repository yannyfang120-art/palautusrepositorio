"""PlayerStats-luokan yksikkötestit."""

from player import Player
from player_stats import PlayerStats


class StubPlayerReader:
    """Palauttaa testipelaajat ilman verkkopyyntöä."""

    def get_players(self):
        """Palauttaa testejä varten ennalta määritellyt pelaajat."""
        return [
            Player({
                "name": "Player One",
                "nationality": "FIN",
                "assists": 40,
                "goals": 30,
                "team": "AAA",
                "games": 70,
            }),
            Player({
                "name": "Player Two",
                "nationality": "FIN",
                "assists": 20,
                "goals": 10,
                "team": "BBB",
                "games": 70,
            }),
            Player({
                "name": "Player Three",
                "nationality": "CAN",
                "assists": 50,
                "goals": 20,
                "team": "AAA",
                "games": 70,
            }),
            Player({
                "name": "Player Four",
                "nationality": "FIN",
                "assists": 10,
                "goals": 25,
                "team": "AAA",
                "games": 70,
            }),
        ]


def test_top_scorers_by_nationality_filters_and_sorts_by_points():
    """Rajaa pelaajat kansalaisuuden mukaan ja järjestää heidät pisteillä."""
    stats = PlayerStats(StubPlayerReader())

    result = stats.top_scorers_by_nationality("FIN")

    assert [player.name for player in result] == [
        "Player One",
        "Player Four",
        "Player Two",
    ]


def test_top_goal_scorers_returns_requested_number_sorted_by_goals():
    """Palauttaa pyydetyn määrän pelaajia maalien mukaan järjestettynä."""
    stats = PlayerStats(StubPlayerReader())

    result = stats.top_goal_scorers(2)

    assert [player.name for player in result] == ["Player One", "Player Four"]


def test_top_scorers_by_team_filters_and_sorts_by_points():
    """Rajaa pelaajat joukkueen mukaan ja järjestää heidät pisteillä."""
    stats = PlayerStats(StubPlayerReader())

    result = stats.top_scorers_by_team("AAA")

    assert [player.name for player in result] == [
        "Player One",
        "Player Three",
        "Player Four",
    ]
