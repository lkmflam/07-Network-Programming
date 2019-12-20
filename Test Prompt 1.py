import requests
import urllib
from urllib.request import urlopen
import json
count = 0
sum = 0
sumcount = 0
link = "http://py4e-data.dr-chuck.net/comments_57128.json"
opening = urlopen(link)
data = opening.read()
#j = requests.get(link).json()
#print(j)
parsing = json.loads(data)
for x in parsing["comments"]:
    num = int(x["count"])
    count = count + 1
z = parsing['comments'][sumcount]
#print(z["count"])
while sumcount < 51:
   number = z["count"]
   sum = sum + number
   sumcount = sumcount + 1
#print(data)
print("Comment Count: ", count)
print("The sum of the numbers in the file is: ", sum)
