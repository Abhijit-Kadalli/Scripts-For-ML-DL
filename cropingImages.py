import imgaug.augmenters as iaa
import cv2
import glob
import numpy as np
import imgaug as ia
import pybboxes as pbx
import imgaug.augmenters as iaa
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage

ia.seed(1)
IMAGE_HEIGHT = 1080
IMAGE_WIDTH = 1920

print(
    "Enter the object ID you want to crop", "0 Housekeeping Staff",
"1 Employee",
"2 Mop",
"3 Cleaning Cloth",
"4 Bin",
"5 Gloves",
"6 Mask",
"7 Trash Bag",
"8 ppekitstaff")
object_id=int(input())

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
        classes_in_text.append(line)
    text.close()
    labels.append(labels_in_text)
    classes.append(classes_in_text)

for i in range(len(images)):
    bbs_list = []
    for j in range(len(labels[i])):
        bbs_list.append(BoundingBox(x1=labels[i][j][0], y1=labels[i][j][1], x2=labels[i][j][2], y2=labels[i][j][3]))
    for j in range(len(classes[i])):
        if int(classes[i][j][0]) == object_id:
            x = float(classes[i][j][1])
            y = float(classes[i][j][2])
            w = float(classes[i][j][3])
            h = float(classes[i][j][4])
            x_min = int(x * IMAGE_WIDTH)
            y_min = int(y * IMAGE_HEIGHT)
            x_max = int((x + w) * IMAGE_WIDTH)
            y_max = int((y + h) * IMAGE_HEIGHT)
            center_x = int((x_min + x_max) / 2)
            center_y = int((y_min + y_max) / 2)
            # Define the cropping limits
            left = int(center_x - 320)
            top = int(center_y - 320)
            right = int(center_x + 320)
            bottom = int(center_y + 320)

            # Ensure cropping limits are inside the image
            left = max(left, 0)
            top = max(top, 0)
            right = min(right, IMAGE_WIDTH)
            bottom = min(bottom, IMAGE_HEIGHT)
            aug = iaa.Sequential([
                iaa.Crop(px=(left, top, right, bottom))
            ]) 
            bbs = BoundingBoxesOnImage(bbs_list, shape=images[i].shape)
            image_cropped , bbs_aug = aug(image=images[i], bounding_boxes=bbs)
            cv2.imwrite("images_cropped/{}_aug.jpg".format(i), image_cropped)
            f = open("images_cropped/{}_aug.txt".format(i), "w")
            for k in range(len(bbs_aug)):
                x1 = bbs_aug[k].x1
                y1 = bbs_aug[k].y1
                x2 = bbs_aug[k].x2
                y2 = bbs_aug[k].y2
                height=1080
                width=1920
                yolo_bbox = pbx.convert_bbox((x1,y1,x2,y2),from_type="voc",to_type="yolo",image_size=(width, height))
                f.write("{} {} {} {} {}\n".format(classes[i][k][0], "{:.6f}".format(yolo_bbox[0]), "{:.6f}".format(yolo_bbox[1]), "{:.6f}".format(yolo_bbox[2]), "{:.6f}".format(yolo_bbox[3])))
            f.close()