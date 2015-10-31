from bs4 import BeautifulSoup
import requests
import re

url = 'https://projecteuler.net/recent'

def xmlnumb(url):
    xPage = requests.get(url)
    soup = BeautifulSoup(xPage.text, "lxml")
    info = int(re.findall('">(.*)</',re.split(', ',soup.find_all('td',{'class':'id_column'}).__str__())[0])[0])
    return info

print xmlnumb(url)
