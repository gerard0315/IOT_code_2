import numpy as np
from PIL import Image
import cv2
from datetime import datetime
np.set_printoptions(threshold='nan')
cap = cv2.VideoCapture('333.avi')
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
accumulated=0
tmp_gray_sum_old = 0
while(cap.isOpened()):
    t= datetime.now()
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.float64(gray)
    if count >300:
        gray_sum = gray_sum+gray
        tmp = old_frame - frame
        tmp_gray = old_gray - gray
        tmp_gray_sum = tmp_gray_sum+tmp_gray
        accumulated =  accumulated + tmp_gray_sum_old - tmp_gray_sum
        accumulated =  np.uint8(np.clip(accumulated,0,255))
        tmp_gray_sum = np.uint8(np.clip(tmp_gray_sum,0,255))
        tmp_gray_sum_old = tmp_gray_sum
        cv2.imshow('accumulated',accumulated)
        cv2.imshow('tmp_gray_sum',tmp_gray_sum)

    old_frame = frame
    old_gray = gray
    count+=1
    count_2+=1
 #   print count
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
