import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    fin_players = [player for player in players if player.nationality == "FIN"]
    fin_players = sorted(fin_players, key=lambda player: player.points, reverse=True)

    print("Players from FIN:\n")

    for player in fin_players:
        print(player)
        
if __name__ == "__main__":
    main()