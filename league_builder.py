# Loop through teams
# for current team
    # add players from roster by looping through roster
    # until it has 1/3 of the experienced players
    # and the total player count is 1/3 the total players on roster
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

def distribute_players():
    exp_players_list, other_players_list = get_players()
    max_player_type = int(len(exp_players_list)/len(teams))
    for player_list in teams.values():
        for player in range(max_player_type):
            try:
                player_list.append("Name: {}, Experience: {}".format(other_players_list[player]['Name'], other_players_list[player]['Soccer Experience']))
                player_list.append("Name: {}, Experience: {}".format(exp_players_list[player]['Name'], exp_players_list[player]['Soccer Experience']))
            except:
                break
        del other_players_list[:3]
        del exp_players_list[:3]
        print(player_list)


# make sure script can't be executed when imported
if __name__ == "__main__":
    distribute_players()
