import requests

# Making a GET request to a public API
response = requests.get('https://official-joke-api.appspot.com/random_joke') 
#Useyour own Api Data For This
data = response.json()

print(data)
