import tkinter as tk


class EntryComponent(tk.Frame):
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        label = tk.Label(self, text='label', anchor=tk.W)
        label.pack(fill=tk.X)
        
        left_frame = tk.Frame(self)
        left_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)

        entry = tk.Entry(left_frame)
        entry.pack(fill=tk.X, expand=True)

        button_list = ['button1', 'button2', 'button3', 'button4']
        buttons = []

        for button_item in button_list:
            button = tk.Button(left_frame, text=button_item)
            button.pack(side=tk.LEFT, fill=tk.X, expand=True)
            buttons.append(button)
            
        right_frame = tk.Frame(self)
        right_frame.pack(side=tk.LEFT, fill=tk.Y)

        submit_button = tk.Button(right_frame, text='submit')
        submit_button.pack(side=tk.TOP)

