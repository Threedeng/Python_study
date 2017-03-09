# -*- coding: UTF-8 -*-
from scrapy import log
from scrapy.spiders import Spider
import urllib2
from scrapy.selector import Selector
import sys
sys.path.append("E:\Study\Python\Spider\Scrapy\jobScrapy\jobScrapy")
reload(sys)
sys.setdefaultencoding('utf8')

from items import JobscrapyItem

class TesterSpider(Spider):
    name = "tester"
    allowed_domains = ["51job.com"]
    start_urls = []
    i = 0
    while  i < 1519/30 :
        i = i + 1
        start_urls.append("http://api.51job.com/api/job/search_job_list.php?postchannel=0000&&keyword=软件测试工程师&keywordtype=2&jobarea=040000&pageno=" + str(i) + "&pagesize=30")

    def parse(self, response):
        log.msg(response.body)
        items = []
        webitems = response.xpath('//item')
        a = webitems
        i=0
        for webitem in webitems:
            i = i + 1
            item = JobscrapyItem()
            item['jobid'] = webitem.xpath('//jobid['+ str(i) + ']/text()').extract()[0]
            item['jobname'] = webitem.xpath('//jobname['+ str(i) + ']/text()').extract()[0]
            item['cddr'] = webitem.xpath('//cddr['+ str(i) + ']/text()').extract()[0]
            item['coname'] = webitem.xpath('//coname['+ str(i) + ']/text()').extract()[0]
            item['jobarea'] = webitem.xpath('//jobarea['+ str(i) + ']/text()').extract()[0]

            item['providesalary'] = webitem.xpath('//providesalary['+ str(i) + ']/text()').extract()[0]

            items.append(item)



        return  items

