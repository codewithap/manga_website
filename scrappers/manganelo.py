import requests
from bs4 import BeautifulSoup as bs
import json

class manganelo:
  def __init__(self):
    self.base_url = "https://ww5.manganelo.tv/"

  def search(query): 
    r = requests.get(f"https://ww5.manganelo.tv/search/{query}").text
    soup = bs(r, 'html.parser')
    html = soup.select(".panel-search-story .search-story-item")
    data = '{"data": ['
    for item in html:
      img = "https://ww5.manganelo.tv"+item.find("img")["src"]
      title = item.find("img")["alt"]
      link = item.find("a")["href"].replace("/manga/","")
      info = "{" + f'"img" :"{img}", "title": "{title}", "id": "{link}"'+ "},"
      data = data + info
    jsonData = data[:-1] + ']}'
    try:
    	d =  json.loads(jsonData)
    except:
    	d = {
    		"err": "manga not found"
    	}
    return d

  # returns all chapters name and list from mangaLink
  def getChapters(link): 
    r = requests.get("https://ww5.manganelo.tv/manga/"+link).text
    soup = bs(r, 'html.parser')
    html = soup.select("a.chapter-name")
    data = '{"data": ['
    for item in html: 
      title = item.text
      link = item["href"]
      info = "{" + f'"title": "{title}", "link": "{link}"'+ "},"
      data = data+info
    jsonData = data[:-1] + ']}'
    return json.loads(jsonData)

  # returns the list of mangaJpgs
  def getManga(url): 
    r = requests.get("https://ww5.manganelo.tv/"+url).text
    soup = bs(r, 'html.parser')
    html = soup.select(".container-chapter-reader img")
    imgs = []
    for item in html:
      imgs.append(item["data-src"])
    return imgs


#print(manganelo.getManga("/chapter/manga-ng952689/chapter-1"))
#print(getManga("https://ww5.manganelo.tv/chapter/manga-gi983965/chapter-6"))

