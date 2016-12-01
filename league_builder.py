import csv

# Define list of team names
teams = {'Raptors': [], 'Sharks': [], 'Dragons': []}

# Define function to read in the roster of players
def get_roster():
    with open('soccer_players.csv') as file:
        read_roster = csv.DictReader(file)
        roster = list(read_roster)
    return roster

# define function to filter experience players into a separate list
def get_players():
    # read roster in and define empty list to hold players
    roster = get_roster()
    exp_players_list = []
    other_players = []

    # sort through list of players,
    # divide into playes with and witout experience
    for player in roster:
        if player['Soccer Experience'] == "YES":
            exp_players_list.append(player)
        else:
            other_players.append(player)
    return exp_players_list, other_players

# Define function to distribute players by type
# evenly among teams
def distribute_players():
    # get list of players by type
    exp_players_list, other_players_list = get_players()

    # calculate the max number of players of each type per team
    max_player_type = int(len(exp_players_list)/len(teams))

    for player_list in teams.values():
        for player in range(max_player_type):
            player_list.append("Name: {}, Experience: {}, Guardians: {}".format(other_players_list[player]['Name'], other_players_list[player]['Soccer Experience'], other_players_list[player]['Guardian Name(s)']))
            player_list.append("Name: {}, Experience: {}, Guardians: {}".format(exp_players_list[player]['Name'], exp_players_list[player]['Soccer Experience'], exp_players_list[player]['Guardian Name(s)']))
        del other_players_list[:max_player_type]
        del exp_players_list[:max_player_type]

def print_player_names():
    for team_name, roster in teams.items():
        print(team_name)
        for player in roster:
            print(player)


# make sure script can't be executed when imported
if __name__ == "__main__":
    distribute_players()
    print_player_names()
