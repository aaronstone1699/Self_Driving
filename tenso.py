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

def seg_model(shape):
    input = Input(shape)
    seg1 = Conv2D(16,(4,4),strides=(1,1),padding='same',activation='relu')(input)
    m1 = MaxPooling2D((2,2))(seg1)
    seg2 = Conv2D(16,(4,4),strides=(1,1),padding='same',activation='relu')(m1)
    m2 = MaxPooling2D((2,2))(seg2)
    seg3 = Conv2D(32,(4,4),strides=(1,1),padding='same',activation='relu')(m2)
    m3 = MaxPooling2D((2,2))(seg3)
    seg4 = Conv2D(32,(4,4),strides=(1,1),padding='same',activation='relu')(m3)
    m4 = MaxPooling2D((2,2))(seg4)
    seg5 = Conv2D(64,(4,4),strides=(1,1),padding='same',activation='relu')(m4)
    m5 = MaxPooling2D((2,2))(seg5)
    seg6 = Conv2D(64,(4,4),strides=(1,1),padding='same',activation='relu')(m5)
    m6 = MaxPooling2D((2,2))(seg6)
    seg7 = Conv2D(128,(4,4),strides=(1,1),padding='same',activation='relu')(m6)
    m7 = MaxPooling2D((2,2))(seg7)
    seg8 = Conv2D(128,(4,4),strides=(1,1),padding='same',activation='relu')(m7)

    deg1 = Conv2DTranspose(128,(4,4),strides=(2,2),padding='same',activation='relu')(seg8)
    deg1 = concatenate([deg1,seg7],axis=3)
    deg1 = Conv2DTranspose(64,(4,4),strides=(2,2),padding='same',activation='relu')(deg1)
    deg1 = concatenate([deg1,seg6],axis=3)
    deg1 = Conv2DTranspose(64,(4,4),strides=(2,2),padding='same',activation='relu')(deg1)
    deg1 = concatenate([deg1,seg5],axis=3)
    deg1 = Conv2DTranspose(32,(4,4),strides=(2,2),padding='same',activation='relu')(deg1)
    deg1 = concatenate([deg1,seg4],axis=3)
    deg1 = Conv2DTranspose(32,(4,4),strides=(2,2),padding='same',activation='relu')(deg1)
    deg1 = concatenate([deg1,seg3],axis=3)
    deg1 = Conv2DTranspose(16,(4,4),strides=(2,2),padding='same',activation='relu')(deg1)
    deg1 = concatenate([deg1,seg2],axis=3)
    deg1 = Conv2DTranspose(16,(4,4),strides=(2,2),padding='same',activation='relu')(deg1)
    deg1 = concatenate([deg1,seg1],axis=3)
    deg1 = Conv2DTranspose(3,(4,4),strides=(1,1),padding='same',activation='relu')(deg1)
    model = Model(input,deg1)
    return(model)

def use_model(model,weights):
    model.compile(Adam(0.0003),loss='binary_crossentropy',metrics=['acc'])
    model.load_weights(weights)
    return(model)

def predict(model,img):
    image = cv2.resize(img,(256,256))/255
    pred_image = model.predict(image.reshape(-1,256,256,3)).reshape(256,256,3)
    return(pred_image)






