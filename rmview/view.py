from .mainapplication import MainApplication

class View:

    def __init__(self):
        self.view = MainApplication()

    def runapp(self):
        self.view.mainloop()