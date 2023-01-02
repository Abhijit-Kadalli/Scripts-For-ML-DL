import glob
import os
from sklearn.model_selection import StratifiedShuffleSplit

def get_label(image_path):
    labels =  []
    label_path = image_path.replace(".jpg", ".txt")
    with open(label_path, "r") as f:
        for line in f:
            line.split(" ")
            labels.append(line)
    return labels

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

current_dir = 'data/obj'

# Load the file paths and labels for the images
image_paths = [image_path for image_path in glob.iglob(os.path.join(current_dir, "*.jpg"))]
labels = [get_label(image_path) for image_path in image_paths]

# Create the stratified shuffle split
splitter = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

# Iterate over the splits
for train_index, test_index in splitter.split(image_paths, [len(l) for l in labels]):
    # Split the data into training and test sets
    X_train, X_test = [image_paths[i] for i in train_index], [image_paths[i] for i in test_index]
    y_train, y_test = [labels[i] for i in train_index], [labels[i] for i in test_index]

# Create and/or truncate train.txt and test.txt
file_train = open('data/train.txt', 'w')
file_test = open('data/test.txt', 'w')

# Write
for image_path in X_train:
    file_train.write(image_path + "\n")
for image_path in X_test:
    file_test.write(image_path + "\n")

# Close
file_train.close() 
file_test.close()