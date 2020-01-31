# While loops

number = 0
counter = 1

while number < 1_000_000_000:
    counter += 1
    number = 2 ** counter


print(counter)
