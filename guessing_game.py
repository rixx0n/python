## Pick a secret word :D
secret_word = "rat"
guess = ""
guess_count = 0
guess_remaining = 3
out_of_guesses = False

print("Welcome to RAT_GOD Guessing Game! Step up, if the price is right boi.")
print("Made by rixx0n")

while guess != secret_word and out_of_guesses != True:
    if guess_remaining != 0:
        print("You have " + str(guess_remaining) + " guesses remaining.")
        guess = input("Enter guess: ")
        guess_count += 1
        guess_remaining -= 1
    else:
        out_of_guesses = True

## Break out of above while loop implies out of guess = True
## This is why we do not specify true for the lower if statement.

if out_of_guesses:
    print("Zero guesses remaining, YOU LOSE LOL!")
else:
    print("You win! RAT_GOD dey all applaud.")