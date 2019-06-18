import requests
from bs4 import BeautifulSoup

class Product():
  def __init__(self, name, price, image, link):
    self.name = name
    self.price = price
    self.image = image
    self.link = link

def scrapSnapdeal(query):
  url = "https://www.snapdeal.com/search"
  params = {
      "keyword": query
  }

  r = requests.get(url, params=params)
  soup = BeautifulSoup(r.content)
  result = []
  products = soup.findAll('div', attrs = {"class": "product-tuple-listing"})
  for product in products:
    try:
      name = product.find('p', attrs = {"class": "product-title"}).text
      price = product.find('span', attrs = {"class": "product-price"}).text
      img_src = product.find('img', attrs = {"class": "product-image"}).attrs["src"]
      link = product.find('a', attrs = {"class": "dp-widget-link"}).attrs["href"]
      result.append(Product(name, price, img_src, link))
    except:
      pass
  return result
