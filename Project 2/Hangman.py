# Hangman

import time

lives = 5
stringword = "Apple"
word = list(stringword.lower())
guess = ["_"] * len(word)
winner = False
incorrectletters = []

def printscore():
    global guess
    print("Lives: " + str(lives))
    print("Incorrect letters: ", end="")
    for i in range(len(incorrectletters)):
        if i == len(incorrectletters) - 1:
            print(incorrectletters[i])
        else:
            print(incorrectletters[i] , end=", ")
    print("")
    for i in range(len(guess)):
        if i == len(guess) - 1:
            print(guess[i])
        else:
            print(guess[i] , end=", ")
    print("")


def askforletter():
    global guess
    global word
    letterguess = input("Please guess a letter!\n").lower()
    correct = False
    for x in range(len(word)):
        if letterguess == word[x]:
            guess[x] = letterguess
            correct = True
    if correct:
        print("You got one!")
    else:
        print("oh no! That wasn't in there.")
        incorrectletters.append(letterguess)
        global lives
        lives -= 1
    time.sleep(1)

def checkwinner():
    if "_" not in guess:
        global winner
        winner = True


while lives > 0 and not winner:
    # Print out the current scoreboard
    printscore()
    # Ask the user for a letter
    askforletter()
    # Check if they won
    checkwinner()

if lives <= 0:
    print("You lost! The word was " + str(word))
else:
    print("Congratulations! You won with " + str(lives) + " lives left!")
