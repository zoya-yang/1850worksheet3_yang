import random

def guessing_game():
    secret_number = random.randint(1, 100)

    max_guesses = 10
    guesses = [ ]
    print("Welcome to the Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_guesses} attempts to guess the number.")
    for attempt in range(max_guesses):
        guess = input(f"Attempt {attempt to guess the number.}")

    for attempt in range(max_guesses):
        guess = input(f"Attempt {attempt + 1}: Enter your guess: ")

        try:
            guess = int(guess)
            if guess < 1 or guess > 100:
                print("Invalid input. Please enter a number between 1 and 100.")
                continue
        except ValueError:
            print("Incalid input. Please enter a number.")
            continue
        guesses.append(guess)

        if guess < secret_number:
            print("The secret number is higher than your guess. Guess again.")
        elif guess > secret_number:
            print("The secret number is lower than your guess. Guess again.")
        else:
            print("You have guessed the secret number! Well done.")
            break
    else:
        print(f"You could not guess the secret number in {max_guesses} tries. Unlucky! The number was {secret_number}.")

    print("Your guesses were:", guesses)

guessing_game()