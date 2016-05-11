import numpy as np
from PIL import Image
import cv2
from datetime import datetime
np.set_printoptions(threshold='nan')
cap = cv2.VideoCapture('222.avi')
fgbg = cv2.BackgroundSubtractorMOG()
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
    if count >100:
        gray_sum = gray_sum+gray
        tmp = old_frame - frame
        tmp_gray = old_gray - gray
        tmp_gray_sum = tmp_gray_sum+tmp_gray

        tmp_gray_sum = np.uint8(np.clip(tmp_gray_sum,0,255))
        
        if count%1500 == 0 and flag == 0: 
            flag = 1
            cv2.imshow('current',tmp_gray_sum)
            ggggg = np.float64(tmp_gray_sum)
            tmp_min.append(ggggg)
            tmp_gray_sum = 0
            if len(tmp_min) >=2:
                old = np.uint8(np.clip(tmp_min[len(tmp_min)-2],0,255))
                cv2.imshow('old',old)
                pic = tmp_min[len(tmp_min)-1]-tmp_min[len(tmp_min)-2]
                pic = np.uint8(np.clip(pic,0,255))
                cv2.imshow('diff',pic)
                k =  input()
            print 'one pic added'
        if count%1500 != 0 and flag == 1:
            flag = 0

    old_frame = frame
    old_gray = gray
    count+=1
    count_2+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
