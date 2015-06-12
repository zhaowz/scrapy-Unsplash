#coding: utf-8
import urllib2

f=open("bizhi.txt",'r')
sites=f.readlines()
for i,site in enumerate(sites):
    url=site.strip("\n")          #去掉每行末的换行符
    print url
    u=urllib2.urlopen(url)
    data=u.read()
    downFile=open("./tmp"+"//"+str(i)+".png","wb")   #当前路径下建立tmp文件夹，保存图片   /tmp/1.jpg
    downFile.write(data)
    downFile.close()
print "download over"

