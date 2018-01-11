# source: http://www.pythonchallenge.com/pc/def/banner.p
# Answer is channel

import pickle # Import pickle for the urllib.request.open that is going to happen
import urllib.request # open page source 

url = 'http://www.pythonchallenge.com/pc/def/banner.p' # Set the url
data = urllib.request.urlopen(url) # Open the page

data = pickle.load(data) # load the data with pickle

for i in data: # Iterate over the elements
    for j in i: # iterate over the next elements
       for k in range(j[1]): # Print the character 'x', 'y' times (x, y)
           print(j[0], end='') # Print
# Add a new line for comfort when reading / scrolling
print("\n")
    
