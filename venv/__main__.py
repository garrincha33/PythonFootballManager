import generate


def main():
    print("Welcome to Py Director")
    print(" 1) Start Game")
    print(" 2) Load Game")
    while True:
        start_option = input(">")
        if start_option == "1":
            new_game()
            break
        elif start_option == "2":
            load_game()
            break
        elif start_option.lower() == "exit":
            break
        else:
            print("sorry please choose a valid option")


def new_game():
    global player
    global league

    print("congratulations on becoming manager what is your name?")
    name = input(">")
    print('%s, is that your name?' % name)
    confirm = input(">")
    if confirm.upper() == "Y":
        player = generate.Manager(name)
        league = generate.League()
        team_selection()
    elif confirm.upper() == "N":
        print("sorry lets try that again")
    elif confirm.lower() == 'exit':
        sys.exit()
    else:
        print("sorry name entered incorrectly make sure you enter Y or N")


def load_game():
    # TODO Load game function
    print('load game')


def team_selection():
    print("now which team would you like to go?")
    for n in range(10):
        print(str(n + 1) + ')' + league.team_list[n].get_name())

        while True:
            choice = input(">")
            my_team = league.team_list[int(choice) - 1]
            print("%s, is that your team? Y Or N?" % my_team.get_name())
            confirm = input('> ')
            if confirm.upper() == 'Y':
                print('Alright. You are the now the manager of %s' % my_team.get_name())
            my_team = generate.PlayerTeam(my_team.get_name(), my_team.prestige)
            league.team_list[int(
                choice) - 1] = my_team
            print(str(my_team.prestige))
            print('Here are your current players, and some information about them:')
            for x in range(len(my_team.player_list)):
                print('Name:'.ljust(25, ' ') + ' | ' + 'Position:'.ljust(10, ' ') + ' | ' + 'Rating:')
            break
    # elif confirm.upper() == 'N':
    #     print("Sorry! Let's try that again.")
    # else:
    #     print("I didn't catch that. Make sure you enter either a Y or an N.")


main()
