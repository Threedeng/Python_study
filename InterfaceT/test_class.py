#encoding:utf-8
import os
import ConfigParser
import os
import xlrd
import re
import httplib
import urllib
from urlparse import urlparse
import json
import time
import unittest
import pdf

currentdir=os.path.split(os.path.realpath(__file__))[0]
class test_class():
    def getexcel(self):
        casefile=currentdir + '/class.xls'
        if ((os.path.exists(casefile))==False):
            print "当前路径下没有case.xls，请检查"
        data=xlrd.open_workbook(casefile)
        table = data.sheet_by_name(casefile)
        nrows = table.nrows
        ncols = table.ncols

        for rownum in range(1,nrows):
            for col in range(3,ncols):
                value = table.cell(rownum,col).value
                if col == 3:
                    method = value
                if col == 4:
                    url = value

        return table,nrows,ncols

