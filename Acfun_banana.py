#-*-coding:utf-8-*-
import time
from urllib import request
from bs4 import BeautifulSoup
import requests
import win32api#调用win32api是为了显示剩下的香蕉树，当然如果你只是为了签到领香蕉，可以不用这么写
from datetime import datetime
user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'#
referer='http://www.acfun.tv/login/?returnUrl=http://www.acfun.tv/'#需要用到的请求头和refer
head={'User-Agent':user_agent,'Referer':referer}
ttt=time.time()#这里是返回了当前的时间，就是你发送登录请求的时间。
tt=str(ttt).split('.')#格式化字符串
ti=(''.join(tt))[:13])#python和javascript中的时间不一样，发送的时要以javascript中的时间为准，这里特做处理。
s=requests.Session()#使用requests登录，可以保存我们的cookies，方便我们登录以后访问到我们的主页，获得当前信息。
url='http://www.acfun.tv/login.aspx'
payload={'username':'*******','password':'******'}#这是你要提交的表单内容
r=s.post(url,headers=head,data=payload)#提交表单操作，使用post模拟登录
tt=s.post('http://www.acfun.tv/webapi/record/actions/signin?channel=0&date=%s'%(ti))#这里你已经登录了，可以使用之前的cookies访问其他的网页，抓包的结果，就是请求这个网页，并且发送一个时间的请求，就可以模拟签到。
print(ti)
htobj=s.get('http://www.acfun.tv/member/#area=splash').content#打开个人主页，以下就是用解析文本的过程，最终获得你当前的香蕉树。
htobj=htobj.decode('utf-8')

html=BeautifulSoup(htobj,'html.parser')

guide=html.find('div',{'class':'area-extra'})

banana=guide.find('a',{'href':'#area=banana'})
tt=banana.find('span')
win32api.MessageBox(0, '你还剩：'+tt.text+" 个香蕉", 'Information', 0)

