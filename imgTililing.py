import cv2
import glob
import imgaug as ia
import pybboxes as pbx
from imgaug import augmenters as iaa
import os
ia.seed(1)

height=1080
width=1920

images = []
labels = []
classes =[]
images_path = glob.glob("images/*.jpg")
labels_path = glob.glob("images/*.txt")
image_names_noext = [os.path.splitext(os.path.basename(x))[0] for x in images_path]

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
        labels_in_text.append(pbx.convert_bbox(yolo_bbox,from_type="yolo",to_type="voc",image_size=(width, height)))
        classes_in_text.append(line[0])
    text.close()
    labels.append(labels_in_text)
    classes.append(classes_in_text)

# Input for cropping images
print('enter the crop x percentage: ')
tile_sizex = int(int(input()) * width / 100)
print('enter the crop y percentage: ')
tile_sizey = int(int(input()) * height / 100)

# Cropping images 'left-top', 'left-center', 'left-bottom', 'right-top', 'right-center', 'right-bottom'
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
    cv2.imwrite('tiled_images/{}_cropped_topleft.jpg'.format(image_names_noext[i]), cropped_images_bottomright[i])
    cv2.imwrite('tiled_images/{}_cropped_topright.jpg'.format(image_names_noext[i]), cropped_images_bottomleft[i])
    cv2.imwrite('tiled_images/{}_cropped_bottomleft.jpg'.format(image_names_noext[i]), cropped_images_topright[i])
    cv2.imwrite('tiled_images/{}_cropped_bottomright.jpg'.format(image_names_noext[i]), cropped_images_topleft[i])