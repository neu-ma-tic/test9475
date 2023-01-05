import requests


def FloorPrice(url):

    querystring = {"offset":"0","limit":"300"}

    response = requests.request("GET", url, params=querystring)

    response = response.json()

    floorPrice = response["collection"]["stats"]["floor_price"]

    return floorPrice