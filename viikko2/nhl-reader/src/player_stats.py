"""Pelaajatilastot."""

class PlayerStats:
    """Muodostaa tilastoja pelaajalukijan antamista pelaajista."""

    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        """Palauttaa maan pelaajat pisteiden mukaan laskevassa järjestyksessä."""
        player = [p for p in self.players if p.nationality == nationality]
        return sorted(player, key=lambda p: p.points, reverse=True)

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa
        maalimäärän mukaan laskevassa järjestyksessä.
        """
        return sorted(self.players, key=lambda p: p.goals, reverse=True)[:how_many]

    def top_scorers_by_team(self, team):
        """Palauttaa joukkueen pelaajat pisteiden mukaan laskevassa järjestyksessä."""
        players = [p for p in self.players if p.team == team]
        return sorted(players, key=lambda p: p.points, reverse=True)
