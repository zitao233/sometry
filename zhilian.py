# -*- coding:utf-8 -*-
import urllib, re, time, os
global Joblist
global page
page = 1

#获取职业分类url
def getJobs(url):
    html = urllib.urlopen(url)
    text = html.read()
    pattern = re.compile(r'<div class="listcon height48">(.*?)</div>',re.S)
    jobs = re.findall(pattern, text)
    jobs = jobs[1]
    pattern = re.compile(r'<a href="(.*?)">(.*?)</a>')
    job = re.findall(pattern, jobs)
    return job

#打印职业分类并获取相关职业url
def getJob(L):
    return (L[0][1],L[0][0])

#获取具体职业url
def getTheJob(url):
    job = []
    for i in range(1,page+1):
        html = urllib.urlopen(url+ 'p'+ str(i))
        text = html.read()
        pattern = re.compile('<div class=".*?">.*?<span class="post"><a href="(.*?)" title=".*?</a></span>',re.S)
        job1 = re.findall(pattern, text)
        for j in job1:
            job.append(j)
    # os.chdir(r'D:\Desktop\text')
    # f = open('123.txt','w')
    # f.write(job)
    # f.close()
    print '获取单项内容完毕'
    return job

#分析职业信息
def analyzeJob(url):
    html = urllib.urlopen(url)
    text = html.read()
    pattern = re.compile(
        '<h1>(.*?)</h1>.*?target="_blank">(.*?)<.*?<li><span>职位月薪：</span><strong>(.*?)&nbsp;<a.*?<li><span>工作地点：</span><strong><a target="_blank" href="http://www.zhaopin.com/beijing/">(.*?)</a></strong></li>.*?<li><span>发布日期：</span><strong><span id="span4freshdate">(.*?)</span></strong></li>.*?<li><span>工作性质：</span><strong>(.*?)</strong></li>.*?<li><span>工作经验：</span><strong>(.*?)</strong></li>.*?<li><span>最低学历：</span><strong>(.*?)</strong></li>.*?<li><span>招聘人数：</span><strong>(.*?)</strong></li>',
        re.S)
    theJob = re.findall(pattern, text)
    return theJob


def main():
    print '运行开始\n',
    Joblist = getJobs('http://jobs.zhaopin.com/beijing/')
    n = len(Joblist)
    f = open('result.txt', 'w')
#    f.close()
#    f = open('C:\Users\user\Desktop\text\result.txt','a')
    f.write('读取到'+str(n)+'个职业分类。\n')
    print '读取到'+str(n)+'个职业分类。'
    i = 0
    y = 0
    while i<n:
        url = getJob(Joblist)[1]
        f.write(getJob(Joblist)[0]+'\n')
        job = getTheJob(url)
        for url in job:
            content = analyzeJob(url)
            for x in content:
                f.write('**************************\n')
                f.write('职位介绍：'+ x[0] + '\n')
                f.write('就职公司：'+ x[1] + '\n')
                f.write('职位月薪：'+ x[2] + '\n')
                f.write('工作地点：'+ x[3] + '\n')
                f.write('发布时间：'+ x[4] + '\n')
                f.write('工作性质：'+ x[5] + '\n')
                f.write('工作经验：'+ x[6] + '\n')
                f.write('最低学历：'+ x[7] + '\n')
                f.write('招聘人数：'+ x[8] + '\n')
                y += 1
                print '正在下载第%d个职位信息' %y
        del Joblist[0]
        print '第'+str(i)+'个获取完毕'
        i += 1
        f.write('以上为%d个职位信息，统计完毕。' %y)
    f.close()

main()

