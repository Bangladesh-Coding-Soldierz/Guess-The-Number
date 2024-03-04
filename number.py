import random

def guess_the_number():
    number_to_guess = random.randint(1, 100) # The computer selects a random number between 1 and 100
    attempts = 0

    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        attempts += 1
        try:
            player_guess = int(input("Make your guess: ")) # The player inputs their guess
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if player_guess < 1 or player_guess > 100:
            print("Your guess is out of bounds. Please guess a number between 1 and 100.")
        elif player_guess < number_to_guess:
            print("Too low. Try again.")
        elif player_guess > number_to_guess:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break # This exits the loop when the player guesses the number correctly

if __name__ == "__main__":
    guess_the_number()
