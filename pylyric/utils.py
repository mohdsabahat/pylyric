import requests
from bs4 import BeautifulSoup


def get(url):

    resp = requests.get(url)
    return resp

def soupify(page):

    return BeautifulSoup(page.content, 'html.parser')
