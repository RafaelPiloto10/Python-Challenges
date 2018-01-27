
file = open("challenge.txt", mode="r")

characters = {}

for line in file:
    for letter in line:
        if letter not in characters:
            characters[str(letter)] = 0
        characters[str(letter)] += 1
for each in characters:
    print(each, characters[each])
