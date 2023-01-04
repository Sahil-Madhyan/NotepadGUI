import tkinter as tk
from tkinter import *
from tkinter import messagebox,filedialog
import os

def createWidgets():

    global textArea
    textArea = Text(root,font="Arial 11")
    textArea.grid(sticky = N+E+S+W)
    menuBar = Menu(root)
    root.config(menu=menuBar)

    #fileMenu

    fileMenu = Menu(menuBar,tearoff=0)
    fileMenu.add_command(label="New",command=newFile)
    fileMenu.add_command(label="Open",command=openFile)
    fileMenu.add_command(label="Save",command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit",command=exit)
    menuBar.add_cascade(label="File",menu=fileMenu)

    #editMenu
    editMenu = Menu(menuBar,tearoff=0)
    editMenu.add_command(label="Cut",command=cut)
    editMenu.add_command(label="Copy",command=copy)
    editMenu.add_command(label="Paste",command=paste)
    menuBar.add_cascade(label="Edit",menu=editMenu)

    #optionsMenu

    optionsMenu = Menu(menuBar,tearoff=0)
    
    #themeMenu

    themeMenu = Menu(optionsMenu,tearoff=0)
    optionsMenu.add_cascade(label="Theme",menu=themeMenu)
    themeMenu.add_command(label="Light Theme",command=lightTheme)
    themeMenu.add_separator()
    themeMenu.add_command(label="Dark Theme",command=darkTheme)
    
    #font Menu

    fontMenu = Menu(optionsMenu,tearoff=0)
    optionsMenu.add_cascade(label="Fonts & FontSize",menu=fontMenu)   
    fontArial = Menu(fontMenu,tearoff=0)
    fontArial.add_command(label="Arial 11",command=arial11Font)
    fontArial.add_command(label="Arial 16",command=arial16Font)
    fontArial.add_command(label="Arial 20",command=arial20Font)
    fontMenu.add_cascade(label="Arial",menu=fontArial)
    fontConsolas = Menu(fontMenu,tearoff=0)
    fontConsolas.add_command(label="Consolas 11",command=consolas11Font)
    fontConsolas.add_command(label="Consolas 16",command=consolas16Font)
    fontConsolas.add_command(label="Consolas 20",command=consolas20Font)
    fontMenu.add_cascade(label="Consolas",menu=fontConsolas)
    menuBar.add_cascade(label="Options",menu=optionsMenu)
    
    #helpMenu

    helpMenu= Menu(menuBar,tearoff=0)
    helpMenu.add_command(label="About Notepad",command=help)
    menuBar.add_cascade(label="Help",menu=helpMenu)
    
def newFile():
    global textArea
    root.title("Untitled - Notepad")
    file = None
    textArea.delete(1.0,END)
    

def openFile():
    global textArea
    file= filedialog.askopenfile(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
    file=file.name
    
    if file =="":
        file = None
    else:
        root.title(os.path.basename(file) + " -Notepad")
        textArea.delete(1.0, END)
        file=open(file, "r")
        textArea.insert(1.0,file.read())
        file.close()



def saveFile():
    global textArea,file
    if file == None:
        file = filedialog.asksaveasfilename(initialfile = "Untitled.txt",defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
        
        if file == "":
            file = None

        else:
            file = open(file,"w")
            file.write(textArea.get(1.0,END))
            file.close()
            file = file.name
            root.title(os.path.basename(file) + " - Notepad")
    
    else:
        file = open(file,"w+")
        file.write(textArea.get(1.0,END))
        file.close()
    
    

def exit():
    root.destroy()
    
    
def cut():
    global textArea
    textArea.event_generate("<<Cut>>")
    
def copy():
    global textArea
    textArea.event_generate("<<Copy>>")


def paste():
    global textArea
    textArea.event_generate("<<Paste>>")

def lightTheme():
    main_color = "#FFFFFF"
    textArea.config(bg=main_color,fg="#000000",insertbackground="#000000")

def darkTheme():
    main_color = "#373737"
    textArea.config(bg=main_color,fg="#FFFFFF",insertbackground="#FFFFFF")

def arial11Font():
    textArea.config(font="Arial 11") 

def arial16Font():
    textArea.config(font="Arial 16") 

def arial20Font():
    textArea.config(font="Arial 20") 

def consolas11Font():
    textArea.config(font="Consolas 11")

def consolas16Font():
    textArea.config(font="Consolas 16") 

def consolas20Font():
    textArea.config(font="Consolas 20")
     


def help():

    messagebox.showinfo("Notepad","Notepad Using tkinter\nThis sample of Notepad is developed by Shalini , Sahil and Siddhant")



root = tk.Tk()
root.title("Untitled - Notepad")
#root.wm_iconbitmap("notepadico.ico")
icon = PhotoImage(master=root, file='notepad.png')
root.wm_iconphoto(True, icon)
file = None
createWidgets()
root.mainloop()
