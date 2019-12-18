#Create a Python script to verify if any given webpage exists or not on the server

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
	site = urlopen("https://google.com")
except HTTPError as e:
	print("HTTP Error found")
except URLError as e:
	print("URL Error")
else:
	print(site.read())

