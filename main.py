import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    print("Welcome to the Number Guessing Game!")
    print("Guess number  between 1 and 100. Try to guess it!")

    while not guessed:
        # User input
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check if the guess is correct, too high, or too low
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number correctly in {attempts} attempts.")
                guessed = True

            print(f"You've {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")

# Start the game
if __name__ == "__main__":
    user_name = input("Enter your name")
    while True :
        play_again = input(f"{user_name} Do you want to play Game\n Press y for yes or n for no")
        if play_again == 'y':
            guessing_game()
        else:
            break


    
