import cv2
import numpy as np
import glob
import re

for image in glob.glob('*.jpg'):
    I = cv2.imread(image)
    """
    I_s = np.float32(I)/255.0
    g_x = cv2.Sobel(I_s,cv2.CV_32F,1,0,ksize=1)
    g_y = cv2.Sobel(I_s,cv2.CV_32F,0,1,ksize=1)

    g, arg = cv2.cartToPolar(g_x,g_y,angleInDegrees = True)"""
    X = np.array([])
    y = []
    
    hog = cv2.HOGDescriptor((128,128),(32,32),(16,16),(16,16),9)
    X = np.append(X,hog.compute(I))
    m = re.search('_(\w+)',image)
    if m.group(1)=='pos':
        y.append(1)
    elif m.group(1)=='neg':
        y.append(0)

    print (X)
