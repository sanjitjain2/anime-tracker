from bs4 import BeautifulSoup
import requests
import scrape

def parse_page_bs4(page):
	soup = BeautifulSoup(page.text, 'lxml')
	anime_list_episodes = soup.find(class_="bigBarContainer")
	print(type(anime_list_episodes))
	anime_list_episodes_items = anime_list_episodes.findall('a')
	return anime_list_episodes_items


def read_anime_file(filename):
	anime_list = []
	with open(filename) as fp:
		line = fp.readline()
		anime_list.append(line)
		while line:
			line = fp.readline()
			anime_list.append(line)
	
	return anime_list[:-1]

def add_anime(anime_name, filename):
	with open(filename, 'a') as f:
		f.write(anime_name)


def create_url(anime_name):
	anime_link = "https://kissanime.ru/Anime/"
	
	anime_name = anime_name.replace('!', '')
	anime_name = anime_name.replace('(', '')
	anime_name = anime_name.replace(')', '')
	anime_name = anime_name.replace(':', '')
	anime_name = anime_name.replace(".", ' ')
	anime_name = anime_name.replace("'", ' ')
	list_words = anime_name.split()
	s = "-"
	anime_name =  s.join(list_words)
	return anime_link + anime_name
