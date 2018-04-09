from __future__ import division
import numpy as np
import cv2 
from matplotlib import pyplot as plt
import sys
sys.setrecursionlimit(10000)


def on_click2(event):
    global img,b,g,r,x,y,h
    lx=int(round(event.xdata))
    ly=int(round(event.ydata))
    if event.inaxes is not None:
        plt.close(4)
        red = int(r[ly,lx])
        green = int(g[ly,lx])
        blue = int(b[ly,lx])
        plt.figure(4,figsize=(7,2))
        plt.axis("off")
        plt.get_current_fig_manager().window.wm_geometry("-50-500")
        if x > h and y > h:
            mean, std = cv2.meanStdDev(img[y-h:y+h, x-h:x+h])
        else:
            mean, std = cv2.meanStdDev(img[y:y+h, x:x+h])
        
        intensity = "Intensidade: %.2f"%((red+green+blue)/3)
        vmean = np.mean(mean)
        vstd = np.mean(std)
        mean = " Mean : " +( str(mean) +(" Media: " + str(vmean)))
        std = " Std : " +( str(std) +( " Media: " + str(vstd)))
        plt.text(0,1,intensity)
        plt.text(0,0.5,mean)
        plt.text(0,0,std)
        plt.show()
    else:
        print 'Clicked ouside axes bounds but inside plot window'

def on_click(event):
    global img,x,y,h
    if event.inaxes is not None:
        x=int(round(event.xdata))
        y=int(round(event.ydata))
        h=11
        if x > h and y > h:
            crop_img = img[y-h:y+h, x-h:x+h]
        else:
            crop_img = img[y:y+h, x:x+h]
        plt.close(4)
        plt.figure(3,figsize=(7,4))
        plt.axis("off")
        plt.get_current_fig_manager().window.wm_geometry("-50-800")
        plt.connect('button_press_event', on_click2)
        plt.imshow(cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB))
        plt.show()
    else:
        print 'Clicked ouside axes bounds but inside plot window'

x = 0
y = 0
h = 0
# open image
img = cv2.imread('lena.png')
# img2 = cv2.imread('lena.png',0)
# split in channels
b,g,r = cv2.split(img)
#enum cores
color = ('b','g','r')
#show histogram 
plt.figure(1)
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
# histr = cv2.calcHist([img2],[0],None,[256],[0,256])
# plt.plot(histr,color = 'black')
# plt.xlim([0,256])
plt.get_current_fig_manager().window.wm_geometry("-1400-800")
# show image 
plt.figure(2)
plt.axis("off")
plt.get_current_fig_manager().window.wm_geometry("-640-800")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.connect('button_press_event', on_click)
plt.show()