# Letter Grade Bot

pointsPossible = 37
score = (int(input("What is your score?\n")))
studentName = "Gabor"

'''
A - 100 - 90%
B - 89 - 80%
C - 79 - 70%
D - 69 - 60%
F - 59 - 0%
'''

age = input("What's your age?\n")
print("You are " + age + " years old.")

print("Student name: " + studentName)
percent = 100 / (pointsPossible / score)
print(percent)

if (100 >= percent >= 90):
    print(studentName +" got grade A")
elif (89 >= percent >= 80):
    print(studentName +" got grade B")
elif (79 >= percent >= 70):
    print(studentName +" got grade C")
elif (69 >= percent >= 60):
    print(studentName +" got grade D")
elif (59 >= percent >= 0):
    print(studentName +" got grade F")

