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
                for j in i:
                    res += j + " "
                print(res)
                f.write(res)
                f.write("\n")
        f.close()

if __name__ == '__main__':
    main()