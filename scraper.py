import urllib.request
import os
from bs4 import BeautifulSoup

NPAGES = 11
DIR = "html"
dir_path = os.getcwd()+"\\"+DIR

def main():
	if not os.path.exists(dir_path):
		os.mkdir(dir_path)
	#Imdb 1000 greatest film of all time
	url = "https://www.imdb.com/list/ls006266261/"
	for n in range(1, NPAGES):
		try:		
			filename = os.path.join(dir_path, "page"+str(n))
			print("page"+str(n))
			urllib.request.urlretrieve(url, filename)
			with open(filename, "r", encoding="utf-8") as outfile:
				content = outfile.read()
				soup = BeautifulSoup(content, 'html.parser')
				url = soup.find("a", "next-page").get('href') 
				url = "https://www.imdb.com"+url 
				print(url)	
		except Exception as e:
			print(str(e))
			print(url)

if __name__ == '__main__':
	main()