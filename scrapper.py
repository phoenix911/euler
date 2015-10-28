from lxml import html
from lxml import etree
import requests
import re
import bs4
import csv

def scrapper(i):
    for n in range(1,i+1):
        url='https://projecteuler.net/problem='+str(n)+'.html'
        print url
        page = requests.get(url,verify = True)
        #print (page)
        scraped = html.fromstring(page.text)
        sscraped = etree.tostring(scraped)
        basic_info = (re.search('<h2>(.*)</div>',sscraped)).group(1)
        name = re.search('(.*)</h2>',basic_info).group(1)
        number = re.search('<h3>(.*)</h3>',basic_info).group(1)
        published_date = re.search(',(.*),',basic_info).group(1)
        difficulty_rating = re.search('rating:(.*)%',basic_info).group(1)
        soup = bs4.BeautifulSoup(page.text,"lxml")
        q=soup.find_all('p').__str__()
        qu = re.sub('<p>','',q)
        qu = re.sub('</p>','',qu)
        qu = qu[1:-2]
        published_date= published_date[1:]
        difficulty_rating= difficulty_rating[1:]
        sl = number[8:]
        op = csv.writer(open("dboct.csv", "ab"))
        op.writerow([sl,number,name,qu,difficulty_rating,published_date])
    return n

print scrapper(522)