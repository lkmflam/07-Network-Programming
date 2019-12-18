#Create a Python script to get the number of people visiting a U.S. government website right now. using this information-> Source: https://analytics.usa.gov/data/live/realtime.json

#https://bit.ly/2lVhlLX
# via: https://analytics.usa.gov/
import requests
url = 'https://analytics.usa.gov/data/live/realtime.json'
j = requests.get(url).json() #States it is a json file
print("Number of people visiting a U.S. government website-")
print("Active Users Right Now:")
print(j['data'][0]['active_visitors']) #Pulls and prints the information from the JSON file
