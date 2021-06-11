import tkinter as tk
import tkinter.ttk as ttk


class EntryComponent_A(tk.Frame):
    # entry widget and submit button
    
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        # super().__init__(parent, *args, **kwargs)

        label = tk.Label(self, text=kwargs['label'], anchor=tk.W)
        label.pack(fill=tk.X)

        input_frame = tk.Frame(self)
        input_frame.pack(fill=tk.BOTH, expand=True)
        
        left_frame = tk.Frame(input_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.entry_variable = tk.StringVar()
        entry = tk.Entry(left_frame, textvariable=self.entry_variable)
        entry.pack(fill=tk.X, expand=True)
            
        right_frame = tk.Frame(input_frame)
        right_frame.pack(side=tk.LEFT, fill=tk.Y)

        submit_button = tk.Button(right_frame, text=kwargs['submit_button']['text'], command=kwargs['submit_button']['command'])
        submit_button.pack(side=tk.TOP)

        dummy_label = tk.Label(self, text='')
        dummy_label.pack(fill=tk.X)
    
    def set_entry(self, set_var):
        self.entry_variable.set(set_var)

    def get_entry(self):
        return self.entry_variable.get()



class EntryComponent_B(tk.Frame):
    # entry widget, submit button and quick entry buttons
    
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        # super().__init__(parent, *args, **kwargs)

        label = tk.Label(self, text=kwargs['label'], anchor=tk.W)
        label.pack(fill=tk.X)

        input_frame = tk.Frame(self)
        input_frame.pack(fill=tk.BOTH, expand=True)
        
        left_frame = tk.Frame(input_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)

        button_list_frame = tk.Frame(left_frame)
        button_list_frame.pack(fill=tk.X, expand=True)

        buttons = []

        for button_item in kwargs['button_list']:
            button = tk.Button(button_list_frame, text=button_item['text'], command=button_item['command'])
            button.pack(side=tk.LEFT, fill=tk.X, expand=True)
            buttons.append(button)

        self.entry_variable = tk.StringVar()
        entry = tk.Entry(left_frame, textvariable=self.entry_variable)
        entry.pack(fill=tk.X, expand=True)
            
        right_frame = tk.Frame(input_frame)
        right_frame.pack(side=tk.LEFT, fill=tk.Y)

        submit_button = tk.Button(right_frame, text=kwargs['submit_button']['text'], command=kwargs['submit_button']['command'])
        submit_button.pack(side=tk.BOTTOM)

        dummy_label = tk.Label(self, text='')
        dummy_label.pack(fill=tk.X)
    
    def set_entry(self, set_var):
        self.entry_variable.set(set_var)

    def get_entry(self):
        return self.entry_variable.get()



class EntryComponent_C(tk.Frame):
    # multiple buttons in single row
    
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text=kwargs['label'], anchor=tk.W)
        label.pack(fill=tk.X)

        input_frame = tk.Frame(self)
        input_frame.pack(fill=tk.BOTH, expand=True)
        
        button_frame = tk.Frame(input_frame)
        button_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)

        buttons = []

        for button_item in kwargs['button_list']:
            button = tk.Button(button_frame, text=button_item['text'], command=button_item['command'])
            button.pack(side=tk.LEFT, fill=tk.X, expand=True)
            buttons.append(button)

        dummy_label = tk.Label(self, text='')
        dummy_label.pack(fill=tk.X)
    
    def set_entry(self, set_var):
        self.entry_variable.set(set_var)

    def get_entry(self):
        return self.entry_variable.get()



