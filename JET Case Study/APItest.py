import requests
import json

comics = requests.get(url = "https://xkcd.com/info.0.json", timeout=100)

print(comics.json())

