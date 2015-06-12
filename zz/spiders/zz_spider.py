#coding: utf-8
import scrapy,re
from zz.items import zzItem

class zzSpider(scrapy.spider.Spider):
    name = "zz"
    allowed_domains = ["unsplash.com"]
    start_urls=["https://unsplash.com/"]
    f=open('bizhi.txt','wb')

    def parse(self, response):
        sel=scrapy.Selector(response)
        pre_path="http://download.unsplash.com/"
        sites=sel.xpath("//img[contains(@src,'photo')]/@src").extract()
        for site in sites:
            site_list=re.split("[-,?]",site)
            pid="photo-" + site_list[1] + "-" + site_list[2]
            full_path=str(pre_path+pid)
            self.f.write(full_path)
            self.f.write('\n')

