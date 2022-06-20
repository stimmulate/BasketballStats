# import data
from constants import TEAMS, PLAYERS
import copy


def create_players(players):
    """
    Return a List of players.
    Iterate over the player list
    Convert height property to an integer
    Convert experience to a boolean
    Split guardian into a List of strings and use list comprehension to remove whitespace
    """
    for player in players:
        player["height"] = int(player["height"][0:2])

        if player["experience"] == "YES":
            player["experience"] = True
        else:
            player["experience"] = False

        guardians_split = player["guardians"].split("and")
        player["guardians"] = [guardian.strip(" ") for guardian in guardians_split]
    


    return players


# balance the number of players equally between teams
def balance_teams(players_list):
    """
    Balance the number of players equally between teams and then return teams.
    Create Lists for the different team stats
    Iterate over the players_list List to:
        Separate experienced and inexperienced players into separate Lists
    Iterate over the experienced List to divide players equally between teams
    Iterate over the inexperienced List to divide players equally between teams
    """
    # creates global variables for teams so they can be accessed in the menu function
    global panthers, bandits, warriors
    experienced = []
    inexperienced = []
    panthers = []
    bandits = []
    warriors = []

    for player in players_list:
        if player["experience"] == True:
            experienced.append(player)
        else:
            inexperienced.append(player)

    for num, player in enumerate(experienced, start = 1):
        if num % 3 == 0:
            panthers.append(player)
        elif num % 2 == 0:
            bandits.append(player)
        else:
            warriors.append(player)

    for num, player in enumerate(inexperienced, start = 1):
        if num % 3 == 0:
            panthers.append(player)
        elif num % 2 == 0:
            bandits.append(player)
        else:
            warriors.append(player)

    return panthers, bandits, warriors


# displays team stats
def display_stats(team, players):
    """
    Print out the various team stats.
    Iterate over the players list to:
        Calculate the number of experienced players on the team
        Calculate the number of inexperienced players on the team
        Calculate the sum of the player's height
        Append the player's name to a List
        Append the player's guardians to a List
    Use list comprehension to create a string of player names
    Use nested list comprehension to create a string of guardian names
    Print team name, number of players, number of experienced/inexperienced players, average height, player names, and guardian names
    """
    exp_players = 0
    inexp_players = 0
    height = 0
    names_list = []
    guardians_list = []

    """
    Sort players by height, found article for sorting list with dictionary values @

    https://note.nkmk.me/en/python-dict-list-sort/#:~:text=In%20Python%2C%20sorting%20a%20list,value%20of%20the%20specific%20key. 
    """
    players = sorted(players, key=lambda x: x['height'])

    for player in players:
        if player["experience"] is True:
            exp_players += 1
        elif player["experience"] is False:
            inexp_players += 1

        height += player["height"]
        names_list.append(player["name"])
        guardians_list.append(player["guardians"])

    names = ", ".join([str(name) for name in names_list])
    guardians = ", ".join([str(guardian) for sublist in guardians_list for guardian in sublist])

    print("\nDisplaying stats for the {}.\n".format(team))
    print("There are {} players on the team,".format(len(players)))
    print("{} experienced players and {} inexperienced.".format(exp_players, inexp_players))
    print("The average player height is {} inches.\n".format(height / len(players)))
    print("Players (sorted by height):", names, "\n")
    print("Guardians:", guardians, "\n")


def menu(TEAMS, players_list):
    """
    Prompt the user for input and display stats for the selected team.
    Take input from user
    Display stats for selected team
    Raise and handle exception if they enter something outside of the expected responseds
    Reprompt user to select another team until they chose to quit the program
    """
    create_players(players_list)
    balance_teams(players_list)

    print("\nWelcome to the BasketBall Stats Tool!")
    
    while True:
        print("""
            Type "1" to see stats for the Panthers.
            Type "2" to see stats for the Bandits.
            Type "3" to see stats for the Warriors.
            Enter "Q" to exit the program.
        """)

        try:
            response = input("> ")

            if response == "1":
                display_stats(TEAMS[0], panthers)
                continue
            elif response == "2":
                display_stats(TEAMS[1], bandits)
                continue
            elif response == "3":
                display_stats(TEAMS[2], warriors)
                continue
            elif response.lower() == "q":
                print("Have a great day!")
                break
            else:
                raise ValueError()
        except ValueError as err:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    # run initial function
    menu(TEAMS, copy.deepcopy(PLAYERS))