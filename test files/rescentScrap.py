from bs4 import BeautifulSoup
import requests
import re

url = 'https://projecteuler.net/recent'

def xmlnumb(url):
    xPage = requests.get(url)
    soup = BeautifulSoup(xPage.text, "lxml")
    info = re.split(', ',soup.find_all('td',{'class':'id_column'}).__str__())
    mr = int(re.findall('n">(.*)</',info[0])[0])
    lr = int(re.findall('n">(.*)</',info[-1])[0])

    return mr,lr


def dataRecent(url):
    wPage = requests.get(url)
    soup = BeautifulSoup(wPage.text, "lxml")
    title = str(soup.h2)
    title = title[4:-5]  ########
    name = str(soup.h3)
    name = name[4:-5]  ##########
    nameNsl = re.split(' ', name)
    plno = nameNsl[1]  ##########
    #################################
    genInfo = str(soup.find("div", {"class": "info"}))
    cac = re.split(';', genInfo)
    date = re.split(' ', cac[0])
    dd = date[-5][:-2]
    mm = date[-4]
    yy = date[-3][:-1]
    cac1 = re.split(' ', cac[1])
    solved = cac1[-1]
    #dr = int(re.findall(':(.*)%', cac[-1])[0])
    ################################
    questionHTML = str(soup.find("div", {"class": "problem_content"}))[45:-7]
    return plno, title, questionHTML, dd, mm, yy, solved, dr

n,m = xmlnumb(url)
print n
print m

