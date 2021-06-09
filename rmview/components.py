import tkinter as tk

class EntryComponent_A(tk.Frame):
    pass

class EntryComponent(tk.Frame):
    
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        # super().__init__(parent, *args, **kwargs)

        label = tk.Label(self, text=kwargs['label'], anchor=tk.W)
        label.pack(fill=tk.X)
        
        left_frame = tk.Frame(self)
        left_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.entry_variable = tk.StringVar()
        entry = tk.Entry(left_frame, textvariable=self.entry_variable)
        entry.pack(fill=tk.X, expand=True)

        buttons = []

        for button_item in kwargs['button_list']:
            button = tk.Button(left_frame, text=button_item['text'], command=button_item['command'])
            button.pack(side=tk.LEFT, fill=tk.X, expand=True)
            buttons.append(button)
            
        right_frame = tk.Frame(self)
        right_frame.pack(side=tk.LEFT, fill=tk.Y)

        submit_button = tk.Button(right_frame, text=kwargs['submit_button']['text'], command=kwargs['submit_button']['command'])
        submit_button.pack(side=tk.TOP)
    
    def set_entry(self, set_var):
        self.entry_variable.set(set_var)

    def get_entry(self):
        return self.entry_variable.get()

