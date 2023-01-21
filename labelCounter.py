import glob
import os

labels_count_test =[]
labels_count_val = []

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

current_dir = 'train'

# Directory where the data will reside
for label_path in glob.iglob(os.path.join(current_dir, "*.txt")):
    with open(label_path, "r") as f:
        for line in f:
            line.split(" ")
            labels_count_test[int(line[0])] += 1

current_dir = 'val'
for label_path in glob.iglob(os.path.join(current_dir, "*.txt")):
    with open(label_path, "r") as f:
        for line in f:
            line.split(" ")
            labels_count_val[int(line[0])] += 1

# display the label count
print(labels_count_test)
print(labels_count_val)