from bs4 import BeautifulSoup
import requests
import re
import csv
import gc


def link(var):
    n = var
    for i in range(n):
        url = 'https://projecteuler.net/problem=' + str(i + 1) + '.html'
    return url


def totalQue(url):
    xPage = requests.get(url)
    soup = BeautifulSoup(xPage.text, "lxml")
    info = re.split(', ', soup.find_all('td', {'class': 'id_column'}).__str__())
    mr = int(re.findall('n">(.*)</', info[0])[0])
    lr = int(re.findall('n">(.*)</', info[-1])[0])
    return mr, lr


mq,lq = totalQue('https://projecteuler.net/recent')


i = 1
while i <= mq:
    url = link(i)
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
    ##questiom+
    questionHTML = str(soup.find("div", {"class": "problem_content"}))[45:-7]
    op = csv.writer(open("op9.csv", "ab"))
    if i < lq:
        dr = int(re.findall(':(.*)%', cac[-1])[0])
        cac1 = re.split(' ', cac[1])
        solved = cac1[-1]
        op.writerow((plno, title, questionHTML, dd, mm, yy, solved,dr))
    else:
        solved = int(re.findall('y (.*)</s',cac[1])[0])
        op.writerow((plno, title, questionHTML, dd, mm, yy, solved))
    print i
    i += 1
    gc.enable()
    gc.collect()
