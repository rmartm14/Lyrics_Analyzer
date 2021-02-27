import geniusScraping as gs
import artistListScraping as al

NUM_CANCIONES = 5

urlArtistas = "https://es.wikipedia.org/wiki/Anexo:Los_100_mejores_artistas_de_la_Historia_seg%C3%BAn_la_revista_Rolling_Stone"


listaArtistas = al.artistListScraping(urlArtistas).scrape_list()
print(listaArtistas)
clase = gs.geniusScraping(artist=listaArtistas)

clase.write_lyrics_to_file(NUM_CANCIONES)
