# -*- coding:utf-8 -*-
import urllib, re, time
Totol = 0
n = 0
for ID in range(0, 101, 20):
    print '\n'
    html = urllib.urlopen('https://read.douban.com/tag/%E7%9F%AD%E7%AF%87%E5%B0%8F%E8%AF%B4/?cat=article&sort=top&start='+str(ID))
    html = html.read()
    pattern = r'<span class="price-tag ">(.*?)</span>.*?<div class="title"><.*?>(.*?)</a>.*?</div><p class=""><span class=""><span class="label">作者</span><.*?><.*?>(.*?)</a>.*?</span></span>.*?</p><p class=""><.*?><span class="label">类别</span><.*?><.*?> (.*?) </span>.*?</span></span></p>'
    reg = re.compile(pattern)
    rel = re.findall(reg, html)
    for i in rel:
        print '书名：' + i[1]+ '\n' + '\t' + '单价：'+ i[0] + '\t' + '作者：'+ i[2] + '\t' + '类型：'+ i[3]
        n += 1
        if i[0] == '免费':
            continue
        else:
            Totol += float(i[0][0:-3])
ave = Totol/n
print '-----------------------------------'
print '共%d本书' %n
print '总价：%f元\n平均：%f' %(Totol, ave)
