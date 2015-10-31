from bs4 import BeautifulSoup
import requests
import re
import csv


def link(var):
    n = var
    for i in range(n):
        url = 'https://projecteuler.net/problem=' + str(i + 1) + '.html'
    return url
#url = link(529)

def dataArchive(url):
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
    dr = int(re.findall(':(.*)%', cac[-1])[0])
    ################################
    questionHTML = str(soup.find("div", {"class": "problem_content"}))[45:-7]
    return plno, title, questionHTML, dd, mm, yy, solved, dr


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
    solved = int(re.findall('y (.*)</s',cac[1])[0])
    # dr = int(re.findall(':(.*)%', cac[-1])[0])
    ################################
    questionHTML = str(soup.find("div", {"class": "problem_content"}))[45:-7]
    return plno, title, questionHTML, dd, mm, yy, solved
    return solved



def xmlnumb(url):
    xPage = requests.get(url)
    soup = BeautifulSoup(xPage.text, "lxml")
    info = re.split(', ', soup.find_all('td', {'class': 'id_column'}).__str__())
    mr = int(re.findall('n">(.*)</', info[0])[0])
    lr = int(re.findall('n">(.*)</', info[-1])[0])

    return mr, lr


urlR = 'https://projecteuler.net/recent'

i = 520
n, m = xmlnumb(urlR)

while i <= n:
    url = link(i)
    op = csv.writer(open("test.csv", "ab"))
    if i < m:
        op.writerow(dataArchive(url))
    else:
        op.writerow(dataRecent(url))
    print i
    i += 1
