#-*-coding:utf-8-*-
from PIL import Image
img=Image.open('chuishi.png')
box=(0,0,img.width/3,img.height/3)
img_1=img.crop(box)
img_1.show()
def cut_img(im):
    img=Image.open(im)
    x1=x2=y1=y2=0
    t=1
    for i in range(3):
        y2+=img.height/3
        x1=0
        x2=0
        for j in range (3):
            x2+=img.width/3

            box=(x1,y1,x2,y2)
            print(box)
            out=img.crop(box)
            out.save('{}.png'.format(t))
            t+=1
            x1 += img.width / 3
        y1+=img.height/3

cut_img('chuishi.png')