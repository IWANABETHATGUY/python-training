#-*-coding:utf-8-*-
import requests
import time
from PIL import Image,ImageOps
from urllib import request
from bs4 import BeautifulSoup
import subprocess
import requests
import win32api
from datetime import datetime
import time
import time
user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
referer='http://www.acfun.tv/login/?returnUrl=http://www.acfun.tv/'
head={'User-Agent':user_agent,'Referer':referer}
baseurl='http://www.acfun.tv/captcha.svl'
ttt=time.time()

tt=str(ttt).split('.')
ti=(''.join(tt))[:13]

# request.urlretrieve(baseurl,'captcha.jpg')
# cleanImage("capmain.tif")
# p = subprocess.Popen(["tesseract", "cap0.png", "captcha"],stdout=
#     subprocess.PIPE,stderr=subprocess.PIPE)
# p.wait()
# f = open("captcha.txt", "r")
# captchaResponse = f.read().replace(" ", "").replace("\n", "")
# print("Captcha solution attempt: "+captchaResponse)
s=requests.Session()
url='http://www.acfun.tv/login.aspx'
payload={'username':'18692259817','password':'forhxj1996'}
r=s.post(url,headers=head,data=payload)
print(r.text)
tt=s.post('http://www.acfun.tv/webapi/record/actions/signin?channel=0&date=%s'%(ti))
print(ti)


htobj=s.get('http://www.acfun.tv/member/#area=splash').content
htobj=htobj.decode('utf-8')

html=BeautifulSoup(htobj,'html.parser')

guide=html.find('div',{'class':'area-extra'})

banana=guide.find('a',{'href':'#area=banana'})
tt=banana.find('span')
win32api.MessageBox(0, '你还剩：'+tt.text+" 个香蕉", 'Information', 0)
for i in range (720):
    htobj = s.get('http://www.acfun.tv/member/#area=splash')
    print(htobj)
    time.sleep(10)