"""Pelaajatilastojen tulostus."""

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

from player_reader import PlayerReader
from player_stats import PlayerStats

SEASONS = ["2018-19", "2019-20", "2020-21", "2021-22",
           "2022-23", "2023-24", "2024-25", "2025-26"]

NATIONALITIES = ["USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA",
                 "GBR", "SVK", "DEN", "NED", "AUT", "BLR", "GER", "SUI",
                 "NOR", "UZB", "LAT", "AUS"]

console = Console()


def show_table(season, nationality, players):
    """Tulostaa pelaajat taulukkona."""
    table = Table(title=f"Season {season} players from {nationality}")
    table.add_column("name", style="cyan", no_wrap=True)
    table.add_column("team", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points)
        )
    console.print(table)

def main():
    """Kysyy kauden ja maan sekä tulostaa tilastot."""
    season = Prompt.ask("Season", choices=SEASONS)
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url))

    try:
        while True:
            nationality = Prompt.ask("Nationality", choices=NATIONALITIES)
            players = stats.top_scorers_by_nationality(nationality)
            show_table(season, nationality, players)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
