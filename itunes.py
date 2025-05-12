import json
import requests
import sys

def main():

    if len(sys.argv) != 2:
        sys.exit()

    response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

    print(response)
    res = response.json()

    for result in res["results"]:
        print(result["trackName"])

if __name__ == "__main__":
    main()
