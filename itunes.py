import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()


responce = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

object = responce.json()

for result in object["results"]:
    print(result["trackName"])