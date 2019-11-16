import scrape

url = "https://kissanime.ru/Anime/Dr-Stone/"
episodes_metadata = scrape.getAnimeEpisodesDetails(url)

"""
return a list of dictionaries where fields are:
name, url, title, release_date
"""