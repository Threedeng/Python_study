#coding:utf-8
import os
import ConfigParser
import os
import xlrd
import re
import httplib
import urllib
import urllib2
from urlparse import urlparse
import json
import time
import unittest
import xlwt

from xlutils.copy import copy

currentdir=os.path.split(os.path.realpath(__file__))[0]
casefile = currentdir + '\case.xlsx'

def getexcel():
    print '请在当前目录下准备名为case.xlsx的excel用例文件！'
    print '--------------------------以下为用例文件规则--------------------------'
    print '1.第一行不写用例'
    print '2.其中第四列为http请求url地址'
    print '3.第五列为http请求路径'
    print '4.第六列为http请求方法'
    print '5.第七列为http Post请求参数'
    print '6.Post请求参数格式为 username=xxxxxx&password=xxxxxx,以 & 为分割符'
    print '----------如果已准备好，请输入 Y 回车，或输入其他字符退出程序----------'
    ready = str(raw_input())
    if not(ready == 'Y' or ready == 'y'):
        print '请准备好再打开，谢谢！'
        exit()
    if ((os.path.exists(casefile)) == False):
        print casefile + " 当前路径下没有case.xlsx，请检查"
        exit()
    if ((os.path.exists(currentdir+'\\result.xlsx')) == False):
        print casefile + " 当前路径下没有result.xlsx，请检查"
        exit()

    book = xlrd.open_workbook(casefile)
    wbook = copy(book)
    wbook.save('result.xlsx')

    table = book.sheet_by_name("Login")
    nrows = table.nrows
    ncols = table.ncols

    for i in range(1,nrows):
        url = 'http://' + table.cell(i,3).value
        dir = table.cell(i,4).value
        method = table.cell(i,5).value
        paras = table.cell(i,6).value
        if method == 'Post':
            result = httppost(url, dir, paras)
            print result
#            table.put_cell(i,9,1,result,0)
            insertExcel(i,7,result)
        elif method == 'Get':
            httpget(url,dir)
        else:
            print 'Sorry!Please input correct http method!'


def httppost(url,dir,para):
    httpClient = None
    try:
#        paras = urllib.urlencode(displiteparas(para))
#        print paras

        print para
        request = urllib2.Request(url+dir,para)
        response = urllib2.urlopen(request)
        result = response.read()
        return result
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()



def httpget(url,dir):
    httpClient = None
    try:
        httpClient = httplib.HTTPConnection(url,80,timeout=30)
        httpClient.request('GET',dir)
        response = httpClient.getresponse()
        print '------------------------------Here is status---------------------------------------'
        print  response.status
        print '------------------------------Here is reason---------------------------------------'
        print response.reason
        print '-------------------------------Here is read------------------------------------------'
        print  response.read()
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()


def displiteparas(parasS):
    paras = parasS.split(';')
    listP = {}
    for i in paras:
        para = i.split(':')
        listP[para[0]] = para[1]
    return listP


def insertExcel(rowx, colx, content):
    rbook = xlrd.open_workbook(currentdir+'\\result.xlsx')
    wbook = copy(rbook)
    wsheet = wbook.get_sheet(0)
    wsheet.write(rowx, colx, content)
    wbook.save('result.xlsx')

getexcel()