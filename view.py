from tkinter import *
from tkinter import ttk
import controller


def PrintBox():

    root = Tk()
    
    root.geometry('400x400')
    root.title("Контакты")
    

    controller.ViewContact()

    add = ttk.Button(root, text="Экспорт(Xml)",padding=10, command=controller.expXml)
    search = ttk.Button(root, text="Экспорт(Html)",padding=10, command=controller.exp)

    add.pack(anchor="w", fill=X)
    search.pack(anchor="w", fill=X)
    
    root.mainloop()