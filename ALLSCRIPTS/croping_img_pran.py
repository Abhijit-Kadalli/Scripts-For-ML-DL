from PIL import Image
import glob
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = os.path.join(current_dir, "images")
print("Enter the object ID you want to crop", 
"0 Housekeeping Staff",
"1 Employee",
"2 Mop",
"3 Cleaning Cloth",
"4 Bin",
"5 Gloves",
"6 Mask",
"7 Trash Bag",
"8 ppekitstaff",sep='\n')

object_id = int(input())

labels_of_cropimg_path = []
labels_path = glob.glob(os.path.join(current_dir, "*.txt"))
count = 0
cropped_imgs = []
for label_path in labels_path:
    text = open(label_path,"r") 
    new_cords_list = []
    for line in text:
        line = line.split()
        Id = int(line[0])
        a = float(line[1])
        b = float(line[2])
        c = float(line[3])
        d = float(line[4])
        if Id == object_id:
            image_path = label_path.replace("txt","jpg")
            image_name = os.path.splitext(os.path.basename(image_path))[0]
            im = Image.open(image_path)
            image_width, image_height = im.size
            x = 320/image_height
            y = 320/image_width
            left = (a - y) * image_width
            upper = (b - x) * image_height
            right = (a + y) * image_width
            lower = (b + x) * image_height
            im_cropped = im.crop((left, upper, right, lower))
            cropped_imgs.append(im_cropped)
            count += 1
            im_cropped.save(f"resized_images/{image_name}_resized_{count}.jpg")
            label = open(label_path, "r")
            for line in label:
                line = line.split()
                all_id = int(line[0])
                a = float(line[1])
                b = float(line[2])
                c = float(line[3])
                d = float(line[4])
                new_image_width, new_image_height = im_cropped.size
                new_a = ((a * image_width) - left) / new_image_width
                new_b = ((b * image_height) - upper) / new_image_height
                new_c = c * image_width / new_image_width
                new_d = d * image_height / new_image_height
                new_cords = [new_a, new_b, new_c, new_d] 
                for i in range(len(new_cords)-2):
                    if new_cords[i+2] < 0:
                        new_cords[i+2] = 0
                    if new_cords[i+2] > 1:
                        new_cords[i+2] = 1
                if new_cords[0] > 0.1 and new_cords[1] > 0.1 and new_cords[0]<0.9 and new_cords[1]<0.9:
                    new_cords_list.append(" ".join([str(all_id)] + [str(coord) for coord in new_cords]))
                with open(f'resized_images//{image_name}_resized_{count}.txt', 'w') as file:
                    file.write("\n".join(new_cords_list))
            label.close()