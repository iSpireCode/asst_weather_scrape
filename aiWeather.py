
from bs4 import BeautifulSoup
import requests

url = "https://www.njweather.org/station/3411"

#class <div class="bigTemperature">

# "https://www.yahoo.com/news/weather/united-states/new-jersey/551-jersey-city-24701761/"
# "https://www.theweather.com/jersey-city-city.html"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
temp = doc.find("div", class_ ="bigTemperature").text



print(temp)

# temp = result.find_all("div", class_="temp-value")

# print(temp)

