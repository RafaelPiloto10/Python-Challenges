# Source : 'http://www.pythonchallenge.com/pc/def/channel.html'
# I did not solve this. I was absolutely stumpped by the challenge and
# could no longer help my self. I looked it up and found this solution.
# I did not know that www.url.zip existed as well as the zipfile module
# I am glad that I looked it up because not only would I have been stuck
# On this for ages but I know I have learned how it works
# Solution used : https://the-python-challenge-solutions.hackingnote.com/level-6.html

import zipfile, re # Imports

f = zipfile.ZipFile("zipSource/channel.zip") # Zip files
start = "90052" # Readme.txt hints to start at this number
comments = [] # later hinted to keep track of comments

while True: # Iterate over files
	content = f.read(start + ".txt").decode("utf-8") # read file
	comments.append(f.getinfo(start + ".txt").comment.decode("utf-8")) # Get comments
	print(content) # Print number
	match = re.search("Next nothing is (\d+)", content) # Get number
	if match == None: # If there are no more numbers
		break # End loop
	start = match.group(1) # Otherwise continue the loop with the match

print("".join(comments)) # At the end print the comments
