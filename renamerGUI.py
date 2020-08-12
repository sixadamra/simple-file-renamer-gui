import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
import os

#This function renames ALL files that have any
#of the selected options in their name,
#so please be careful with files that you
#don't want to be auotmatically renamed.
def renameFiles():
    for files in os.listdir():
        file_name = str(files)
        print (file_name)
        if (hyphenCheckState.get() == True):  
            file_name = re.sub("-", " ", file_name)
        if (underscoreCheckState.get() == True):
            file_name = re.sub("_", " ", file_name)
        if (tbsCheckState.get() == True):
            file_name = re.sub("   ", " ", file_name)
        print (file_name)
        os.rename(files, file_name)
        

def getCWD():
    cwd=fd.askdirectory()
    name.set(cwd)
    os.chdir(cwd)

#App is the main window
app = tk.Tk()
app.title("Renamer GUI Alpha 1.0")
app.minsize(325,75)
app.maxsize(325,75)


#frame is the main container inside the window
ContainerFrame = tk.Frame(app, bg="#ADD8E6")
ContainerFrame.grid()

#Center Container
CenterFrame = tk.Frame(ContainerFrame, bg="white")
CenterFrame.grid(sticky=W)

#Frame containing the directory text and button
DirectoryFrame = tk.Frame(CenterFrame, bg="white")
DirectoryFrame.grid(sticky=W)

name = StringVar()
name.set("Select directory")
directoryName = Entry(DirectoryFrame, width=20, textvariable=name)
directoryName.grid(column = 0, row = 1)

button = Button(DirectoryFrame, text="Open File Directory", command=getCWD)
button.grid(column = 1, row = 1)

#Frame containing the radio box options
OptionsFrame = tk.Frame(CenterFrame, bg="white")
OptionsFrame.grid(sticky=W)

hyphenCheckState = BooleanVar()
hyphenCheckButton = Checkbutton(OptionsFrame, text="Remove -", bg="white", variable=hyphenCheckState)
hyphenCheckButton.grid(column=0, row=1)

underscoreCheckState = BooleanVar()
underScoreCheckButton = Checkbutton(OptionsFrame, text="Remove _", bg="white", variable=underscoreCheckState)
underScoreCheckButton.grid(column=1, row=1)

tbsCheckState = BooleanVar()
tripleBlankSpaceCheckButton = Checkbutton(OptionsFrame, text="Remove triple blank spaces", bg="white", variable=tbsCheckState)
tripleBlankSpaceCheckButton.grid(column=2, row=1)

#Frame containing the Rename Files button
RenameFrame = tk.Frame(CenterFrame, bg="white")
RenameFrame.grid(sticky=E)

renameButton = Button(RenameFrame, text="Rename files", command=renameFiles)
renameButton.grid(column=0, row=1)

app.mainloop()