class EntryComponent_D(tk.Frame):
    # entry widget, and quick entry buttons
    
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        # super().__init__(parent, *args, **kwargs)

        label = tk.Label(self, text=kwargs['label'], anchor=tk.W)
        label.pack(fill=tk.X)

        input_frame = tk.Frame(self)
        input_frame.pack(fill=tk.BOTH, expand=True)
        
        left_frame = tk.Frame(input_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.entry_variable = tk.StringVar()
        entry = tk.Entry(left_frame, textvariable=self.entry_variable)
        entry.pack(fill=tk.X, expand=True)

        buttons = []

        for button_item in kwargs['button_list']:
            button = tk.Button(left_frame, text=button_item['text'], command=button_item['command'])
            button.pack(side=tk.LEFT, fill=tk.X, expand=True)
            buttons.append(button)

        dummy_label = tk.Label(self, text='')
        dummy_label.pack(fill=tk.X)
    
    def set_entry(self, set_var):
        self.entry_variable.set(set_var)

    def get_entry(self):
        return self.entry_variable.get()




class Container_A(tk.LabelFrame):
    
    def __init__(self, parent, *args, **kwargs):
        tk.LabelFrame.__init__(self, parent, text=kwargs['text'])


class VerticalScrolledFrame(tk.Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling

    """
    def __init__(self, parent, *args, **kw):
        tk.Frame.__init__(self, parent, *args, **kw)            

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = tk.Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=tk.NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)



class ScrolledWindow(tk.Frame):
    """
    1. Master widget gets scrollbars and a canvas. Scrollbars are connected 
    to canvas scrollregion.

    2. self.scrollwindow is created and inserted into canvas

    Usage Guideline:
    Assign any widgets as children of <ScrolledWindow instance>.scrollwindow
    to get them inserted into canvas

    __init__(self, parent, canv_w = 400, canv_h = 400, *args, **kwargs)
    docstring:
    Parent = master of scrolled window
    canv_w - width of canvas
    canv_h - height of canvas

    """


    def __init__(self, parent, canv_w = 400, canv_h = 400, *args, **kwargs):
        """Parent = master of scrolled window
        canv_w - width of canvas
        canv_h - height of canvas

       """
        super().__init__(parent, *args, **kwargs)

        self.parent = parent

        # creating a scrollbars
        self.xscrlbr = ttk.Scrollbar(self.parent, orient = 'horizontal')
        self.xscrlbr.grid(column = 0, row = 1, sticky = 'ew', columnspan = 2)         
        self.yscrlbr = ttk.Scrollbar(self.parent)
        self.yscrlbr.grid(column = 1, row = 0, sticky = 'ns')         
        # creating a canvas
        self.canv = tk.Canvas(self.parent)
        self.canv.config(relief = 'flat',
                         width = 10,
                         heigh = 10, bd = 2)
        # placing a canvas into frame
        self.canv.grid(column = 0, row = 0, sticky = 'nsew')
        # accociating scrollbar comands to canvas scroling
        self.xscrlbr.config(command = self.canv.xview)
        self.yscrlbr.config(command = self.canv.yview)

        # creating a frame to inserto to canvas
        self.scrollwindow = ttk.Frame(self.parent)

        self.canv.create_window(0, 0, window = self.scrollwindow, anchor = 'nw')

        self.canv.config(xscrollcommand = self.xscrlbr.set,
                         yscrollcommand = self.yscrlbr.set,
                         scrollregion = (0, 0, 100, 100))

        self.yscrlbr.lift(self.scrollwindow)        
        self.xscrlbr.lift(self.scrollwindow)
        self.scrollwindow.bind('<Configure>', self._configure_window)  
        self.scrollwindow.bind('<Enter>', self._bound_to_mousewheel)
        self.scrollwindow.bind('<Leave>', self._unbound_to_mousewheel)

        return

    def _bound_to_mousewheel(self, event):
        self.canv.bind_all("<MouseWheel>", self._on_mousewheel)   

    def _unbound_to_mousewheel(self, event):
        self.canv.unbind_all("<MouseWheel>") 

    def _on_mousewheel(self, event):
        self.canv.yview_scroll(int(-1*(event.delta/120)), "units")  

    def _configure_window(self, event):
        # update the scrollbars to match the size of the inner frame
        size = (self.scrollwindow.winfo_reqwidth(), self.scrollwindow.winfo_reqheight())
        self.canv.config(scrollregion='0 0 %s %s' % size)
        if self.scrollwindow.winfo_reqwidth() != self.canv.winfo_width():
            # update the canvas's width to fit the inner frame
            self.canv.config(width = self.scrollwindow.winfo_reqwidth())
        if self.scrollwindow.winfo_reqheight() != self.canv.winfo_height():
            # update the canvas's width to fit the inner frame
            self.canv.config(height = self.scrollwindow.winfo_reqheight())
