import datetime as dt
import requests

baseUrl = "https://api.openweathermap.org/data/2.5/weather?"
apikey = open('apikey.txt', 'r').read()

print(type(apikey))
city = "Melbourne,AU"

url = baseUrl + "appid=" + apikey + "&q=" + city

response = requests.get(url).json()

print(response)
'''
print(str(response['main']['temp'] - 273.15)[0:5])
print(response['weather'][0]['description'])
'''