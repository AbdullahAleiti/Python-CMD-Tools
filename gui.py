try:
    import Tkinter
    import tkMessageBox
    import Time
    from Tkinter import Entry,Label
except ImportError:
    print "Error : your system dosn't support Tkinter GUI, either it is a command line interface or you do not have \
the Tkinter library installed."
    exit()

class parent():
    def __init__(self,name):
        top = Tkinter.Tk()

        def helloCallBack():
            tkMessageBox.showinfo("time", Time.getTime(False))

        self.B = Tkinter.Button(top, text="show time", bg="gray", command=helloCallBack)
        self.L = Tkinter.Label(top, text="hi %s" % name , fg = "orange")
        Label(top,text="enter anything :").grid(row=1 ,column=0)
        E = Entry(top)
        self.L.grid(row=0 ,column=1)
        E.grid(row=1 ,column=1)
        self.B.grid(row=3 , column=1)
        Text = E.get();
        Label(top,text=Text).grid(row=4 ,column=1)
        top.mainloop()

    def object(self):
        pass
