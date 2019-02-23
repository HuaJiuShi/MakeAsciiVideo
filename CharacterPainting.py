#-*- coding:utf-8 -*-
import cv2
import numpy as np
import os

#字符视频生成代码
cap = cv2.VideoCapture("testVid3.wmv")
ascii_char = list(" .-=/<([+*123456789cvadtxw")

asciiRow = 32
asciiCol = 64
vidFPS = cap.get(5)
print(vidFPS)
frameNum = 0

while 1:
    ret, frame = cap.read()
    if ret is False:
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    frame = cv2.resize(frame, (asciiCol, asciiRow), interpolation=cv2.INTER_CUBIC)
    frame = cv2.equalizeHist(frame)
    frame = frame//10
    
    #OpenCV图片添加字符
    font=cv2.FONT_HERSHEY_SIMPLEX   #使用默认字体
    asciiImg=np.zeros((asciiRow*30, asciiCol*30, 3), np.uint8) + 255
    
    for i in range(asciiRow):
        for j in range(asciiCol):
            #添加文字，1.2表示字体大小，（0,40）是初始的位置，(255,255,255)表示颜色，2表示粗细
            asciiImg = cv2.putText(asciiImg, ascii_char[25-frame[i][j]], (j*30+2, i*30+25), font, 1, (0,0,0), 2)
            j = j + 1
        i = i + 1
        
    cv2.imwrite('asciiImgs/'+str(frameNum)+'.jpg', asciiImg)
    frameNum = frameNum + 1
    print(frameNum)
    if frameNum > 101:
        break
    cv2.namedWindow("img",cv2.WINDOW_NORMAL)
    cv2.imshow("img", asciiImg)
    
    cv2.namedWindow("raw",cv2.WINDOW_NORMAL)
    cv2.imshow("raw", frame*10)
    if cv2.waitKey(10) & 0xff == ord("q"):
        break

'''
#将图片合成视频
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
video_writer = cv2.VideoWriter("test001.avi", fourcc, 30, (asciiRow*30, asciiCol*30))
for i in range(100):
    frame = cv2.imread(os.path.join('asciiImgs/'+'{}.jpg'.format(i)))
    video_writer.write(frame)
video_writer.release()
'''

'''
ascii_char = list("　／＊＋－ａｂｃｄｅ？＜｛ｆｇｈｉｊｋｌｍｎ＝－９）（５０７")
while(1):
    ret, frame = cap.read()
    if ret == False:
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    frame = cv2.resize(frame, (960, 480), interpolation=cv2.INTER_CUBIC)
    frame = cv2.equalizeHist(frame)
    #ret, frame = cv2.threshold(frame,0,255,cv2.THRESH_OTSU)
    
    #将0-255灰度值均匀映射到25个灰度值
    frame = frame//10

    imgTxt = open('imgTxt.txt', 'w')
    for j in range(47):
        j = j + 1 
        for i in range(96):
            imgTxt.write(ascii_char[frame[j][i]])
            i = i + 1
        imgTxt.write('\n')
    imgTxt.close()
    
    frame = frame * 10 + 5

    cv2.namedWindow("cap",cv2.WINDOW_NORMAL)
    cv2.imshow("cap", frame)
    
    if cv2.waitKey(10) & 0xff == ord("q"):
        break
'''

'''
#OpenCV图片添加字符
font=cv2.FONT_HERSHEY_SIMPLEX#使用默认字体
im=np.zeros((60,200,3),np.uint8)+255
img=cv2.putText(im,'0223456789',(0,25),font,1,(0,0,0),2)#添加文字，1.2表示字体大小，（0,40）是初始的位置，(255,255,255)表示颜色，2表示粗细
img=cv2.putText(im,'0223456789',(0,55),font,1,(0,0,0),2)
cv2.namedWindow("img",cv2.WINDOW_NORMAL)
cv2.imshow("img", img)
cv2.waitKey(0)
'''


'''
#字符画生成代码
ascii_char = list("　／＊＋－ａｂｃｄｅ？＜｛ｆｇｈｉｊｋｌｍｎ＝－９）（５０７")

cap1 = cv2.imread("testImg2.jpg",1)
frame = cv2.cvtColor(cap1, cv2.COLOR_BGR2GRAY) 
frame = cv2.resize(frame, (96, 48), interpolation=cv2.INTER_CUBIC)
frame = cv2.equalizeHist(frame)
#ret, frame = cv2.threshold(frame,0,255,cv2.THRESH_OTSU)
#将0-255灰度值均匀映射到25个灰度值
frame = frame//10
imgTxt = open('imgTxt.txt', 'w')
for j in range(47):
    j = j + 1 
    for i in range(96):
        imgTxt.write(ascii_char[25-frame[j][i]])
        i = i + 1
    imgTxt.write('\n')
imgTxt.close()
frame = frame * 10 + 5
cv2.namedWindow("cap",cv2.WINDOW_NORMAL)
cv2.imshow("cap", frame)
cv2.waitKey(0)
'''




