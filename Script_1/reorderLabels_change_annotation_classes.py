import easygui as eg
import os
availableClasses = []
classesRequired = []
dictofClasses = {}
dictofneededClasses = {}
file = []

def fill_files(path):
    files = []
    for i in os.listdir(path):
        if i.endswith('.txt'):
            files.append(i)
    return files

def get_key(val,dictofneededClasses):
    for key, value in dictofneededClasses.items():
        if val == value:
            return key
                

def main():
    eg.msgbox("Enter the path of the current Annotation file","Script 2","Next")
    path_annotation = eg.diropenbox()
    eg.msgbox("Enter the path of the current Classes file","Script 2","Next")
    path_classesCurrent = eg.fileopenbox()
    
    classes = open(path_classesCurrent,"r")
    
    for line in classes:
        availableClasses.append(line[:-1])
    classes.close()
    
    eg.msgbox("Select the classes you want to convert to","Script 2","Next")
    path_classesRequired = eg.fileopenbox()

    classes = open(path_classesRequired,"r")

    for line in classes:
        classesRequired.append(line[:-1])
    classes.close()

    dictofClasses = dict(enumerate(availableClasses))
    dictofneededClasses = dict(enumerate(classesRequired))
    file = fill_files(path_annotation)
    
    for item in file:
        file_data = []
        with open(path_annotation +"\\" + item, 'r') as myfile:
            for line in myfile:
                currentLine = line[:-1]
                data = currentLine.split(" ")
                file_data.append(data)

        f = open(path_annotation +"\\"+item, 'w')
        for i in file_data:
            res  = ""
            if dictofClasses.get(int(i[0])) in classesRequired:
                i[0] = str(get_key(dictofClasses.get(int(i[0])),dictofneededClasses))
                #i[0] = str(dictofneededClasses.get(dictofClasses.get(int(i[0]))))
                for j in i:
                    res += j + " "
                print(res)
                f.write(res)
                f.write("\n")
        f.close()

if __name__ == '__main__':
    main()