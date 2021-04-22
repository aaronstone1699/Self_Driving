import tenso
import tensorflow as tf
from tensorflow.keras.layers import Input, Reshape, Dropout, Dense 
from tensorflow.keras.layers import Flatten, BatchNormalization
from tensorflow.keras.layers import Activation, ZeroPadding2D
from tensorflow.keras.layers import LeakyReLU,Concatenate,concatenate
from tensorflow.keras.layers import UpSampling2D, Conv2D,Conv2DTranspose,MaxPooling2D
from tensorflow.keras.models import Sequential, Model, load_model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import LeakyReLU,Add
import tensorflow
import cv2
import numpy as np
from PIL import Image
import os 
import time
import matplotlib.pyplot as plt
from tensorflow.keras.utils import plot_model

driver = serial.Serial('COM5',9600,timeout=1)

step =  {"f":[b'f',b's'],"b":[b'b',b's'],"l":[b'r',b's'],"r":[b'l',b's']}
st = ['f','b','l','r']
status = True
segnet = tenso.use_model(tenso.seg_model((256,256,3)),"/home/pi/Desktop/sdcar/segnet.h5")
vid_feed = cv2.VideoCapture(0)

while(True):

    _, frame = vid_feed.read()
    frame = cv2.rotate(frame,cv2.ROTATE_180)
    pred_frame = tenso.predict(segnet,frame)
  
    print('ready')
    x = list(map(str,input().split()))
    inp = [0,0,0,0]
    
    for i in x:
        if(i!='stop'):
            driver.write(step[i][0])
            time.sleep(0.25)
            driver.write(step[i][1])
            time.sleep(0.25)
            
            ino = driver.readline().decode('utf-8')[0:2]
            if(len(ino)>0):
                inp[0] = ino[0]
                inp[1] = ino[1]
                inp[2] = st.index(i)
                print(inp)
                inp[3] = pred_frame
                cv2.imshow('frame', frame)
                cv2.imshow('pred_frame', pred_frame)    
                if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            status = False
            break

    if(status == False):
        break

    
  
print("GoodBye")
driver.close()
vid_feed.release()

cv2.destroyAllWindows()
