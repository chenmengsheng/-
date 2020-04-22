from urllib.request import urlopen
import json
from pprint import pprint
myURL='http://www.ahstu.edu.cn'
with open("ahstu.html","w") as outFile:
    for line in  urlopen(myURL).readlines():  # get all content on url page
        outFile.write(line.encode().decode('unicode_escape'))

