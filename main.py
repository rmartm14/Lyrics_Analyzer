import lyricsgenius
from requests.exceptions import HTTPError, Timeout
import artistListScraping as al
import re


def remove_punctuation(lyrics):
    return re.sub(r'[^\w\s]', '', lyrics)


token = '7XFgPELzsHlp6CtJZv1gaqwNfqDhzx6838_-Ttwq6gGiNDKd6rU6f9S1MBNvItOz'
NUM_CANCIONES = 5
urlArtistas = "https://es.wikipedia.org/wiki/Anexo:Los_100_mejores_artistas_de_la_Historia_seg%C3%BAn_la_revista_Rolling_Stone"

listaArtistas = al.artistListScraping(urlArtistas).scrape_list()
genius = lyricsgenius.Genius(token)
genius.remove_section_headers = True
current_artist = list()

for current_artist in listaArtistas:
    try:
        artist = genius.search_artist(
            current_artist, max_songs=NUM_CANCIONES, include_features=False)
    except Timeout:
        artist = genius.search_artist(
            current_artist, max_songs=NUM_CANCIONES, include_features=False)

    a = open("./lyrics/Lyrics.txt", 'wb')
    for i in range(0, len(artist.songs)):
        lyrics = remove_punctuation(artist.songs[i].lyrics)
        a.write(str(lyrics + ", " +
                    current_artist + "\n").encode("utf-8"))
    a.close()
