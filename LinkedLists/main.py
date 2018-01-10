#Used to make requests
import urllib.request
import re
y = 16044 / 2

while True:
    #print(i)
    pasty = y
    x = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(y))
    content = x.read()
    expre = re.compile(r"next nothing is 63579 \d")
    nothing = re.findall(expre, str(content))
    tempString = ""
    for i in nothing:
        tempString += i
    answer = re.findall("\d", tempString)
    
    y =("".join(nothing))
    print(y)
##    if x.getcode() == 200 and "and the next" not in x.read():
##        print(y)
##        break

