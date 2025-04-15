import pyfiglet

text = "Welcome!"
text=pyfiglet.print_figlet(text="Welcome to Kira's game!",
                           colors='Red')
import random

def number_guessing_game():
    number_to_guess = random.randint(1,50)
    max_attempts = 5
    attempts = 0

    print("Welcome to Kira's number guessing game!")
    print("Kira is thinking of a number between 1 - 50.")
    print(f"Broda,you have {max_attempts} attempts to guess it!")
    while True:
            guess_int = input("Take a guess broda!")
            if guess_int.isdigit():
                guess = int(guess_int)
                attempts += 1
                attempts_left = max_attempts - attempts
                if guess < number_to_guess:
                 print("Too low,don't be scared! You have {attempts_left}!")
                elif guess > number_to_guess:
                  print("Too high man!")
                else:
                 print(f"Congraats! You guessed it in {attempts} attempts! Holy ****! sorry...You are so good!")
                 break
