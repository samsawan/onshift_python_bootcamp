# Using the requests module
import requests

# Star Wars API - https://swapi.co/
api_url = 'https://swapi.co/api/'

# Make a get request to get starship 9
response = requests.get(api_url + 'starships/9')

# Store this data so that we can use it later
# and limit our callbacks to the API
starship9_data = response.json()

# Print the status code of the response.
print("response code from endpoint that exists: {}\n".format(response.status_code))

# File Not Found
# Note that the / before starships is intentional
response = requests.get(api_url + 'dne')
print("response code from endpoint that dne: {}\n".format(response.status_code))


# Set up the parameters we want to pass to the API.
# Get the Wookiee translation
parameters = {'format': 'wookiee'}

# Make a get request with the parameters.
response = requests.get(api_url + 'starships/9/', params=parameters)

# Print the content of the response (the data the server returned)
print("wookie format response: {}\n".format(response.content))

# This gets the same data as the command above
response = requests.get(api_url + 'starships/9/?format=wookiee')
print("another way to get wookie data: {}\n".format(response.content))

# What is starship 9?
print("startship9 name: {}\n".format(starship9_data['name']))
# Who is the manufacturer?
print("starship9 manufacturer: {}\n".format(starship9_data['manufacturer']))

# JSON representation of starship 9
print("all of the data associated with starship9: {}\n".format(starship9_data))
