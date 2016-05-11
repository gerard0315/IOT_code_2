import numpy as np
from PIL import Image
import cv2
#from matplotlib import pyplot as plt
from datetime import datetime
np.set_printoptions(threshold='nan')
cap = cv2.VideoCapture('333.avi')
fgbg = cv2.BackgroundSubtractorMOG()
#tmp = np.zeros(shape=(720,1280),dtype=np.int)
count = 0
diff = 0
tmp_gray_sum = 0
gray_sum = 0
gray_min=[]
tmp_min = []
flag = 0
count_2 = 1
x = 1500
ggggg=0
gen_mask=1
while(cap.isOpened()):
    t= datetime.now()
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.float64(gray)
    if count >1500:
        gray_sum = gray_sum+gray
      #  tmp = old_frame - frame
      #  tmp_gray = old_gray - gray
      #  tmp_gray_sum = tmp_gray_sum+tmp_gray
        if count%1500 == 0 and flag == 0: 
            flag = 1
            gray_sum = gray_sum/count_2
            gray_min.append(gray_sum)
            gray_sum = np.uint8(np.clip(gray_sum,0,255))
            cv2.imshow('origin',gray_sum)
            pic = np.uint8(gray_min[len(gray_min)-1])
            cv2.imshow('pic',pic)
            if len(gray_min)>=3:
                pic = np.uint8(gray_min[len(gray_min)-2])
                cv2.imshow('pic_old',pic)
                diff = gray_min[len(gray_min)-1] - gray_min[len(gray_min)-3]
                diff = np.uint8(np.clip(diff,0,255))
                cv2.imshow('diff',diff)
                k = input()
            gray_sum = 0
            count_2 = 0
            x = 0            
            print '1 pic added'
        if count%1500 != 0 and flag == 1:
            flag = 0
            
      #  if count>5000:
      #  tmp_gray_sum = np.uint8(np.clip(tmp_gray_sum,0,255))
       # cv2.imshow('frame__',tmp_gray_sum)
       # cv2.imshow('frame',tmp_gray)
        #tmp_gray = np.uint8(np.clip(tmp_gray,0,255))
        count_2+=1        
   # old_frame = frame
    #old_gray = gray

    count+=1

 #   print count
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
