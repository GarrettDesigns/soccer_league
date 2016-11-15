import csv

# Define list of team names
teams = {'Raptors': [], 'Sharks': [], 'Dragons': []}

# Define function to read in the roster of players
def distibute_players():
    with open('soccer_players.csv') as file:
        read_roster = csv.DictReader(file)
        roster = list(read_roster)
        print(roster)
        # for player in roster:
        #     for info in player:
        #         print('{}: {}'.format(info, player[info]))

# make sure script can't be executed when imported
if __name__ == "__main__":
    distibute_players()
