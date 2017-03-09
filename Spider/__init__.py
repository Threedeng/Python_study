# code:UTF-8
import urllib
import re
import xlrd
from xlutils.copy import copy
import os

currentdir=os.path.split(os.path.realpath(__file__))[0]


def getHtml(url):  #Get Html Page
    page = urllib.urlopen(url)
    html = page.read()
#    print html
    return html

def getPrice(html,page):
    reg = r'<b class=\'pri\'>.*/b>'
    pricere = re.compile(reg)
    priceList = re.findall(pricere,html)
    priceL = []
    row = (page - 1) * 20

    reg1 = r'http://cd.58.com.*shtml'
    addressRe = re.compile(reg1)
    addressList = re.findall(addressRe,html)
    addressList = list(set(addressList))
    print addressList
    addressL = []
    num = 0
    for price in priceList:
        priceL.append(price[15:-4])
        insertExcel(row,1,price[15:-4])
        row=row+1
        num = num + 1
    row = row - num
    for add in addressList:
        addressL.append(add)
        insertExcel(row,2,add)
        row=row+1

    print priceL
    return priceList


def insertExcel(rowx, colx, content):
    rbook = xlrd.open_workbook(currentdir+'\\result.xlsx')
    wbook = copy(rbook)
    wsheet = wbook.get_sheet(0)
    wsheet.write(rowx, colx, content)
    wbook.save('result.xlsx')

url = "http://cd.58.com/xiaoqu/kaihualijing/chuzu/pn_3/"
i=1
row = 1
col = 1
while i<8:
    url = "http://cd.58.com/xiaoqu/kaihualijing/chuzu/pn_" + str(i) +"/"
    getPrice(getHtml(url),i)
    i = i + 1

