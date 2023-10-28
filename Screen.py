from tkinter import *

class Screen:
    def __init__(self,title,window=None,size=[300,200]):
        self.title = title
        if window is None:
            self.window = Tk(title)
        else:
            self.window = window
        self.size = size
        self.window.config(width=size[0],height=size[1])
        self.window.title(title)
        self.window.grid()
        # self.rideredirect()
    
    # top_bar[0] image
    # top_bar[1] Label
    # top_bar[2] Button minimized
    # top_bar[3] Button resize
    # top_bar[4] Button close

    def rideredirect(self):
        self.window.overrideredirect(True)
        self.top_bar = []
        self.top_bar.append(Label(self.window,text=self.title))
        
        
    def start(self):
        self.window.mainloop()