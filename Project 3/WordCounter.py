import operator
import sys

# open the argument filename after WordCounter.py
# WordCounter.py lincoln.txt
file = open(sys.argv[1], "r")

# Read in file
text = file.read()
text = text.replace("—", "")
text = text.replace(".", "")
text = text.replace(",", "")
file.close()

# Count the words

words = {}

for word in text.split():
    if word.lower() in words:
        words[word.lower()] += 1
    else:
        words[word.lower()] = 1

sortedwords = sorted(words.items(), key = operator.itemgetter(1), reverse=True)

print(sortedwords)

# Write the counted words into a new file
# original filename-4char + "-count" + ".txt"
file = open(sys.argv[1][:-4] + "-count" + sys.argv[1][-4:], "w")

file.write("Total words - {}\nUnique words - {}\n\n".format(len(text.split()), len(sortedwords)))

for wordinfo in sortedwords:
    file.write("{} - {}\n".format(wordinfo[0], wordinfo[1]))

file.close()
