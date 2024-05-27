#Rock-Paper-Scissors Game
#User Input: Prompt the user to choose rock, paper, or scissors.
#Computer Selection: Generate a random choice (rock, paper, or scissors) for the computer.
#Game Logic: Determine the winner based on the user's choice and the computer's choice.Rock beats scissors, scissors beat paper, and paper beats rock.
#Display Result: Show the user's choice and the computer's choice.Display the result, whether the user wins, loses, or it's a tie.
#Score Tracking (Optional): Keep track of the user's and computer's scores for multiple rounds.
#Play Again: Ask the user if they want to play another round.
#User Interface: Design a user-friendly interface with clear instructions and feedback.

import random

selection = ["rock", "paper", "scissor"]
User_score = 0
computer_score = 0

def get_User_choice():
    """Get the player's choice"""
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ")
        if choice in selection:
            return choice
        else:
            print("Invalid choice! Please try again.")

def get_computer_choice():
    """Get the computer's random choice"""
    return random.choice(selection)

def determine_winner(User_choice, computer_choice):
    """Determine the winner based on the choices"""
    if User_choice == computer_choice:
        return "tie"
    elif (User_choice == "rock" and computer_choice == "scissor") or \
         (User_choice == "paper" and computer_choice == "rock") or \
         (User_choice == "scissor" and computer_choice == "paper"):
        return "User"
    else:
        return "computer"

def play_game():
    """Play a single round of the game"""
    global User_score, computer_score
    
    User_choice = get_User_choice()
    computer_choice = get_computer_choice()
    
    print(f"You chose: {User_choice}")
    print(f"Computer chose: {computer_choice}")
    
    winner = determine_winner(User_choice, computer_choice)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "player":
        print("You win!")
        User_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
    
    print(f"""Score: You score:{User_score} 
        computer score:{computer_score}""")

def new_func(computer_choice):
    print(f"computer chose: {computer_choice}")

def main():
    """Main function to run the game"""
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no):")
        if play_again != "yes":
            break
    
    print("Thanks for playing!")

if __name__ == "__main__":
    main()

