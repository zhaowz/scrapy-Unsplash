# scrapy-Unsplash
爬取unsplash上的壁纸

##思路
1.爬取 [最美壁纸][1] 的第一屏（未解决瀑布流问题）壁纸
2.使用scrapy框架进行网页解析，得到图片链接
zzSpider.py：
```python
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
```
3.使用urllib2进行图片下载
download.py
```python
import urllib2

f=open("bizhi.txt",'r')
sites=f.readlines()
for i,site in enumerate(sites):
    url=site.strip("\n")          #去掉每行末的换行符
    print url
    u=urllib2.urlopen(url)
    data=u.read()
    downFile=open("./tmp"+"//"+str(i)+".png","wb") #当前路径下建立tmp文件夹，保存图片   /tmp/1.jpg
    downFile.write(data)
    downFile.close()
print "download over"
```
##存在问题
1. urlopen对https解析，在python3以下存在问题（暂时用http代替解析）
2. 瀑布流，无法进一步提取接下来的图片
