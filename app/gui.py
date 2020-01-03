import tkinter as tk

class OnScreen(object):
    def __init__(self,master):
        self.master = master
        # set the title
        self.master.title('Product app')
        # set the dimensions
        full_width=self.master.winfo_screenwidth()
        full_height=self.master.winfo_screenheight()
        self.master.geometry("%dx%d+%d+%d" % (full_width/2,full_height/2,full_width/4,full_height/4))
        # set bg
        self.master.config(bg="#1b2a49")
        #call the widget funtion to crate widgets
        self.AddWidgets()

    def AddWidgets(self):
        pass


#if __name__ == '__main__':
def show():
    
    #create a Tk() object
    screen = tk.Tk()
    app = OnScreen(screen)   
    screen.mainloop()