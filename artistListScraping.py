# Http
import requests

# Scrape data from an HTML document
from bs4 import BeautifulSoup

# Files
import os

# Search and manipulate strings
import re


class artistListScraping():

    def __init__(self, url):
        self.artistList = list()
        self.url = url

    def removeCountries(self, countries, lyrics):
        for country in countries:
            lyrics = str(lyrics).replace(country, "")
        return lyrics

    def cleanList(self, lista):
        for i in range(0, len(lista)):
            lista[i] = re.sub(r'[ ]{2}', "", lista[i])
        return lista

    def scrape_list(self):
        page = requests.get(self.url)
        html = BeautifulSoup(page.text, 'html.parser')
        lyrics = html.find("table").get_text()
        # remove identifiers like chorus, verse, etc
        lyrics = re.sub(r'[\s]', ' ', lyrics)
        countries = ["Estados Unidos", "Reino Unido", "Canadá",
                     "Australia", "Irlanda", "Jamaica", "México"]
        #lyrics = self.remove_punctuation(lyrics)
        # remove empty lines
        lyrics = self.removeCountries(countries, lyrics)
        lyrics = re.sub(r'[\d]', "", lyrics)
        #lyrics = re.sub(r'[ ]{3,}', "", lyrics)

        listaFinal = lyrics.split("     ")
        listaFinal.pop(0)
        listaFinal = self.cleanList(listaFinal)
        return listaFinal
