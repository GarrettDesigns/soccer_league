import csv

# Define list of team names
teams = {'Raptors': [], 'Sharks': [], 'Dragons': []}

def get_roster():
    with open('soccer_players.csv') as file:
        read_roster = csv.DictReader(file)
        roster = list(read_roster)
    return roster

def find_good_players():
    experienced_player_count = 0
    roster = get_roster()
    for player in roster:
        if player['Soccer Experience'] == "YES":
            experienced_player_count += 1

    # print statement for debug purposes, remove in final code
    # print(experienced_player_count)
    return experienced_player_count

# Define function to read in the roster of players
def distribute_players():
    roster = get_roster()
    find_good_players()
    max_player_count = len(roster)/len(teams)
    print(max_player_count)
    for team in teams:
        for player in roster:
            if len(teams[team]) <= max_player_count:
                print(len(teams[team]))
                teams[team].append(player['Name'])

def print_teams():
    distribute_players()
    for team in teams:
        print(teams[team])

print_teams()

# make sure script can't be executed when imported
if __name__ == "__main__":
    distribute_players()
