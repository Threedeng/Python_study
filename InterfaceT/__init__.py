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

rowUrl = 3
rowDir = 4
rowMethod = 5
rowParas = 6
rowExRes = 7
rowAcRes = 8
rowNoMatched =9
rowNoExRes = 10
rowNoAcRes = 11

def getexcel():
    print '请在当前目录下准备名为case.xlsx的excel用例文件！'
    print '--------------------------以下为用例文件规则--------------------------'
    print '1.第一行不写用例'
    print '2.其中第四列为http请求url地址'
    print '3.第五列为http请求路径'
    print '4.第六列为http请求方法'
    print '5.第七列为http Post请求参数'
    print '6.Post请求参数格式为 username=xxxxxx&password=xxxxxx,以 & 为分割符'
    print '----------如果已准备好，请输入回车，或输入其他字符退出程序----------'
    '''
    ready = str(raw_input())
    if not(ready != '/r'):
        exit()
    '''
    if ((os.path.exists(casefile)) == False):
        print casefile + " 当前路径下没有case.xlsx，请检查"
        exit()

    book = xlrd.open_workbook(casefile)
    wbook = copy(book)
    wbook.save('result.xlsx')

    table = book.sheet_by_name("Login")
    nrows = table.nrows
    ncols = table.ncols

    for i in range(1,nrows):
        url = 'http://' + table.cell(i,rowUrl).value
        dir = table.cell(i,rowDir).value
        method = table.cell(i,rowMethod).value
        paras = table.cell(i,rowParas).value
        expect = table.cell(i,rowExRes).value
        if method == 'Post':
            result = httppost(url, dir, paras)
            print result
            assertResult(result,expect,i)
#            table.put_cell(i,9,1,result,0)
            insertExcel(i,rowAcRes,result)
        elif method == 'Get':
            result = httpget(url,dir)
            insertExcel(i, rowAcRes, result)
            assertResult(result, expect, i)
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
#        httpClient = httplib.HTTPConnection('www.baidu.com', '80',timeout=30)
#        httpClient.request('GET', dir)
#        response = httpClient.getresponse()
        request = urllib2.Request(url+dir)
        response = urllib2.urlopen(request)
        result =  response.read()
        return result
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

def assertResult(result, expect, caserow):
    dictResult = eval(result)
    dictExpect = toDict(expect)
    print dictExpect
    unMatchedKey = []
    noinExpKey = []
    noinResKey = []
    for key in dictResult.keys():
        if key not in dictExpect.keys():
            noinExpKey.append(key)
        else:
            if dictResult[key] != dictExpect[key]:
                unMatchedKey.append(key)
    for key in dictExpect.keys():
        if key not in dictResult.keys():
            noinResKey.append(key)

    insertExcel(caserow,rowNoMatched,str(unMatchedKey))
    insertExcel(caserow,rowNoExRes,str(noinExpKey))
    insertExcel(caserow,rowAcRes,str(noinResKey))
    print str(unMatchedKey)
    print str(noinExpKey)
    print str(noinResKey)

def toDict(sString):
    if sString == "":
        return {"Error Message":"No Expect Result!"}
    listR = sString.split("&")
    dictR = {}
    for strR in listR:
        listTemp = strR.split("=")
        dictR[listTemp[0]] = listTemp[1]
    return dictR

getexcel()