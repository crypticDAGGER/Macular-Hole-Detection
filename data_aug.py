import cv2
import numpy as np
import glob
from imgaug import augmenters as iaa

img_count=len(list(glob.iglob("*.jpg",recursive=True)))

images=np.empty(img_count,dtype=object)
images=[cv2.imread(file) for file in glob.glob("*.jpg")]

seq=iaa.Sequential([
    iaa.GaussianBlur(sigma=(0,3.0)),
    iaa.Invert(0),


    ])

for batch_id in range(img_count):
    img_aug=seq.augment_images(images[batch_id])

cv2.imwrite("trial.jpg",img_aug)
