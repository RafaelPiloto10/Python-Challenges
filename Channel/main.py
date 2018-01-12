# Source : 'http://www.pythonchallenge.com/pc/def/channel.html'
import zipfile, re

f = zipfile.ZipFile("zipSource/channel.zip")
start = "90052"
comments = []

while True:
	content = f.read(start + ".txt").decode("utf-8")
	comments.append(f.getinfo(start + ".txt").comment.decode("utf-8"))
	print(content)
	match = re.search("Next nothing is (\d+)", content)
	if match == None:
		break
	start = match.group(1)

print("".join(comments))
