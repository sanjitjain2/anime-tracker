import scrape
from utils import read_anime_file, create_url
import datetime

filename = "test.txt"
anime_list = read_anime_file(filename)
for anime in anime_list:
    url = create_url(anime)
    episodes_metadata = scrape.getAnimeEpisodesDetails(url)
	
