import cv2
import glob
import numpy as np
import imgaug as ia
import pybboxes as pbx
from imgaug import augmenters as iaa
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage

ia.seed(1)

# 1. Load Dataset
images = []
labels = []
classes =[]
images_path = glob.glob("images/*.jpg")
labels_path = glob.glob("images/*.txt")
for img_path in images_path:
    img = cv2.imread(img_path)
    images.append(img)
for label_path in labels_path:
    labels_in_text=[]
    classes_in_text=[]
    text= open(label_path,"r") 
    for line in text:
        line=line.split()
        a=float(line[1])
        b=float(line[2])
        c=float(line[3])
        d=float(line[4])
        yolo_bbox = (a,b,c,d)
        height=1080
        width=1920
        labels_in_text.append(pbx.convert_bbox(yolo_bbox,from_type="yolo",to_type="voc",image_size=(width, height)))
        classes_in_text.append(line[0])
    text.close()
    labels.append(labels_in_text)
    classes.append(classes_in_text)

# Input for cropping images
print('enter the crop x percentage: ')
tile_sizex = int(input()) * 1920 / 100
print('enter the crop y percentage: ')
tile_sizey = int(input()) * 1080 / 100

# Cropping images 'uniform', 'normal', 'center', 'left-top', 'left-center', 'left-bottom', 'center-top', 'center-center', 'center-bottom', 'right-top', 'right-center', 'right-bottom'
cropper_topleft     = iaa.CropToFixedSize(width=tile_sizex, height=tile_sizey, position="left-top")
cropper_topright    = iaa.CropToFixedSize(width=tile_sizex, height=tile_sizey, position="right-top")
cropper_bottomleft  = iaa.CropToFixedSize(width=tile_sizex, height=tile_sizey, position="left-bottom")
cropper_bottomright = iaa.CropToFixedSize(width=tile_sizex, height=tile_sizey, position="right-bottom")



cropped_images_topleft = cropper_topleft(images= images)
cropped_images_topright = cropper_topright(images= images)
cropped_images_bottomleft = cropper_bottomleft(images= images)
cropped_images_bottomright = cropper_bottomright(images= images)

# saving cropped images
for i in range(len(cropped_images_topleft)):
    cv2.imwrite('tiled_images/{}_cropped_topleft.jpg'.format(i), cropped_images_topleft[i])
    cv2.imwrite('tiled_images/{}_cropped_topright.jpg'.format(i), cropped_images_topright[i])
    cv2.imwrite('tiled_images/{}_cropped_bottomleft.jpg'.format(i), cropped_images_bottomleft[i])
    cv2.imwrite('tiled_images/{}_cropped_bottomright.jpg'.format(i), cropped_images_bottomright[i])

