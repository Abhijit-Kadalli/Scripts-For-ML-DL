# annotation_class_converter
This script is used to filter the annotation files in a given directory based on a set of selected classes.

## Requirements
- Python 3.x
- easygui library (can be installed using pip install easygui)
## Usage
1. Run the script.
2. Select the directory containing the annotation files that need to be filtered.
3. Select the classes file that contains all the available classes.
4. Select the classes that you want to keep from the available classes.
5. The script will then filter the annotation files in the selected directory and keep only the annotations that correspond to the selected classes.
## Note
- The script currently only works with text files that have the '.txt' file extension.
- The script assumes that the annotation files have the format of one annotation per line, with the class label as the first element and the rest of the elements being the annotation coordinates.
- The script also assumes that the class labels are integers and the classes file is a plain text file with one class per line.

## EXAMPLE

### Annotation file before running the script:

``` 0 50 100 150 200    ```
``` 1 75 125 175 225    ```
``` 2 100 150 200 250   ```
``` 3 125 175 225 275   ```

### Classes file:

``` class1```
``` class2```
``` class3```
``` class4```

### If the user selects to keep classes 1 and 3, the annotation file after running the script:

``` 0 50 100 150 200    ```
``` 2 100 150 200 250   ```
