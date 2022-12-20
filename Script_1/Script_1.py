import easygui as eg
eg.msgbox("Enter the path of the current Annotation file","Script 1","Next")
path_annotation = eg.fileopenbox()
eg.msgbox("Enter the path of the current Classes file","Script 1","Next")
path_classesCurrent = eg.fileopenbox()

def main():
    pass

if __name__ == '__main__':
    main()