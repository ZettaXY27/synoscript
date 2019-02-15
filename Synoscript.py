import urllib2
import requests
from bs4 import BeautifulSoup

synonym = raw_input("Type in a word you wish to find synonyms of\n")

resp = requests.get("https://www.thesaurus.com/browse/" + synonym)
soup = BeautifulSoup(resp.text, 'html.parser')
l = soup.find("ul",{"class":"css-1lc0dpe et6tpn80"})

for i in l.findAll("a"): 
                print(i.text);
