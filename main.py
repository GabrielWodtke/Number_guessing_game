import random

difficult = {"easy": 10 , "medium": 5, "hard": 3}#defines the number of lives

print("Welcome to the number guessing game!\nI am thinking of a number between 1 to 100")
print("Please select a difficulty level: \nEasy\nMedium\nHard")
difficulty = input("\nType your choice:")
print(f"You have selected the {difficulty} level! Good luck.")

number_of_lives = difficult[difficulty.lower()]
number = random.randint(1, 100)

game_running = True


def game(correct_number, lives):
    global game_running, number_of_lives
    try:
        guessed_number = int(input("Please enter your guess:"))
        if guessed_number < 1 or guessed_number > 100:
            print("invalid number, please enter a number between 1 to 100!")
            game(correct_number, lives)
        elif guessed_number == correct_number:
            print(f"Congratulations! The Number is {guessed_number}, you win!")
            game_running = False
            return game_running
        else:
            lives -= 1
            higher_or_lower = "higher" if guessed_number < correct_number else "lower"
            print(f"Incorrect number! the number is {higher_or_lower} than {guessed_number}. "
                  f"\nnumber of chances:{lives}")
            number_of_lives = lives
            if lives == 0:
                print("You ran out of lives. You have lost")
                game_running = False
                return game_running
            return lives
    except ValueError:
        print("Invalid input! please enter a valid integer.")


while game_running:
    game(number, number_of_lives)
