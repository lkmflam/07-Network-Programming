#Write a Python program to extract h1 tags from example.com

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

link = urlopen("http://example.com")
reading = BeautifulSoup(link.read(), "html.parser")

print(reading.h1)
