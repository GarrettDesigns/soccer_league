import csv

# Define list of team names
teams = {'Raptors': [], 'Sharks': [], 'Dragons': []}

# Define function to read in the roster of players
def get_roster():
    with open('soccer_players.csv') as file:
        read_roster = csv.DictReader(file)
        roster = list(read_roster)
    return roster

# define function to filter player types into a separate lists
def distribute_players():
    # read roster in
    roster = get_roster()

    # define empty lists to hold players
    exp_players_list = []
    other_players = []

    # sort through list of players, divide into playes with and witout experience
    for player in roster:
        if player['Soccer Experience'] == "YES":
            exp_players_list.append(player)
        else:
            other_players.append(player)
    return exp_players_list, other_players

# Define function to distribute players by type evenly among teams
def create_teams():
    # get list of players by type
    exp_players_list, other_players_list = distribute_players()

    # calculate the max number of players of each type per team
    max_player_type = int(len(exp_players_list)/len(teams))

    # For each team
    for player_list in teams.values():
        # Add players of each type up to the max type per team
        for player in range(max_player_type):
            # Add non-experienced players
            player_list.append([other_players_list[player]['Name'], other_players_list[player]['Soccer Experience'], other_players_list[player]['Guardian Name(s)']])

            # Add experienced players
            player_list.append([exp_players_list[player]['Name'], exp_players_list[player]['Soccer Experience'], exp_players_list[player]['Guardian Name(s)']])

        # Remove already added chunk of player types
        del other_players_list[:max_player_type]
        del exp_players_list[:max_player_type]

# Define function to generate a file container a list of teams and players information
def generate_teams_list():
    # Open file to write team
    with open('teams.txt', 'w') as file:
        for team_name, roster in teams.items():
            # Loop through teams and write each team name to file
            file.write('\n' + team_name + '\n')
            # Loop through team roster and write players to appropriate teams
            for player in roster:
                file.write('{}, {}, {}'.format(player[0], player[1], player[2]) + '\n')

# Define function to generate welcome letters to all player's guardians
def generate_welcome_letter():
    # Loop through teams and grab team name
    for team_name, roster in teams.items():
        team = team_name

        # Loop though each team roster
        for player in roster:
            # Create file name from player name
            file_name = '_'.join(player[0].split())

            # Open file to write letters
            with open(file_name + '.txt', 'w') as letter:
                player_name = player[0]
                guardian = player[2]

                # Generate letter for each player 
                letter.write("Dear " + guardian + ",\n")
                letter.write("\nWe are writing to welcome {0} to the {1}, we are so glad to have you both!\nYour first practice will take place at the {1}'s home field on Monday December 5th at 5:00pm".format(player_name, team))

# make sure script can't be executed when imported
if __name__ == "__main__":
    create_teams()
    generate_teams_list()
    generate_welcome_letter()
