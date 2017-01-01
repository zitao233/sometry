# -*- coding:utf-8 -*-
import re
import urllib2
req = urllib2.urlopen('http://read.douban.com/tag/%E7%9F%AD%E7%AF%87%E5%B0%8F%E8%AF%B4/')
buf = req.read()
listurl = re.findall(r'https:.+\.jpg',buf)
i = 0
for url in listurl:
	f = open('douban'+str(i)+'.jpg','wb')
	req = urllib2.urlopen(url)
	buf = req.read()
	f.write(buf)
	i+=1
f.close
