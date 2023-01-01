import imgaug.augmenters as iaa
import cv2
import glob
import numpy as np
import imgaug as ia
import pybboxes as pbx
import imgaug.augmenters as iaa
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

# 2. Image Augmentation
aug = iaa.Sequential([
    # 1. Flip
    iaa.Fliplr(0.5),
    iaa.Flipud(0.5),
    # 2. Affine
    iaa.Affine(translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)},
               rotate=(-30, 30),
               scale=(0.5, 1.5)),
    # 3. Multiply
    iaa.Multiply((0.8, 1.2)),
    # 4. Linearcontrast
    iaa.LinearContrast((0.6, 1.4)),
    # Perform methods below only sometimes
    iaa.Sometimes(0.5,
        # 5. GaussianBlur
        iaa.GaussianBlur((0.0, 3.0))
        )
])

# 3. Augment
images_aug = []
labels_aug = []
for i in range(len(images)):
    bbs_list = []
    for j in range(len(labels[i])):
        bbs_list.append(BoundingBox(x1=labels[i][j][0], y1=labels[i][j][1], x2=labels[i][j][2], y2=labels[i][j][3]))
    bbs = BoundingBoxesOnImage(bbs_list, shape=images[i].shape)
    image_aug , bbs_aug = aug(image=images[i], bounding_boxes=bbs)
    images_aug.append(image_aug)
    labels_aug.append(bbs_aug)

# 4. Save Augmented Images
for i in range(len(images_aug)):
    cv2.imwrite("images_aug/{}_aug.jpg".format(i), images_aug[i])
    f = open("images_aug/{}_aug.txt".format(i), "w")
    for j in range(len(labels_aug[i])):
        x1 = labels_aug[i][j].x1
        y1 = labels_aug[i][j].y1
        x2 = labels_aug[i][j].x2
        y2 = labels_aug[i][j].y2
        height=1080
        width=1920
        yolo_bbox = pbx.convert_bbox((x1,y1,x2,y2),from_type="voc",to_type="yolo",image_size=(width, height))
        f.write("{} {} {} {} {}\n".format(classes[i][j], "{:.6f}".format(yolo_bbox[0]), "{:.6f}".format(yolo_bbox[1]), "{:.6f}".format(yolo_bbox[2]), "{:.6f}".format(yolo_bbox[3])))

    