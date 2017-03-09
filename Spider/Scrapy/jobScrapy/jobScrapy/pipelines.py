# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook


def transSalary(self, salary):
    result = ''
    if "千" in salary:
        begnum = float(salary.split("-")[0]) * 1000
        endnum = float(salary.split('-')[1].split('千')[0]) * 1000
    elif "万" in salary:
        begnum = float(salary.split("-")[0]) * 10000
        endnum = float(salary.split('-')[1].split('万')[0]) * 10000
    else:
        return "No wan or qian"

    if '年' in salary:
        begnum = begnum/12
        endnum = endnum/12

    result = str(begnum) + '-' + str(endnum)
    return result,begnum,endnum

class JobscrapyPipeline(object):
    wb = Workbook()
    ws = wb.active
    ws.append(['Jobid','Jobname','cddr','coname','jobarea','providesalary'])



    def process_item(self, item, spider):
        salary = transSalary(self,item['providesalary'])
        line = [item['jobid'],item['jobname'],item['cddr'],item['coname'],item['jobarea'],item['providesalary'],salary[0],salary[1],salary[2]]
        self.ws.append(line)
        self.wb.save('E:\Study\Python\Spider\Scrapy\jobScrapy\job.xlsx')
        return item


