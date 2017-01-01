# -*- coding:utf-8 -*-
import re
import urllib2
req = urllib2.urlopen('http://www.imooc.com/course/list')
buf = req.read()
listurl = re.findall(r'http:.+\.jpg',buf)
i = 0
for url in listurl:
	f = open(str(i)+'.jpg','wb')
	req = urllib2.urlopen(url)
	buf = req.read()
	f.write(buf)
	i+=1
f.close
