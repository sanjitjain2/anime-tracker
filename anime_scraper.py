import scrape
from utils import read_anime_file, create_url
from datetime import datetime, date

filename = "test.txt"
anime_list = read_anime_file(filename)

for anime in anime_list:
    url = create_url(anime)
    episodes_metadata = scrape.getAnimeEpisodesDetails(url)
    """
    return a list of dictionaries where fields are:
    name, url, title, release_date
    """
    if (episodes_metadata == None):     # anime not found
        continue    
    
    latest_episode = episodes_metadata[0]
    not_latest_episode = episodes_metadata[1]
    
    latest_date = latest_episode['release_date'][0]
    latest_date = datetime.strptime(latest_date, '%m/%d/%Y').date()
    
    today = date.today()

    if(latest_date == today):
        message = f"\n{latest_episode['name']} released today!!\nURL: {latest_episode['url']}\n"
        print(message)