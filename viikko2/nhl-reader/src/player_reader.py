"""Pelaajien haku verkosta."""

import requests
from player import Player

class PlayerReader:
    """Hakee pelaajat annetusta osoitteesta."""

    def __init__(self, url):
        self._url = url

    def get_players(self):
        """Palauttaa listan Player-olioita."""
        response = requests.get(self._url, timeout=10).json()
        return [Player(player_dict) for player_dict in response]
