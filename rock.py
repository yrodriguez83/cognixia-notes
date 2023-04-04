#Student Exercise: Make Rock, Paper, Scissor Game

#function to get user input and validate result(MUST be r, p, or s)
def get_user_choice():
    #prompt user for input and make sure it is lowercase
    choice = input("Choose rock(r), paper(p), or scissors (s): ").lower()
    
    #validate input... Used a list ["r", "p", "s"] to validate the user's choice 
    # instead of checking each letter individually
    if choice in ["r", "p", "s"]:
        return choice
    else:
        #If the user's choice is invalid, display error message
        print("Please enter r, p, or s!")
        
#Get player 1 choice
user_choice1 = get_user_choice()
#player 2 choice
user_choice2 = get_user_choice()

def game(choice1, choice2):
    if choice1 == choice2:
        return "It's a tie!"
    elif choice1 == "r":
        if choice2 == "p":
            return "Player 2 won!"
        else:
            return "Player 1 won!"
            
    #if player 1 picks p
    elif choice1 == "p":
        if choice2 == "s":
            return "Player 2 won!"
        else:
            return "Player 1 won!"
        
    #if player picks s
    elif choice1 == "s":
        if choice2 == "r":
            return "Player 2 won!"
        else:
            return "Player 1 won!"
        
#print winner yass
result = game(user_choice1, user_choice2)
print(result)