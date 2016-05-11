import numpy as np
from PIL import Image
import cv2
#from matplotlib import pyplot as plt
from datetime import datetime
np.set_printoptions(threshold='nan')
cap = cv2.VideoCapture('111.avi')
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
    if count >300:
        gray_sum = gray_sum+gray
        tmp = old_frame - frame
        tmp_gray = old_gray - gray
        tmp_gray_sum = tmp_gray_sum+tmp_gray

            
      #  print count_2
        
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
            gray_sum = 0
            count_2 = 0
            x = 0            
            print '1 pic added'
        if count%1500 != 0 and flag == 1:
            flag = 0
            
      #  if count>5000:
        tmp_gray_sum = np.uint8(np.clip(tmp_gray_sum,0,255))
        '''
        if count%1500 == 0 and flag == 0: 
            flag = 1
            cv2.imshow('cap!',tmp_gray_sum)
            ggggg = np.float64(tmp_gray_sum)
            tmp_min.append(ggggg)
            tmp_gray_sum = 0
            if len(tmp_min) >=2:
                pic = tmp_min[len(tmp_min)-1]-tmp_min[len(tmp_min)-2]
                pic = np.uint8(np.clip(pic,0,255))
                cv2.imshow('diff',pic)
                #cv2.imshow('origin',tmp_min[len(tmp_min)-3])
                #cv2.imshow('new',tmp_min[len(tmp_min)-1])
            print 'one pic added'
        if count%1500 != 0 and flag == 1:
            flag = 0
        '''
        cv2.imshow('frame__',tmp_gray_sum)
       # cv2.imshow('frame',tmp_gray)
        tmp_gray = np.uint8(np.clip(tmp_gray,0,255))
        
    old_frame = frame
    old_gray = gray
    '''
    if count>5000:
        for i in range(0,len(gray_min)):
            pic = np.uint8(gray_min[i])
            cv2.imshow('pic',pic)
            if i>=1:
                diff = gray_min[i] - gray_min[i-1]
                diff = np.uint8(diff)
                cv2.imshow('diff',diff)
                k=input()
    '''
    '''
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.float64(gray)
    noise = np.random.randn(*gray.shape)*10
    noisy = gray+noise
    noisy = np.uint8(np.clip(noisy,0,255))
    dst = cv2.fastNlMeansDenoisingMulti(noisy, 2, 5, None, 4, 7, 35)
    plt.subplot(131),plt.imshow(gray,'gray')
    plt.subplot(132),plt.imshow(noisy,'gray')
    plt.subplot(133),plt.imshow(dst,'gray')
    plt.show()
    '''
   # if count >1500:
     #   fgmask = fgbg.apply(frame)
   #     cv2.imshow('frame',fgmask)
       # print fgmask
      #  tmp += fgmask
       # k=input()
      #  if count >100:
      #      tmp_ = tmp/(count-50)
            #print tmp_
     #       img = Image.fromarray(tmp_, 'L')
      #      img.save('my.png')
     #       image = cv2.imread('my.png',0)
     #       cv2.imshow('tmp',image)
      #      k=input()
    '''
    if count%100 == 0:
        calibrate = gray
    #    print calibrate[100]
     #   k=input()
        cv2.imshow('calibrate',calibrate)
    if count == 100:        
        cv2.imshow('calibrate',calibrate)


   # print gray
    rows, cols = gray.shape

    cv2.imshow('Origin',gray)
    
    if count>100: 
        diff = gray - calibrate 
        diff_old = diff  
      #  k=input()
        cv2.imshow('diff',diff)
    '''
    count+=1
    count_2+=1
 #   print count
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
