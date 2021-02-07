# Http
import requests

# Scrape data from an HTML document
from bs4 import BeautifulSoup

# Files
import os

# Search and manipulate strings
import re

# Class that will scrap and create the dataset


class geniusScraping():

    def __init__(self, artist=None, pathDataset="./lyrics"):
        self.token = '7XFgPELzsHlp6CtJZv1gaqwNfqDhzx6838_-Ttwq6gGiNDKd6rU6f9S1MBNvItOz'
        self.artistList = artist
        self.pathDataset = pathDataset

    # Get artist object from Genius API
    def request_artist_info(self, artist_name, page):
        base_url = 'https://api.genius.com'
        headers = {'Authorization': 'Bearer ' + self.token}
        search_url = base_url + '/search?per_page=10&page=' + str(page)
        data = {'q': artist_name}
        response = requests.get(search_url, data=data, headers=headers)
        return response

    # Get Genius.com song url's from artist object

    def request_song_url(self, artist_name, song_cap):
        page = 1
        songs = []

        while True:
            response = self.request_artist_info(artist_name, page)
            json = response.json()
            # Collect up to song_cap song objects from artist
            song_info = []
            for hit in json['response']['hits']:
                if artist_name.lower() in hit['result']['primary_artist']['name'].lower():
                    song_info.append(hit)

            # Collect song URL's from song objects
            for song in song_info:
                if (len(songs) < song_cap):
                    url = song['result']['url']
                    songs.append(url)

            if (len(songs) == song_cap):
                break
            else:
                page += 1

        print('Found {} songs by {}'.format(len(songs), artist_name))
        return songs

    def remove_punctuation(self, lyrics):
        return re.sub(r'[^\w\s]', '', lyrics)

    def scrape_song_lyrics(self, url):
        lyrics = "Produced by"
        while lyrics == "Produced by":
            page = requests.get(url)
            html = BeautifulSoup(page.text, 'html.parser')
            lyrics = html.find('p').get_text()
            # remove identifiers like chorus, verse, etc
            lyrics = re.sub(r'[\(\[].*?[\)\]]', '', lyrics)
            lyrics = self.remove_punctuation(lyrics)
            # remove empty lines
            lyrics = os.linesep.join([s for s in lyrics.splitlines() if s])
        return lyrics

    def scrape_song_name(self, url, artist_name):
        page = requests.get(url)
        html = BeautifulSoup(page.text, "html.parser")
        song_name = html.find("title")

        # Quit artist_name
        regex = artist_name
        song_name = str(song_name).replace(regex, "")

        # Quit the first tag
        regex = "<title>"
        song_name = str(song_name).replace(regex, "")

        # last tag
        regex = "</title>"
        song_name = str(song_name).replace(regex, "")

        # quit the " - "
        regex = " – "
        song_name = str(song_name).replace(regex, "")

        regex = "Lyrics | Genius Lyrics"
        song_name = str(song_name).replace(regex, "")

        return song_name

    def write_lyrics_to_file(self, song_count):
        f = open('lyrics/' + self.pathDataset + '.txt', 'wb')
        for artist in self.artistList:
            urls = self.request_song_url(artist, song_count)
            for url in urls:
                lyrics = self.scrape_song_lyrics(url)
                #song_name = scrape_song_name(url, artist_name)
                lyrics = lyrics + "," + artist + "\n"
                f.write(lyrics.encode("utf-8"))
        f.close()
        num_lines = sum(1 for line in open(
            'lyrics/' + self.pathDataset + '.txt', 'rb'))
        print('Wrote {} lines to file from {} songs'.format(num_lines, song_count))
