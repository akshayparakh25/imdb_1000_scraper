import os
from bs4 import BeautifulSoup
import csv

DIR = "html"
dir_path = os.getcwd()+"\\"+DIR
def fetch_html():
	with open("imdb_data.csv", "w+") as writefile:
		fields = ['Seq', 'Title', 'Year', 'Certificate', 'Runtime(Minutes)', 'Genre', 'Imdb Rating', 'Directors', 'Actors', 'User Votes', 'Gross(in Million Dollars)']
		writer = csv.writer(writefile, delimiter="\t")
		writer.writerow(fields)
		if os.path.exists(dir_path):
			for file in os.listdir(dir_path):
				print(file)
				with open(os.path.join(dir_path,file), "r", encoding="utf-8") as outfile:
					content = outfile.read()
					soup = BeautifulSoup(content, 'html.parser')
					for item in soup.find_all("div", "lister-item-content"):
	#					print(item.text)
						header = item.find("h3", "lister-item-header")
						#sequence Number
						seq = header.find("span", "lister-item-index").text
						seq = seq[:-1]
						#title of the film
						title = header.find("a").text
						#year of release
						year = header.find("span", "lister-item-year").text
						year = year.replace('(','').replace(')','').replace('|','')
						info = item.find("p", "text-muted")
						#certficate recieved by the film
						if info.find("span", "certificate") != None:
							certificate = info.find("span", "certificate") .text
						else:
							certificate = None
						#movie runtime
						runtime_minutes = info.find("span", "runtime").text
						runtime_minutes = runtime_minutes.replace('min', ''); runtime_minutes = runtime_minutes.rstrip()
						#movie genre
						genre = info.find("span", "genre").text
						genre = genre.strip()
						genre = genre.split(',')
						#imdbRating
						imdb_rating = item.find("div", "ipl-rating-star").text.strip()
						#director and actor
						namess = info.find_next_sibling("p","text-muted")
						names = info.find_next_sibling("p","text-muted").text
						names = names.strip().split('|')
						directors = ""
						actors = ""
						for name in names:
							#print(name.replace('\n', '').strip())
							name = name.replace('\n', '').strip().split(':')
							#print(name)
							if "Director" in name or "Directors" in name:
								directors = name[1:]
							if "Stars" in name or "Star" in name:
								actors = name[1:]
#						print(seq, title, year, certificate, runtime_minutes, genre, imdb_rating, directors, actors)
						#votes and gross
						inf = namess.find_next_sibling("p", "text-muted").text.split('|')
						#print(inf)
						votes = ""
						gross_mill_doll = ""
						for i in inf:
							i = i.strip().split(':')
							#print(i)
							if 'Votes' in i:
								votes = i[1].replace(',', '').strip()
							if 'Gross' in i:
								gross_mill_doll = i[1].replace(',', '').strip().replace('$', '').replace('M', '')
						print(seq, title, year, certificate, runtime_minutes, genre, imdb_rating, directors, actors, votes, gross_mill_doll)
						writer.writerow([seq, title, year, certificate, runtime_minutes, genre, imdb_rating, directors, actors, votes, gross_mill_doll])
		
fetch_html()