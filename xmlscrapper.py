from lxml import html
from lxml import etree
import requests
import re
import bs4

xml_link = 'https://projecteuler.net/rss2_euler.xml'
load_xml=requests.get(xml_link,verify=True)
soup_xml = bs4.BeautifulSoup(load_xml.text,"lxml")
soup_xml = soup_xml.find_all('p')
print (soup_xml)
number = re.search('Problem #,(.*),:',soup_xml)
print number