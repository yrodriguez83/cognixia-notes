import random


# define a function to get the user's choice of rock, paper, or scissors
def get_user_choice():
    # prompt the user to enter their choice
    choice = input("Choose rock(r), paper(p), or scissors(s): ").lower()

    # validate the input to make sure it's one of the allowed values
    # if it's not allowed, print an error message and prompt the user again
    while choice not in ["r", "p", "s"]:
        print("Please enter r, p, or s!")
        choice = input("Choose rock(r), paper(p), or scissors(s): ").lower()

    # return the validated choice
    return choice

# define a function to determine the winner of a single game of rock, paper, scissors


def game(choice1, choice2):
    # if both players choose the same thing, it's a tie
    if choice1 == choice2:
        return "It's a tie!"
    # if player 1 chooses rock and player 2 chooses paper, player 2 wins
    elif choice1 == "r":
        if choice2 == "p":
            return "Player 2 won!"
        else:
            return "Player 1 won!"
    # if player 1 chooses paper and player 2 chooses scissors, player 2 wins
    elif choice1 == "p":
        if choice2 == "s":
            return "Player 2 won!"
        else:
            return "Player 1 won!"
    # if player 1 chooses scissors and player 2 chooses rock, player 2 wins
    elif choice1 == "s":
        if choice2 == "r":
            return "Player 2 won!"
        else:
            return "Player 1 won!"

# define a function to ask the user if they want to play again


def play_again():
    # prompt the user to enter y or n to indicate whether they want to play again
    choice = input("Do you want to play again? (y/n)").lower()

    # if the user enters an invalid value, print an error message and prompt them again
    while choice not in ["y", "n"]:
        print("Please enter y or n!")
        choice = input("Do you want to play again? (y/n)").lower()

    # return True if the user wants to play again, False otherwise
    return choice == "y"

# define a function to play a single game of rock, paper, scissors


def play_game():
    # prompt the user to choose the number of games to play (best of 3 or best of 5)
    num_games = int(
        input("Do you want to play a best of 3 or best of 5 series? (3/5): "))

    # initialize counters for the number of wins for each player and draws
    p1_wins = 0
    p2_wins = 0
    draws = 0

    # loop through each game
    for i in range(num_games):
        # prompt the user to enter their choice for player 1
        print("Game {}".format(i+1))
        user_choice1 = get_user_choice()

        # prompt the user to choose whether they want to play against the computer or another human
        # if they choose to play against the computer, generate a random choice for player 2
        choice_type = input(
            "Do you want to play against a computer? (y/n)").lower()
        if choice_type == "y":
            user_choice2 = random.choice(["r", "p", "s"])
        elif choice_type == "n":
            user_choice2 = get_user_choice()
        else:
            print("Please enter y or n!")
            user_choice2 = get_user_choice()

        # determine the winner of the game and increment the appropriate counter
        result = game(user_choice1, user_choice2)
        if result == "Player 1 won!":
            p1_wins += 1
        elif result == "Player 2 won!":
            p2_wins += 1
        else:
            draws += 1

        # print the result of the game
        print(result)

    # print the final score
    print("Final score: ")
    print("Player 1: {} wins".format(p1_wins))
    print("Player 2: {} wins".format(p2_wins))
    print("Draws: {}".format(draws))

    # ask the user if they want to play again
    if play_again():
        play_game()
    else:
      # ask the user if they want to quit or play again
      choice = input("Do you want to quit? (y/n)").lower()
      if choice == "y":
          return


# call the function and start game
play_game()

        