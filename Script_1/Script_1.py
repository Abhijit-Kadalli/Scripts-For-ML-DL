import easygui as eg
import os
availableClasses = []
classesRequired = []
dictofClasses = {}
file = []

def fill_files(path):
    files = []
    for i in os.listdir(path):
        if i.endswith('.txt'):
            files.append(i)
    return files

def main():
    eg.msgbox("Enter the path of the current Annotation file","Script 1","Next")
    path_annotation = eg.diropenbox()
    eg.msgbox("Enter the path of the current Classes file","Script 1","Next")
    path_classesCurrent = eg.fileopenbox()
    classes = open(path_classesCurrent,"r")
    for line in classes:
        availableClasses.append(line[:-1])
    classes.close()
    classesRequired = eg.multchoicebox("Select the classes you want to Keep","Script 1",availableClasses)
    dictofClasses = dict(enumerate(availableClasses))
    
    file = fill_files(path_annotation)
    print(classesRequired,dictofClasses,file)


if __name__ == '__main__':
    main()