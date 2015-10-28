from lxml import html
from lxml import etree
import requests
import re
import bs4

page = requests.get('https://projecteuler.net/problem=1.html',verify = True)
soup = bs4.BeautifulSoup(page.text,"lxml")
# #print (page)
# scraped = html.fromstring(page.text)s
# sscraped = etree.tostring(scraped)
# c= re.sub('&#13','++',sscraped)
# q = re.search('(.*)',sscraped).group(1)
q=soup.find_all('p')

print q

