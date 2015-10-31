from lxml import html
from lxml import etree
import requests
import re
import bs4

xml_link = 'https://projecteuler.net/rss2_euler.xml'
load_xml=requests.get(xml_link,verify=True)
soup_xml = bs4.BeautifulSoup(load_xml.text,"lxml")
number = soup_xml.find(string=re.compile("Problem")).__str__()
print type (number)
print number
num = re.search('Problem,(.*),break',number)
print num