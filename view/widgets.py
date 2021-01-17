from tkinter import *
from tkinter.ttk import Frame, Label, Entry, Combobox, Treeview, Scrollbar


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

        columns = self.columns

        self.tree = Treeview(self.master, columns=columns)

        # scrollbars
        self.vsb = Scrollbar(self.master, orient="vertical", command=self.tree.yview)
        # self.vsb.place(relx=0.978, rely=0.175, relheight=0.713, relwidth=0.020)
        self.vsb.pack(side='right', fill='y')

        self.hsb = Scrollbar(self.master, orient="horizontal", command=self.tree.xview)
        self.hsb.pack(side='bottom', fill='x')
        # self.hsb.place(relx=0.014, rely=0.875, relheight=0.020, relwidth=0.965)

        self.tree.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)
        
        # hide default first column
        self.tree.heading('#0', text='')
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)

        # Set the heading (Attribute Names)
        for i, column in enumerate(columns):
            self.tree.heading('#'+str(i+1), text=column)
            self.tree.column('#'+str(i+1), width=100, anchor='c') #, stretch=YES)

        # self.tree.grid(row=4, columnspan=4, sticky='nsew')
        self.tree.pack()
    

    def update(self, rows):
        current_entry_in_row = [child for child in self.tree.get_children()]

        for row in rows:

            if not str(row['id']) in current_entry_in_row:
                self.insert_row(row['id'], row['content'])
                continue
            
            for child in current_entry_in_row:
                if row['id'] == int(child):
                    self.tree.item(child, text='', values=row['content'])
                    break

    def update_row(self, id, values):
        pass


    def insert_row(self, id, values):
        self.tree.insert('', 0, iid=id, values=values)
    

    # def refresh(self, rows):
    #     i = 0
    #     for x in rows:
    #         row = x['content']
    #         self.tree.insert('', 'end', iid=i, text=row[0], values=tuple(row[1:]))
    #         i += 1
    #     curent_id_in_row = [int(child) for child in self.tree.get_children()]
    #     print(curent_id_in_row)


    def delete_all(self):
        self.tree.delete(*self.tree.get_children())
    

class container(Frame):
    def __init__(self):
        super().__init__() 
