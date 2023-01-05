from bs4 import BeautifulSoup
import requests
import lxml
import asyncio
from datetime import datetime


def getValue():
    try:
        site_url = "https://www.shining-moon.com/"

        page = requests.get(site_url)
        soup = BeautifulSoup(page.text, 'lxml')

        getCount = soup.find('span')
        print(getCount, 'Text:', getCount.text)

        return int(getCount.text.replace(',', ''))
    except ValueError as exception:
        print(f'Error: {exception}')
        pass


def getDate():
    now = datetime.now()

    return now.strftime("%d-%m-%Y %H:%M:%S")
