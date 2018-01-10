import re
file = open("Challenge.txt", mode='r')

check = re.compile(r"[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]")
bodygaurds = []
for line in file:
    bodygaurds += re.findall(check, line)
only = ""
for gaurds in bodygaurds:
    only += gaurds[1:len(gaurds) -1]

small = re.compile(r"[a-z]")
smLetters = re.findall(small, only)

print(smLetters)
