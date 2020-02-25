import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import re 

# Get Filename
def getFilePath() :
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    return filename

#open File and get its contents split in lists with names and the number of
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
    return dictnames

def makePieChart(dictionary) :
    listnames = []
    values = []
    for key in dictionary:
        listnames.append(key)
    for nummsg in dictionary.values():
        values.append(nummsg)
    
    plt.pie(values, labels=listnames, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.legend(listnames, loc="best")
    plt.show()
    print(listnames)
    print(values)

# heres the main
pathToFile = getFilePath()
makePieChart(getNames(pathToFile))