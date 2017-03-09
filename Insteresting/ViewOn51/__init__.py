#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib2
import xml.sax
import xml.dom.minidom
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

currentpath = os.path.split(os.path.realpath(__file__))[0]
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

def xmlHandler(xmlString):
    DOMTree = xml.dom.minidom.parseString(xmlString)
    collection = DOMTree.documentElement
    data = {}
    elements = ['result','viewcount','serviceid',"viewresumename",'coid','coname',
                'indtypename','cotypename','cosizename','viewtime']
    for element in elements:
        value = collection.getElementsByTagName(element)[0]
        value = value.childNodes[0].data
        data[element] = value
#        print element + ':' + value
    print "get xml successfully"
    return  data

def sendEmail(subject,contant):
    sender = "o6943993@163.com"
    receiver = "1401182839@qq.com"
    smtpserver = "smtp.163.com"
    username = 'o6943993@163.com'
    password = 'Deng8155195'
    msg = MIMEText(contant, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = 'o6943993@163.com'
    msg['To'] = '1401182839@qq.com'
    smtp = smtplib.SMTP()
    try:
        smtp.connect(smtpserver)
    except smtplib.SMTPException:
        print 'sorry'
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

def getViewer():
    url = 'http://api.51job.com/'
    dir = 'api/user/get_resumeview_all.php?accountid=61596271&key=17ca24574384d58e95bed48e21356ff058305e3a'
    lasttime = '2016-11-22 15:58'
    while True:
        result = httpget(url,dir)
        data = xmlHandler(result)
        if data['viewtime'] != lasttime:
            saveData(data)
            lasttime = data['viewtime']
            print 'Update successfully'
        time.sleep(10)


def saveData(data):
    summary = data['coname'] + ':' + data['viewtime']
    details = ''
    print summary
    i = 0
    for key in data.keys():
        details = details + key + ":" + data[key] + "<br>"
    fp = open(currentpath +  '/1.html','a')
    content = '<details>' + '\n' + '<summary>'+ summary + '</summary>' + '\n' + '<p>' + details  + '</p>'+ '</details>'
    fp.write(content)


getViewer()

