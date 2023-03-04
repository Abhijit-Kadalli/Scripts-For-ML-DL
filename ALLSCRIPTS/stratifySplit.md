# Image Splitter
This script is used to split a dataset of images into training and test sets, and then copy the images and their corresponding labels to the corresponding train and test folders.

## Dependencies
* glob
* os
* shutil
* sklearn

## Usage
1. Make sure your images and their corresponding labels are stored in the same directory, and that the labels are in a .txt file with the same name as the corresponding image (e.g. image1.jpg and image1.txt).
2. Update the `current_dir` variable to point to the directory where your images and labels are stored.
3. Run the script. The script will create a stratified shuffle split of the data, with 80% of the data going to the train folder and 20% going to the test folder.
4. The script will then copy the images and their corresponding labels to the train and test folders respectively.
