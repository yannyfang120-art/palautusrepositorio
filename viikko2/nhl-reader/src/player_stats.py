class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        player = [p for p in self.players if p.nationality == nationality]
        return sorted(player, key=lambda p: p.points, reverse=True)
    