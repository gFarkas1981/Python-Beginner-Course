# File Creating, Reading and Writing

file = open("fun.txt", "w")

file.write("Hello my name is Gabor\nThis is my new file!")

file = open("fun.txt", "r")

print(file.read())
