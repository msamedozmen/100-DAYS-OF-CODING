import random
print("Welcome to Guessing Number Game")

print("I'm thinking of a number between 1 to 100")
guessing_number = random.randint(1,100)
print(guessing_number)
difficulty = input("Chose a difficulty : Type 'easy' or 'hard'").lower()

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts =5
else:
    print("You typed wrong please try again")
    quit
    
def guessing_number_game(number,dif_lvl):
    while True:
        while dif_lvl>0:
            player_guess = int(input(f"You have a {dif_lvl} attempts remaining to guess a number.\nMake a guess: "))
            if player_guess > number:
                dif_lvl= dif_lvl-1
                if dif_lvl ==0:
                    print("Too high.\nYou've run out of guess. You lost")
                else:
                    print("Too High.\nGuess again.")
            elif player_guess< number:
                dif_lvl = dif_lvl-1
                if dif_lvl ==0:
                    print("Too low.\nYou've run out of guess. You lost")
                else:
                    print("Too low.\nGuess again.")
            else:
                print("You did correct guess you win")
                dif_lvl =0
        if dif_lvl ==0:
            return False

guessing_number_game(guessing_number,attempts)