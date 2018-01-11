#Used to make requests
# Answer is http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=66831

import urllib.request
import re

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' # Python challenges website
nextNothing = 16044 / 2 # Start at this value for faster answer could also start at 12345
stringPattern = r'next nothing is \d*' # Re expression for the string 'next nothing  <int>
numberPattern = r'\d+' # Re expression for just the integer value

def getNextNothing(pattern, string):
    # Easy function for finding and returning the match
    return re.search(pattern, string)

while True:
    # Iterate through the websites
    
    x = urllib.request.urlopen(url + str(nextNothing)) # Open Html page
    content = x.read() # Read html page

    nextNothingString = getNextNothing(stringPattern, str(content)) # Get next nothing string
    string = nextNothingString.group() # turn the group into a string

    nextNothingInt = getNextNothing(numberPattern, string) # Get next nothing int
    nextNothing = nextNothingInt.group() # Set the next y to be the next nothing
    print(nextNothing) # Print the nextNothing



