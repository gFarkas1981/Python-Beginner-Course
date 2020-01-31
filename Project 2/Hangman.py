words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]
cooldictionary = {}
for i in range(len(words)):
    cooldictionary[words[i]] = definitions[i]

for word in cooldictionary.keys():
    print(word)

for item in cooldictionary.items():
    print(item)

del(cooldictionary['PoGo'])


dabools = [False, False, False, False, True, False, True, False, True, False, False, False, False, False, True, False, True, True, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, True, True, False, False, True, True, True, True, True, False, True, True, False, True, False, False, True, False, False, False, False, True, True, False, False, True, True, True, False, True, True, False, False, False, False, True, True, False, True, True, False, True, True, True, False, False, False, True, True, False, True, False, True, False, True, True, True, False, True, False, False, True, True, False, True, False, False, True, False, True, False, True, False, True, True, True, True, False, False, True, True, False, False, False, False, True, True, True, False, False, True, True, True, True, True, False, True, True, False, False, True, True, False, False, True, True, True, True, True, False, False, True, True, False, False, True, True, False, False, False, False, False, True, True, True, True, True, False, True, True, False, False, True, True, True, True, True, False, False, True, True, True, True, True, False, True, True, True, True, True, False, False, True, False, False, False, True, True, True, False, True, False, False, True, False, False, True, True, False, False, False, False, True, False, False, True, True, False, True, True, False, False, True, False, True, True, False, True, False, True, False, True, False, False, True, False, True, False, False, False, True, True, False, False, False, True, True, False, False, True, True, True, True, True, False, True, True, True, True, False, False, True, False, True, True, True, True, True, False, False, False, True, True, False, True, True, True, False, False, True, True, False, True, True, True, True, False, True, True, False, False, False, True, True, True, True, True, False, False, False, True, False, False, False, True, False, True, True, True, True, False, False, False, True, False, False, False, False, True, True, False, True, False, False, True, False, False, False, True, True, True, False, False, True, True, False, False, True, True, False, False, True, False, True, False, True, True, True, False, True, True, True, True, False, True, True, False, True, True, False, True, False, True, False, True, True, False, True, False, True, False, False, True, True, False, True, False, False, True, True, True, False, True, True, True, False, False, False, True, False, True, True, False, True, False, True, True, False, True, True, False, False, True, False, False, False, True, True, False, True, True, False, False, True, True, True, False, False, True, False, True, True, True, True, False, False, True, True, False, False, True, True, False, True, False, True, True, True, True, True, False, False, False, True, False, False, True, False, False, True, True, False, False, False, False, False, False, True, False, True, False, False, True, True, False, True, True, True, False, True, True, False, False, True, False, False, True, True, False, True, False, True, False, False, True, False, True, True, False, False, True, True, False, False, True, False, False, False, False, True, False]

count = {True : 0, False : 0}

for i in range(len(dabools)):
    if dabools[i] == True:
        count[True] += 1
    else:
        count[False] += 1

print(count[True])
print(count[False])
