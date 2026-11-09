"""Pelaajan tiedot."""

class Player:
    """Yksittäinen NHL-peaaja."""

    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.nationality = player_dict['nationality']
        self.assists = player_dict['assists']
        self.goals = player_dict['goals']
        self.team = player_dict['team']
        self.games = player_dict['games']
        self.id = player_dict.get('id')

    @property #kirjoitan palyer.points ilman sulkuja
    def points(self):
        """Maalit ja syötöt yhteensä."""
        return self.goals + self.assists

    def __str__(self):
        return (f"{self.name:20} {self.team:20}"
                f"{self.goals:2} + {self.assists:2} = {self.points:3}")
