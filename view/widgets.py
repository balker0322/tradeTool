from tkinter import *
from tkinter.ttk import Frame, Label, Entry, Combobox, Treeview

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
        self.options = options
        self.initUI()

    def initUI(self):
        self.frame = Frame(self.master)
        frame = self.frame
        frame.pack(fill=X)

        self.lbl = Label(frame, text=self.label, width=self.label_width)
        lbl = self.lbl
        lbl.pack(side=LEFT, padx=5, pady=5)

        self.entry = Combobox(frame, values = self.options)
        entry = self.entry
        entry.pack(fill=X, padx=5, expand=True)
        entry.current(0)

    def get_value(self):
        return self.entry.current(), self.entry.get()

        
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

class Table():

    def __init__(self, master, columns):
        self.master = master
        self.columns = columns
        self.data_list = []
        self.initUI()

    def initUI(self):

        columns = (
            'date',
            'pair',
            'status',
            'profit',
        )

        self.tree = Treeview(self.master, columns=columns[1:])

        # Set the heading (Attribute Names)
        for i, column in enumerate(columns):
            self.tree.heading('#'+str(i), text=column)
            self.tree.column('#'+str(i), stretch=YES)

        self.tree.grid(row=4, columnspan=4, sticky='nsew')

        # self.tree = Treeview(self.master, columns = self.columns)

        # # Set the heading (Attribute Names)
        # for i, column in enumerate(self.columns):
        #     self.tree.heading('#'+str(i), text=column)
        #     self.tree.column('#'+str(i), stretch=YES)

        # self.tree.grid(row=1, columnspan=1)#, sticky='nsew')
        # self.tree.pack(fill=X, padx=5, expand=True)
    
    def update(self, value = None):
        pass
        # if value:
        #     self.value = value
        # selection = self.value
        # self.lbl2.config(text = selection)

    
class container(Frame):
    def __init__(self):
        super().__init__() 
