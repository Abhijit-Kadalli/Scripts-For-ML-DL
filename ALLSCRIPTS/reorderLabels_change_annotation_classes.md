# Class Label Converter

A script to convert the class labels in annotation files from one set of classes to another.

## Requirements
- Python 3
- easygui library

You can install easygui using this command `pip install easygui`

## Usage

1. Run the script by typing `python class_label_converter.py` on your command prompt/terminal.
2. User will be prompted to provide the path of annotation files, current class labels and required class labels.
3. Once all the path are provided, script will automatically convert the class labels in all the annotation files from the current class labels to the required class labels.

## Description

This script performs the following actions:

- Reads the current class labels from the provided file and stores them in the list `availableClasses`.
- Reads the desired class labels from the provided file and stores them in the list `classesRequired`.
- Creates two dictionaries, `dictofClasses` and `dictofneededClasses`, which map the class labels to their corresponding index in the `availableClasses` and `classesRequired` lists respectively.
Iterates through all the annotation files in the provided directory and reads their contents into a list `file_data`.
- Replaces the class label in each line of the `file_data` list with the corresponding label from the `classesRequired` list, using the mapping stored in the dictionaries.
- Writes the modified `file_data` list back to the original annotation files.