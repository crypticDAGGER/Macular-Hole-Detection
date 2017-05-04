import cv2
import re
import glob

coords=[] #List to store coordinates of cropped region

def crop_image(event,x,y,flags,param):
    global coords
    
    if event==cv2.EVENT_LBUTTONDOWN: #If LMB is clicked, stores starting coordinates
        coords=[(x,y)]

    elif event==cv2.EVENT_LBUTTONUP: #If LMB is released, stores ending coordinates
        coords.append((x,y))
        cv2.rectangle(img,coords[0],coords[1],(255,0,0),2) #Draws rectangle around ROI
        cv2.imshow("Image",img)
        
for image in glob.glob("*.jpg"): #Iterates through all JPEG images in working directory
    
    while(1): #Loops until 'c' is pressed.Crops image if 'c' is pressed else resets image
        img=cv2.imread(image)
        img_copy=img.copy()
        cv2.namedWindow("Image")
        cv2.setMouseCallback("Image",crop_image)
        cv2.imshow("Image",img)
        key=cv2.waitKey(0) & 0xFF
        if key==ord("c"):
            break
        else:
            continue

    crop_img=img_copy[coords[0][1]:coords[1][1],coords[0][0]:coords[1][0]] #Crops within the coordinates
   
    m=re.search('(.+?).jpg',image)
    if m:
        resize_img=cv2.resize(crop_img,(128,128)) #Resizes the cropped image
        cv2.imshow("Cropped Image",crop_img)
        cv2.imwrite(m.group(1)+"-crop.jpg",resize_img) #Writes resized image to working directory
   
    key=cv2.waitKey(0) & 0xFF
    if key==(27):
        cv2.destroyAllWindows() #Closes all windows 
