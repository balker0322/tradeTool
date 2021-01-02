from tkinter import *
from tkinter.ttk import Frame, Label, Entry

class slider_input():

    def __init__(self, master, label = "No label", label_width = 15):
        self.master = master
        self.label = label
        self.label_width = label_width
        self.var = DoubleVar()
        self.initUI()

    def initUI(self):
        self.frame1 = Frame(self.master)
        frame1 = self.frame1
        frame1.pack(fill=X)

        self.lbl1 = Label(frame1, text=self.label, width=self.label_width)
        lbl1 = self.lbl1
        lbl1.pack(side=LEFT, padx=5, pady=5)

        self.scale = Scale( frame1, variable = self.var, orient = HORIZONTAL)
        scale = self.scale
        scale.pack(fill=X, anchor = CENTER)

        
class drop_down():

    def __init__(self, master, options : list, label = "No label", label_width = 15):
        self.master = master
        self.label = label
        self.label_width = label_width
        self.var = StringVar()
        self.options = options
        self.initUI()

    def initUI(self):
        self.frame = Frame(self.master)
        frame = self.frame
        frame.pack(fill=X)

        self.lbl = Label(frame, text=self.label, width=self.label_width)
        lbl = self.lbl
        lbl.pack(side=LEFT, padx=5, pady=5)

        OPTIONS = self.options

        self.var.set(OPTIONS[0]) # default value

        self.entry = OptionMenu(frame, self.var, *OPTIONS)
        entry = self.entry
        entry.pack(fill=X, padx=5, expand=True)

        
class entry():

    def __init__(self, master, label = "No label", label_width = 15):
        self.master = master
        self.label = label
        self.label_width = label_width
        self.var = StringVar()
        self.initUI()

    def initUI(self):
        self.frame = Frame(self.master)
        frame = self.frame
        frame.pack(fill=X)

        self.lbl = Label(frame, text=self.label, width=self.label_width)
        lbl = self.lbl
        lbl.pack(side=LEFT, padx=5, pady=5)
 
        self.entry = Entry(frame, textvariable=self.var)
        entry = self.entry
        entry.pack(fill=X, padx=5, expand=True)


class display_value():

    def __init__(self, master, label = "No label", value = "N/A", label_width = 20):
        self.master = master
        self.label = label
        self.label_width = label_width
        self.value = value
        self.initUI()

    def initUI(self):
        self.frame1 = Frame(self.master)
        frame1 = self.frame1
        frame1.pack(fill=X)

        self.lbl1 = Label(frame1, text=self.label, width=self.label_width)
        lbl1 = self.lbl1
        lbl1.pack(side=LEFT, padx=5, pady=5)
        
        self.lbl2 = Label(frame1, text=self.value, width=self.label_width)
        lbl2 = self.lbl2
        lbl2.pack(fill=X, padx=5, expand=True)
    
    def update(self, value = None):
        if value:
            self.value = value
        selection = self.value
        self.lbl2.config(text = selection)
    
class container(Frame):
    def __init__(self):
        super().__init__() 
