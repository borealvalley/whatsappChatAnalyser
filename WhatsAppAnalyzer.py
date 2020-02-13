from tkinter import Tk
from tkinter.filedialog import askopenfilename
import re 

# Get Filename
def getFilePath() :
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    return filename

#open File and get its contents split in lists
def getNames(Path) :
    file = open(Path, "r", encoding="utf8")
    for line in file:
        names = re.search(r"-(\s.*):\s", line)
        print(names)
        


pathToFile= getFilePath()
getNames(pathToFile)