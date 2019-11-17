import scrape
from utils import read_anime_file, create_url
from datetime import datetime, date
from twilio.rest import Client

credentials_file = "credentials.txt"
filename = "anime.txt"

anime_list = read_anime_file(filename)

with open(credentials_file) as f:
    line = f.readline()
    acn_sid, auth_token = line.split()
    line = f.readline()
    twilio_number, my_number = line.split()

client = Client(acn_sid, auth_token)

for anime in anime_list:
    message = ""
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
        message = f"\n\n{latest_episode['name']} released today!!\nURL: {latest_episode['url']}"
        client.messages.create(to=my_number, from_=twilio_number, body=str(message))