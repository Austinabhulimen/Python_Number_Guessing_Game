#Guessing Game
import random
from number_game_logo import logo
print(logo)


print("Welcome to the Number Guessing Game!\n"
      " I am thinking of a number between 1 and 50.")
difficulty = (input("Choose a difficulty. Type 'easy' or 'hard': ").lower())

number = int(random.choice(range(1,51)))


if difficulty == 'hard':
    attempt = int(5)
elif difficulty == 'easy':
    attempt = int(10)
else: print('please input valid response as requested')


while attempt >=1:

    guess= int((input(f"You have {attempt} remaining to guess the number. \nMake a guess: ")).lower())
    if guess == number:
        print(f"You guessed right {guess}, is the {number}........YOU WON")
        break;
    elif guess > number:
        print("Number too high.\n Guess again.")
        attempt -=1

    elif guess < number:
        print("guess too low.\n Guess again.")
        attempt -=1

if attempt == 0:
    print('You have run out of guesses, you lose')