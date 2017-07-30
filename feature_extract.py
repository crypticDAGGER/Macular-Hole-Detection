import cv2
import numpy as np
import glob

for image in glob.glob('*.jpg'):
    I = cv2.imread(image)
    """
    I_s = np.float32(I)/255.0
    g_x = cv2.Sobel(I_s,cv2.CV_32F,1,0,ksize=1)
    g_y = cv2.Sobel(I_s,cv2.CV_32F,0,1,ksize=1)

    g, arg = cv2.cartToPolar(g_x,g_y,angleInDegrees = True)"""
    
    hog = cv2.HOGDescriptor((128,128),(32,32),(16,16),(16,16),9)
    descriptor = hog.compute(I)
