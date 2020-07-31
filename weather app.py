import requests
from bs4 import BeautifulSoup

search = input("Enter the city name :\n")
url = f"https://www.google.com/search?&q=weather in + {search}"
r = requests.get(url)

s = BeautifulSoup(r.text, "html.parser")

update = s.find("div", class_="BNeawe").text
print(update)