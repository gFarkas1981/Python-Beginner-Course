# While loops

age = 38

while age < 100:
    print(age)
    age += 1

steps = 1
secretNumber = '8'

guess = input("Guess a number between 1 and 10!\n")

while guess != secretNumber:
    steps += 1
    if int(guess) < int(secretNumber):
        guess = input("Enter a bigger number!\n")
    else:
        guess = input("Enter a smaller number!\n")

print("You win in " + str(steps) + " step's'")
