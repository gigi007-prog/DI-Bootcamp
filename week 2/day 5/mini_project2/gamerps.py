import random

# The game's rules determine the winner: rock crushes scissors, scissors cut paper, and paper covers rock.
# Mathematically, rock-paper-scissors is actually quite simple. All three options are
# completely equal – they all win, lose, and draw against one of the other signs. Because of
# this, there is no reason to favor one sign over the others, and the mathematically optimal

class Game:
    def __init__(self):
        self.items = ['rock', 'paper', 'scissors']

    def get_user_item(self):
        while True:
            user_choice = input("Enter rock, paper, or scissors: ").lower()
            if user_choice in self.items:
                return user_choice
            else:
                print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

    def get_computer_item(self):
        return random.choice(self.items)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == 'rock' and computer_item == 'scissors') or \
             (user_item == 'paper' and computer_item == 'rock') or \
             (user_item == 'scissors' and computer_item == 'paper'):
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"You selected {user_item}. The computer selected {computer_item}.")
        if result == "win":
            print("Great Choice, You win!")
        elif result == "draw":
            print("It's a draw!")
        else:
            print("Sorry, You lose!")

        return result 