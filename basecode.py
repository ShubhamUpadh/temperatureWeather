import datetime as dt
import requests

baseUrl = "https://api.openweathermap.org/data/2.5/weather?"
apiKey = "appid=f248ae5e389d6870cc0b7dd267b92555"
city = "Delhi"

url = baseUrl + apiKey + "&q=" + city

response = requests.get(url).json()

# print(response)

print(str(response['main']['temp'] - 273.15)[0:5])
print(response['weather'][0]['description'])
