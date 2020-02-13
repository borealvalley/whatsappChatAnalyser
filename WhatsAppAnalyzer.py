from tkinter import Tk
from tkinter.filedialog import askopenfilename
import re 

# Get Filename
def getFilePath() :
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    return filename

#open File and get its contents split in lists
def getNames(path) :
    file = open(path, "r", encoding="utf8")
    dictnames = {} 
    for line in file:
        names = re.search(r"-(\s[A-z]+)+:\s", line)
        if names : 
            name = names.group(0)
            name = name[2:-2]
            if name in dictnames:
                dictnames[name] = dictnames[name] + 1
            else:
                dictnames[name] = 1
            
    print(dictnames)

pathToFile = getFilePath()
getNames(pathToFile)