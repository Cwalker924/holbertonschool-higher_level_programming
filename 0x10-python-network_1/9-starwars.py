#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    arg1 = sys.argv[1]
    url = "https://swapi.co/api/people/?search=" + arg1
    req = requests.get(url)
    data = req.json()["results"]
    print("Number of result: {}".format(len(data)))
    for res in data:
        print(res["name"])
