from bs4 import BeautifulSoup
import cfscrape
import re

scraper = cfscrape.create_scraper()

def getAnimeList(link):
    source = scraper.get(link)
    soup = BeautifulSoup(source.text, 'lxml')

    lst = []

    for anime in soup.find_all('tr')[2:]:
        title = anime.td.a.text.strip()
        url = anime.td.a['href'].strip()
        status = anime.find_all('td')[-1].text.strip()

        lst.append({
            'title': title,
            'url': url,
            'status': status
        })

    return lst


def getAnimeInformantion(link):
    source = scraper.get(link)
    soup = BeautifulSoup(source.text, 'lxml')

    container = soup.find('div', id='container')

    name = container.find('a', class_='bigChar').text.strip()

    genreList = [genre.text.strip() for genre in container.find_all('a', class_='dotUnder')]

    p = container.find_all('p')

    description = p[-1].text.strip().replace(u'\xa0', u' ')

    aired = p[2].text.strip().replace(u'\xa0', u' ')

    detail = p[3].text.split("\n")
    detail = [x.strip().replace(u'\xa0', u' ') for x in detail if x is not None]

    status = detail[1].split(":")[1]
    views = detail[2].split(":")[1]

    animeDescription = {
        "name": name,
        "aired": aired,
        "status": status,
        "views": views,
        "genre": genreList,
        "description": description
    }

    return animeDescription


def getEpisodeVideoUrl(link):
    source = scraper.get(link)
    soup = BeautifulSoup(source.text, 'lxml')
    episodeUrl = []
    for line in soup:
        stuff = re.findall('\S+rapidvideo.com\S+', str(line))
        if (len(stuff) > 0):
            episodeUrl.append(stuff)

    return episodeUrl[0]


def getAnimeEpisodesDetails(link):
	source = scraper.get(link)

	soup = BeautifulSoup(source.text, 'lxml')   
	episode_links = soup.find('table')
	if episode_links is None:
		return None 

	dates = soup.find_all('td') 

	def regex_date(date):
		return re.findall('[0-9]{1,3}/[0-9]{1,}/[0-9]{1,4}', str(date))

	dates = [regex_date(dates[i]) for i in range(1, len(dates),2)]
	
	lst = []
	i=0
	for items in episode_links.find_all('a'):
		name = items.text.strip()
		url = items['href']
		url = f"http://kissanime.ru/{items['href']}"
		title = items['title']
		date = dates[i]
		i += 1
		lst.append({"name": name, "url": url, "title": title, "release_date":date})

	return lst[:2]


def getCustomAnimeList(link):
    source = scraper.get(link)
    soup = BeautifulSoup(source.text, 'lxml')

    lst = []

    for anime in soup.find_all('tr')[2:]:
        title = anime.td.a.text.strip()
        url = anime.td.a['href'].strip()
        status = anime.find_all('td')[-1].text.strip()

        lst.append({
            'title': title,
            'url': url,
            'status': status
        })

    return lst
