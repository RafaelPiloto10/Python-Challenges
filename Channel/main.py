# Source : 'http://www.pythonchallenge.com/pc/def/channel.html'
import urllib.request

url = 'http://www.pythonchallenge.com/pc/def/channel.html'
content = urllib.request.urlopen(url)

for a, b in zip(' now there are pairs', content):
    print(a, b)
